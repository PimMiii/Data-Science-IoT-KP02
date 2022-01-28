import datetime
import time

# import RPi.GPIO to use the GPIO interface on the RPi
import RPi.GPIO as GPIO
# import adafruit DHT module to read data from the DHT11 sensor
import Adafruit_DHT as dht

# import from Colorama to output colored text to the terminal
from colorama import Fore
from colorama import Style

# import config file and set its variables
import config

writeAPIkey = config.writeAPIkey
channelID = config.channelID
url = config.url

posting_interval = 15  # Post data once every 15 seconds
last_update = time.time()  # Track the last update time

task = None
task_status = None
task_start = None
task_end = None
task_duration = None

green_button = 10
red_button = 8

DHT_SENSOR = dht.DHT11
DHT_PIN = 4

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pins to be an input pin and set initial value to be pulled low (off)
GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def start_task():
    # Starts a task, by timestamping the start time
    global task_start
    if not task_start:  # if no task is running
        task_start = time.time()  # timestamp task start
        print(f"{Fore.CYAN}Button Pressed{Style.RESET_ALL}: Task Started!")
        print(task_start)
    else:
        print(f"{Fore.YELLOW}Task already running!{Style.RESET_ALL}")
        print(f"To {Fore.GREEN} finish{Style.RESET_ALL} current task press"
              f" the red button.")
        print(f"To {Fore.RED}cancel{Style.RESET_ALL} current task press"
              f" and hold the red button.")


def cancel_task():
    # Cancel a task, sets task_Status to cancelled. timestamps end time.
    global task_status
    global task_start
    global task_end
    if not task_start:
        print("no task to cancel")
    else:
        task_status = 'cancelled'  # set status to cancelled
        task_end = time.time()  # timestamp task end
        print(f"{Fore.RED}Task cancelled!{Style.RESET_ALL}")
        print(str(task_end) + "\n\n")


def finish_task():
    # Finished task, sets task_status to finished, and timestamps end time.
    global task_status
    global task_start
    global task_end
    if not task_start:
        print("no task to stop.")
    else:
        task_status = 'finished'  # set status to finished
        task_end = time.time()  # timestamp task end
        print(f"{Fore.GREEN}Task finished!{Style.RESET_ALL}")
        print(str(task_end) + "\n\n")


# set button events for GPIO to listen for.
GPIO.add_event_detect(green_button, GPIO.RISING, bouncetime=200)
GPIO.add_event_detect(red_button, GPIO.RISING, bouncetime=200)

if __name__ == '__main__':
    while True:
        if GPIO.event_detected(green_button):
            print(f"{Fore.GREEN}Button Pressed{Style.RESET_ALL}\n")
            start_task()
            time.sleep(0.2)

        if GPIO.event_detected(red_button):
            time.sleep(0.5)  # wait half a second
            if GPIO.input(red_button) == 1:  # check if button is still pressed
                cancel_task()
            else:
                finish_task()
            if task_start:
                task_duration = round(task_end - task_start, 3)
                task = [task_status, task_start, task_end, task_duration]
                print(task)
                task_start = None  # reset task

        if time.time() - last_update >= posting_interval:
            date = datetime.datetime.now()
            humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None and task is not None:
                message = {'created_at': date.strftime("%G %X %z"),
                           'task_Status': task[0],
                           'task_start': task[1],
                           'task_end': task[2],
                           'task_duration': task[3],
                           'temp': temperature,
                           'humidity': humidity}
                print(message)
                task = None  # reset task after writing it into the message
            elif humidity is not None and temperature is not None:
                message = {'created_at': date.strftime("%G %X %z"),
                           'temp': temperature,
                           'humidity': humidity}
                print(message)
            else:
                print("Sensor failure. Check wiring.")
            last_update = time.time()
