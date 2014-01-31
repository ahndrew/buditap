import pygame
from randomsong import randomsong

class playsound:
	def __init__(self):
		self.song = "" 	
	
	def playSong(self):
		rs = randomsong()
		self.song = rs.getRandomSong()

		pygame.mixer.init()
		pygame.mixer.music.load(rs.getSongPath() + self.song)
		pygame.mixer.music.play()

		pygame.mixer.music.set_endevent(pygame.USEREVENT)

		if pygame.mixer.music.get_busy():
			print self.song + " is playing"
			print "Beer is pouring"

	def isSongPlaying(self):
		return pygame.mixer.music.get_busy()
	
	def stopPlaying(self):
		pygame.mixer.init()
		pygame.mixer.music.fadeout(50)
