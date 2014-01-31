#io_button_test
from RPi.GPIO import RPi.GPIO as GPIO
import time

#adjust for where your switch is connected
buttonPin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

while True:
  if (GPIO.input(17)):
    print("Button Pressed")