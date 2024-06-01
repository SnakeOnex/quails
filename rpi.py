import RPi.GPIO as GPIO
import time

# Set up GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    # Turn on the LED
    print("LED on")
    GPIO.output(17, GPIO.HIGH)
    time.sleep(5)  # LED will stay on for 5 seconds

    # Turn off the LED
    print("LED off")
    GPIO.output(17, GPIO.LOW)

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
