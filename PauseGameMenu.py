#!/usr/bin/python

import pygame
from pygame.locals import *
from Button import *

class PauseGameMenu():
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.backgroundRect = pygame.Rect(0, 0, 250, 400)
		self.backgroundRect.center = (self.screen.get_rect().center)

		self.buttons = {}

		self.buttons["resume"] = Button(self.screen.get_width()/2 - 200/2, self.screen.get_rect().h/2 - 170, 200, 40, "RESUME")
		self.buttons["loadlevel"] = Button(self.screen.get_width()/2 - 200/2, self.screen.get_rect().h/2 - 70, 200, 40, "LOAD LEVEL")
		self.buttons["mainMenu"] = Button(self.screen.get_width()/2 - 200/2, self.screen.get_rect().h/2 + 130, 200, 40, "MAIN MENU")

	def update(self):
		pygame.draw.rect(self.screen, (50, 50, 50), self.backgroundRect)

		for button in self.buttons.values():
			button.update()