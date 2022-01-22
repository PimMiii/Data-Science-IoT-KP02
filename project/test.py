import time

# import RPi.GPIO to use the GPIO interface on the RPi
import RPi.GPIO as GPIO

# import from Colorama to output colored text to the terminal
from colorama import Fore
from colorama import Style


def task_start():
    GPIO.output(12, GPIO.HIGH)
    start = time.perf_counter()  # timestamp starting time
    print(f"{Fore.YELLOW}Task Started: {Style.RESET_ALL}" + str(start))
    return start


def task_end():
    GPIO.output(12, GPIO.LOW)
    end = time.perf_counter()  # timestamp end time
    print(f"{Fore.YELLOW}Task Ended: {Style.RESET_ALL}" + str(end))
    return end


def calculate_task_duration(start, end):
    task_duration = round((end - start), 3)
    print(f"\n{Fore.GREEN}Task Completed!{Style.RESET_ALL} It took you: "
          + str(task_duration) +
          " seconds to complete task \n\n")
    return task_duration


GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pins to be an input pin and set initial value to be pulled low (off)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Set pin 12 to be an output and initial low (off)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

start = None
end = None
duration = None
await_confirmation = False
posted_confirmation = False

while True:  # Run forever
    while await_confirmation:
        if not(posted_confirmation):
            print(f"{Fore.CYAN}\nThere's already a task in progress. \n"
                  f"{Fore.WHITE}Are you sure you want to start a new task?\n"
                  f"{Style.BRIGHT}{Fore.GREEN}Y{Fore.WHITE}/"
                  f"{Fore.RED}N{Style.RESET_ALL}")
            posted_confirmation = True
            time.sleep(0.2)
        if GPIO.input(10) == GPIO.HIGH:
            print(f"{Fore.GREEN}\nStarting new task...\n")
            start = task_start()
            time.sleep(0.2)
            posted_confirmation = False
            await_confirmation = False
        elif GPIO.input(8) == GPIO.HIGH:
            print(f"{Fore.RED}\nN{Style.RESET_ALL}: No new task started\n")
            time.sleep(0.2)
            posted_confirmation = False
            await_confirmation = False
            break

    while not (await_confirmation):
        if GPIO.input(10) == GPIO.HIGH:
            if start:
                await_confirmation = True
                break

            else:
                start = task_start()
                time.sleep(0.2)  # to combat counting multiple presses

        if GPIO.input(8) == GPIO.HIGH:
            if start:
                end = task_end()
                duration = calculate_task_duration(start, end)
                start = None
                time.sleep(0.2)  # to combat counting multiple presses
            else:
                print(f"{Fore.RED}Can't stop task!"
                      f" No task has been started. {Style.RESET_ALL}")
                time.sleep(0.2)
