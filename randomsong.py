import os
import random

FULL_MUSIC_PATH = "/home/pi/buditap/music/"

class randomsong:
	def __init__(self):
		self.music = []

	def getSongPath(self):
		return FULL_MUSIC_PATH 

	def getRandomSong(self):
		i = 0

		for file in os.listdir(FULL_MUSIC_PATH):
			if file.endswith(".mp3"):
				self.music.append(file)

		return self.music[random.randint(0, len(self.music) - 1)]
