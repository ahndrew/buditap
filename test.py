from playsound import playsound
import time
import pygame

FRAMERATE = 30

ps = playsound()

ps.playSong()

clock = pygame.time.Clock()

i = 0

while ps.isSongPlaying():
	clock.tick(FRAMERATE)
	i += 1
	print i
	if i > 50:
		ps.stopPlaying()

print "Music ended"
