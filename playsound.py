import pygame
import sys
import time
import randomsong

from randomsong import randomsong

rs = randomsong()

song = rs.getRandomSong()

FRAMERATE = 30

pygame.mixer.init()
pygame.mixer.music.load(rs.getSongPath() + song)
pygame.mixer.music.play()

pygame.mixer.music.set_endevent(pygame.USEREVENT)

clock = pygame.time.Clock()

if pygame.mixer.music.get_busy():
	print song + " is playing"

while pygame.mixer.music.get_busy():
	clock.tick(FRAMERATE)

print "Music ended"
