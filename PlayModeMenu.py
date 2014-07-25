#!/usr/bin/python

import pygame
from Button import *
from GameMenu import *
from MultiMenu import *
from pygame.locals import *

class PlayModeMenu():
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.buttons = {}

		self.buttons["local"] = Button(self.screen.get_width()/2 - 200/2, self.screen.get_height()/2 - 150 - 40/2, 200, 40, "LOCAL")
		self.buttons["network"] = Button(self.screen.get_width()/2 - 200/2, self.screen.get_height()/2 - 50 - 40/2, 200, 40, "NETWORK")
		self.buttons["back"] = Button(self.screen.get_width()/2 - 200/2, self.screen.get_height()/2 + 50 - 40/2, 200, 40, "BACK")
		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()

		for event in pygame.event.get():
			if event.type == QUIT or (key[K_F4] and key[K_LALT]):
				return False, self

			elif event.type == MOUSEBUTTONDOWN:
				mse = pygame.mouse.get_pos()

				if self.buttons["local"].onButton(mse):
					return True, GameMenu()

				elif self.buttons["network"].onButton(mse):
					return True, MultiMenu()

				elif self.buttons["back"].onButton(mse):
					return True, MainMenu.MainMenu()

			elif event.type == MOUSEMOTION:
				mse = pygame.mouse.get_pos()

				pygame.mouse.set_cursor(*pygame.cursors.arrow)

				for button in self.buttons.values():
					if button.onButton(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)

		self.screen.blit(self.background, self.background.get_rect(), self.background.get_rect())

		for button in self.buttons.values():
			button.update()

		pygame.display.update()

		return True, self