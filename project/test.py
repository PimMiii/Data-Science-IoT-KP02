import time

import RPi.GPIO as GPIO


def taskStart():
    GPIO.output(12, GPIO.HIGH)
    start = time.perf_counter()
    return start


def taskEnd():
    GPIO.output(12, GPIO.LOW)
    end = time.perf_counter()
    return end


GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pins to be an input pin and set initial value to be pulled low (off)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

while True:  # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        start = taskStart()
        print(start)
    if GPIO.input(8) == GPIO.HIGH:
        end = taskEnd()
        print(end)
        print("Task took:" + str(end - start) + "seconds")
