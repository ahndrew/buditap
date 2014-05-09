import os
import random

BASE_MUSIC_PATH = "/home/pi/buditap/themes/"

with open ("current_theme.txt", "r") as myfile:
    THEME=myfile.read().replace('\n', '')

FULL_MUSIC_PATH = BASE_MUSIC_PATH + THEME + "/"

print "current theme is: " + FULL_MUSIC_PATH

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
