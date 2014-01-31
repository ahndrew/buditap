import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
 
print "Ready."
 
while True:
  try:
    if GPIO.input(24):
      print "HIGH"
    else:
      print "LO"
 
    sleep(1)
  except KeyboardInterrupt:
    exit()