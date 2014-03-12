#!/usr/bin/python

import pygame
from Button import *
from Slider import *
from Checkbox import *
import Menu
from pygame.locals import *

class Option():
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		if pygame.font:
			self.font = pygame.font.Font(None, 22)

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.musicSlider = Slider(self.screen.get_width()/2 - 200/2, 100, 200, 100)
		self.soundSlider = Slider(self.screen.get_width()/2 - 200/2, 200, 200, 100)

		self.returnButton = Button(self.screen.get_width()/2 - 200/2, 400, 200, 40, "RETURN")

		self.clock = pygame.time.Clock()

		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT or (key[K_F4] and key[K_LALT]):
				return False, self

			elif event.type == MOUSEBUTTONDOWN:
				mse = pygame.mouse.get_pos()
				if self.musicSlider.onSlider(mse):
					self.musicSlider.setValue(mse[0])

				elif self.soundSlider.onSlider(mse):
					self.soundSlider.setValue(mse[0])

				elif self.returnButton.onButton(mse):
					return True, Menu.Menu()

			elif event.type == MOUSEMOTION:
				mse = pygame.mouse.get_pos()
				if self.musicSlider.onSlider(mse) and mouse[0]:
					self.musicSlider.setValue(mse[0])

				elif self.soundSlider.onSlider(mse) and mouse[0]:
					self.soundSlider.setValue(mse[0])

		self.screen.blit(self.background, self.background.get_rect(), self.background.get_rect())

		if pygame.font:
			self.textDisp = self.font.render("Music volume", 1, (100, 100, 100))

		self.textRect = self.textDisp.get_rect(centerx = self.screen.get_width()/2, y = self.musicSlider.getY() - 25)
		self.screen.blit(self.textDisp, self.textRect)

		self.musicSlider.update()

		if pygame.font:
			self.textDisp = self.font.render("Sound volume", 1, (100, 100, 100))

		self.textRect = self.textDisp.get_rect(centerx = self.screen.get_width()/2, y = self.soundSlider.getY() - 25)
		self.screen.blit(self.textDisp, self.textRect)

		self.soundSlider.update()

		self.returnButton.update()

		pygame.display.update()

		self.clock.tick(60)

		return True, self