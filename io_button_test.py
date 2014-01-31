#io_button_test
import RPi.GPIO as GPIO
import time
#GPIO.setmode(BCM)
#adjust for where your switch is connected
#buttonPin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)
input = GPIO.input(24)

while True:
  if (GPIO.input(24)):
    print("Button Pressed")