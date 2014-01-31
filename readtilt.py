from time import sleep
import RPi.GPIO as GPIO
from sys import exit
from playsong import playsound
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
 
print "Ready."
 
while True:
  ps = playsound()
  try:
    if GPIO.input(24):
      print "HIGH"
      ps.playSong()
      ps.isisSongPlaying()
    else:
      print "LO"
      ps.stopPlaying()
    sleep(.7)
  except KeyboardInterrupt:
    exit()