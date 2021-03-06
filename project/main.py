import json
import datetime
import time
import requests

# import RPi.GPIO to use the GPIO interface on the RPi
import RPi.GPIO as GPIO
# import adafruit DHT module to read data from the DHT11 sensor
import Adafruit_DHT as dht

# import from Colorama to output colored text to the terminal
from colorama import Fore
from colorama import Style

# import config file and set its variables
from config import write_api_key, channel_id, write_url


posting_interval = 15  # Post data once every 15 seconds
last_update = time.time()  # Track the last update time
message_buffer = []

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
        print(f"To {Fore.GREEN}finish{Style.RESET_ALL} current task press"
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
        task_status = 0  # set status to 0 (cancelled)
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
        task_status = 1  # set status to finished
        task_end = time.time()  # timestamp task end
        print(f"{Fore.GREEN}Task finished!{Style.RESET_ALL}")
        print(str(task_end) + "\n\n")


def httprequest():
    # Function to send the POST request to ThingSpeak channel for bulk update.
    global message_buffer
    # Format the json data buffer
    data = {'api_key': write_api_key, 'updates': message_buffer}

    print(data)
    r = requests.post(url=write_url + message_buffer[0])  # Post the data
    if r.status_code == 200:
        message_buffer = []  # Reinitialize the message buffer
        print(f"{Fore.GREEN}" + str(r.status_code) + f"{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}" + str(r.status_code) + f"{Style.RESET_ALL}")
        print(r.json())
    global last_update
    last_update = time.time()  # Update the connection time


# set button events for GPIO to listen for.
GPIO.add_event_detect(green_button, GPIO.RISING, bouncetime=200)
GPIO.add_event_detect(red_button, GPIO.RISING, bouncetime=200)

if __name__ == '__main__':
    # print APIKey, channelID and url to console for human verification
    print(f"{Fore.CYAN}APIKey: {Style.RESET_ALL}" + write_api_key)
    print(f"{Fore.CYAN}ChannelID: {Style.RESET_ALL}" + channel_id)
    print(f"{Fore.CYAN}URL: {Style.RESET_ALL}" + write_url)

    # main loop
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
                if task_duration >= 15:
                    task = [task_status, task_start, task_end, task_duration]
                    print(task)
                else:
                    print(f"{Fore.YELLOW}Tasks shorter than 15 seconds"
                          f" won't be logged{Style.RESET_ALL}")
                task_start = None  # reset task

        if time.time() - last_update >= posting_interval:
            message = ''
            date = datetime.datetime.now()
            date = datetime.datetime.replace(date, tzinfo=datetime.timezone.utc)
            humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)
            if task is not None:
                message = message + '&field1=' + str(task[0]) + '&field2=' + str(
                    task[1]) + '&field3=' + str(task[2]) + '&field4=' + str(
                    task[3])
                task = None  # reset task after writing it into the message
            if humidity is not None and temperature is not None:
                message = message + '&field5=' + str(
                    temperature) + '&field6=' + str(humidity)
                print("Temp: " + str(temperature) + " Humidity: " + str(
                    humidity))
            else:
                print(f"{Fore.RED}Sensor failure. Check wiring."
                      f"{Style.RESET_ALL}")
            if message != '':
                message_buffer.append(message)
                httprequest()
                message = ''
