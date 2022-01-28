import time
import datetime

# import RPi.GPIO to use the GPIO interface on the RPi
import RPi.GPIO as GPIO

# import from Colorama to output colored text to the terminal
from colorama import Fore
from colorama import Style

task_start = None
task_status = None
task_end = None
press_duration = 0

green_button = 10
red_button = 8

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pins to be an input pin and set initial value to be pulled low (off)
GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def start_task():
    global task_start
    if not task_start:  # if no task is running
        task_start = datetime.datetime.now()  # timestamp task start
        print(f"{Fore.CYAN}Button Pressed{Style.RESET_ALL}: Task Started!")
        print(task_start)
    else:
        print(f"{Fore.YELLOW}Task already running!{Style.RESET_ALL}")
        print(f"To {Fore.GREEN} finish{Style.RESET_ALL} current task press"
              f" the red button.")
        print(f"To {Fore.RED}cancel{Style.RESET_ALL} current task press"
              f" and hold the red button.")


def cancel_task():
    global task_status
    global task_start
    global task_end
    if not task_start:
        print("no task to cancel")
    else:
        task_status = 'cancelled'  # set status to cancelled
        task_end = datetime.datetime.now()  # timestamp task end
        print(f"{Fore.RED}Long Press{Style.RESET_ALL}: Task cancelled!")
        print(str(task_end) + "\n\n")
        task_start = None  # reset task


def finish_task():
    global task_status
    global task_start
    global task_end
    if not task_start:
        print("no task to stop.")
    else:
        task_status = 'finished'  # set status to finished
        task_end = datetime.datetime.now()  # timestamp task end
        print(f"{Fore.GREEN}Task finished!{Style.RESET_ALL}")
        print(str(task_end) + "\n\n")
        task_start = None  # reset task


GPIO.add_event_detect(green_button, GPIO.RISING, bouncetime=200)
GPIO.add_event_detect(red_button, GPIO.RISING)

while True:
    if GPIO.event_detected(green_button):
        print(f"{Fore.GREEN}Button Pressed{Style.RESET_ALL}\n")
        start_task()
        time.sleep(0.2)
    if GPIO.event_detected(red_button):
        if GPIO.input(red_button) == 1:
            start = time.perf_counter()
            print(f"{Fore.RED}Button Pressed{Style.RESET_ALL}\n")
        if GPIO.input(red_button) == 0:
            end = time.perf_counter()
            elapsed = end - start
            press_duration = int(elapsed)
            if press_duration < 1:  # short press
                finish_task()
            elif press_duration >= 1:  # long press
                cancel_task()
