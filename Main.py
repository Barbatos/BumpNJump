#!/usr/bin/python

import pygame
import Resources
from pygame.locals import *
from MainMenu import *

class BumpNJump():
	def __init__(self):
		screenWidth = 1000
		screenHeight = 600

		pygame.init()
		if(Resources.getOptionValue("fullscreen") == 1):
			pygame.display.set_mode((screenWidth, screenHeight), FULLSCREEN)
		else:
			pygame.display.set_mode((screenWidth, screenHeight))
		pygame.display.set_caption("Bump'N'Jump")

		pygame.mixer.music.load("resources/sound/music.wav")
		pygame.mixer.music.set_volume(float(Resources.getOptionValue("music"))/100)
		pygame.mixer.music.play(-1)

		currentScene = MainMenu()

		clock = pygame.time.Clock()

		game = True

		while game:
			game, currentScene = currentScene.update()

			clock.tick(60)

if __name__ == '__main__': 
	BumpNJump()