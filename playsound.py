import pygame

pygame.mixer.init()
pygame.mixer.music.load("budligt_real_chinese.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
	pygame.time.delay(100)
