#!/usr/bin/python

import pygame
from Button import *
from Slider import *
from Checkbox import *
from GameMenu import *
from Editor import *
from OptionMenu import *
from pygame.locals import *

class MainMenu():
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.buttons = {}

		self.buttons["play"] = Button(self.screen.get_width()/2 - 200/2, 100, 200, 40, "PLAY")
		self.buttons["editor"] = Button(self.screen.get_width()/2 - 200/2, 200, 200, 40, "EDITOR")
		self.buttons["option"] = Button(self.screen.get_width()/2 - 200/2, 300, 200, 40, "OPTION")
		self.buttons["quit"] = Button(self.screen.get_width()/2 - 200/2, 400, 200, 40, "QUIT")

		self.checkboxTest = Checkbox(50, 100, "test")

		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT or (key[K_F4] and key[K_LALT]):
				return False, self

			elif event.type == MOUSEBUTTONDOWN:
				mse = pygame.mouse.get_pos()
				if self.buttons["play"].onButton(mse):
					return True, GameMenu()

				elif self.buttons["editor"].onButton(mse):
					return True, Editor()

				elif self.buttons["option"].onButton(mse):
					return True, OptionMenu()

				elif self.buttons["quit"].onButton(mse):
					return False, self

				elif self.checkboxTest.onCheckbox(mse):
					self.checkboxTest.changeState()

			if event.type == MOUSEMOTION:
				mse = pygame.mouse.get_pos()

				for button in self.buttons.values():
					if button.onButton(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)

					else:
						pygame.mouse.set_cursor(*pygame.cursors.arrow)

		self.screen.blit(self.background, self.background.get_rect(), self.background.get_rect())

		for button in self.buttons.values():
			button.update()

		self.checkboxTest.update()

		pygame.display.update()

		return True, self