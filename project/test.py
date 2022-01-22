import RPi.GPIO as GPIO

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pins to be an input pin and set initial value to be pulled low (off)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

while True:  # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        GPIO.output(12, GPIO.HIGH)
    if GPIO.input(8) == GPIO.HIGH:
        GPIO.output(12, GPIO.LOW)
