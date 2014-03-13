#!/usr/bin/python

import pygame
from Button import *
from Slider import *
from Checkbox import *
import MainMenu
from pygame.locals import *

class OptionMenu():
	def __init__(self):
		self.screen = pygame.display.get_surface()

		if pygame.font:
			self.font = pygame.font.Font(None, 22)

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.sliders = {}

		self.sliders["music"] = Slider(self.screen.get_width()/2 - 200/2, 100, 200, 100)
		self.sliders["sound"] = Slider(self.screen.get_width()/2 - 200/2, 200, 200, 100)

		self.returnButton = Button(self.screen.get_width()/2 - 200/2, 400, 200, 40, "RETURN")

		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT or (key[K_F4] and key[K_LALT]):
				return False, self

			elif event.type == MOUSEBUTTONDOWN:
				mse = pygame.mouse.get_pos()

				for slider in self.sliders.values():
					if slider.onSlider(mse):
						slider.setValue(mse[0])

				if self.returnButton.onButton(mse):
					return True, MainMenu.MainMenu()

			elif event.type == MOUSEMOTION:
				mse = pygame.mouse.get_pos()

				for slider in self.sliders.values():
					if slider.onSlider(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)
						if mouse[0]:
							slider.setValue(mse[0])

				if self.returnButton.onButton(mse):
					pygame.mouse.set_cursor(*pygame.cursors.tri_left)

				else:
					pygame.mouse.set_cursor(*pygame.cursors.arrow)

		self.screen.blit(self.background, self.background.get_rect(), self.background.get_rect())

		if pygame.font:
			self.textDisp = self.font.render("Music volume", 1, (100, 100, 100))
			self.textRect = self.textDisp.get_rect(centerx = self.screen.get_width()/2, y = self.sliders["music"].getY() - 25)
			self.screen.blit(self.textDisp, self.textRect)

			self.textDisp = self.font.render("Sound volume", 1, (100, 100, 100))
			self.textRect = self.textDisp.get_rect(centerx = self.screen.get_width()/2, y = self.sliders["sound"].getY() - 25)
			self.screen.blit(self.textDisp, self.textRect)

		for slider in self.sliders.values():
			slider.update()

		self.returnButton.update()

		pygame.display.update()

		return True, self