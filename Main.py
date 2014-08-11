#!/usr/bin/python

import pygame
import Resources
from pygame.locals import *
from MainMenu import *

class BumpNJump():
	def __init__(self):
		pygame.init()
		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		pygame.mixer.music.load("resources/sound/music.wav")
		pygame.mixer.music.set_volume(float(Resources.getOptionValue("music"))/100)
		pygame.mixer.music.play(-1)

		# music = pygame.mixer.Sound("resources/sound/music.wav")
		# music.play(-1)

		currentScene = MainMenu()

		clock = pygame.time.Clock()

		game = True

		while game:
			game, currentScene = currentScene.update()

			clock.tick(60)

if __name__ == '__main__': 
	BumpNJump()