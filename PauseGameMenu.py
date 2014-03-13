#!/usr/bin/python

import pygame
from pygame.locals import *
from Button import *

class PauseGameMenu():
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.backgroundRect = pygame.Rect(0, 0, 250, 450)
		self.backgroundRect.center = (self.screen.get_rect().center)

	def update(self):
		pygame.draw.rect(self.screen, (50, 50, 50), self.backgroundRect)