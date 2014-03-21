#!/usr/bin/python

import pygame
from pygame.locals import *
from Button import *

class PauseGameMenu():
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.backgroundRect = pygame.Rect(0, 0, 250, 450)
		self.backgroundRect.center = (self.screen.get_rect().center)

		self.buttons = {}

		self.buttons["resume"] = Button(self.screen.get_width()/2 - 200/2, 100, 200, 40, "RESUME")
		self.buttons["load level"] = Button(self.screen.get_width()/2 - 200/2, 200, 200, 40, "LOAD LEVEL")
		self.buttons["mainMenu"] = Button(self.screen.get_width()/2 - 200/2, 400, 200, 40, "MAIN MENU")

	def update(self):
		pygame.draw.rect(self.screen, (50, 50, 50), self.backgroundRect)

		for button in self.buttons.values():
			button.update()