#!/usr/bin/python

import pygame
from pygame.locals import *
from MainMenu import *


class BumpNJump():
	def __init__(self):
		pygame.init()
		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		self.music = pygame.mixer.Sound("resources/sound/music.wav")
		self.music.play(-1)

		currentScene = MainMenu()

		clock = pygame.time.Clock()

		game = True

		while game:
			game, currentScene = currentScene.update()

			clock.tick(60)

if __name__ == '__main__': 
	BumpNJump()