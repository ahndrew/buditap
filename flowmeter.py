import RPi.GPIO as GPIO
import sys, time
from twitter import *

t = Twitter( auth=OAuth('2463739201-D4QDkK5cZB9NHuVdlmVQWU38g2Xw2b3w8CfFpkU', 'OZ09NQ7ZsQNozY20Q15EkYIafSBjk6NLR6xh5Qj5Tmi6m', 'jHp2yiFarSBPkKcbVwSkMRx6o', 'uwdZPzZbQSfb5LHOSCujjv3mUtegDYrRt7Agqs2Dbi4Cn39Mm8') )

GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set up the flow meter
pouring = False
lastPinState = False
pinState = 0
lastPinChange = int(time.time() * 1000)
pourStart = 0
pinChange = lastPinChange
pinDelta = 0
hertz = 0
flow = 0 
litersPoured = 0
pintsPoured = 0

print 'start flowmeter'

while True:
	currentTime = int(time.time() * 1000)
	if GPIO.input(17):
		pinState = True
	#	print 'TRUE'
	else:
		pinState = False
	#	print 'FALSE'

	
	# If we have changed pin states low to high...
	if(pinState != lastPinState and pinState == True):
		if(pouring == False):
			print 'Pour Start'
			pourStart = currentTime
		pouring = True
		# get the current time
		pinChange = currentTime
		pinDelta = pinChange - lastPinChange
		if (pinDelta < 1000 and pinDelta > 0):
			# calculate the instantaneous speed
			hertz = 1000.0000 / pinDelta
			flow = hertz / (60 * 7.5) # L/s
			litersPoured += flow * (pinDelta / 1000.0000)
			pintsPoured = litersPoured * 2.11338
			print 'pintPoured: ' + str(pintsPoured) + ' litersPoured: ' + str(litersPoured)

	#print 'Pouring: ' + str(pouring) + ' ' + str(pinState) + ' ' + str(lastPinState) + ' currenttime: ' + str(currentTime) + ' pinChange: ' + str(pinChange) + ' pinDelta: ' + str(pinDelta)
	if (pouring == True and pinState == lastPinState and (currentTime - lastPinChange) > 3000):
		print 'Pouring is false'
		# set pouring back to false, tweet the current amt poured, and reset everything
		pouring = False
		if (pintsPoured > 0.1):
			pourTime = int((currentTime - pourStart)/1000) - 3
			tweet = 'Buditap has poured ' + str(round(pintsPoured,2)) + ' pints of beer in ' + str(pourTime) + ' seconds'
			t.statuses.update(status=tweet)
			print 'Buditap has poured ' + str(round(pintsPoured,2)) + ' pints of beer in ' + str(pourTime) + ' seconds'
			litersPoured = 0
			pintsPoured = 0

	lastPinChange = pinChange
	lastPinState = pinState
