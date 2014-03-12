#!/usr/bin/python

import pygame
from Button import *
from Slider import *
from Checkbox import *
from Game import *
from Editor import *
from Option import *
from pygame.locals import *

class Menu():
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.playButton = Button(self.screen.get_width()/2 - 200/2, 100, 200, 40, "PLAY")

		self.editorButton = Button(self.screen.get_width()/2 - 200/2, 200, 200, 40, "EDITOR")

		self.optionButton = Button(self.screen.get_width()/2 - 200/2, 300, 200, 40, "OPTION")

		self.quitButton = Button(self.screen.get_width()/2 - 200/2, 400, 200, 40, "QUIT")

		self.sliderTest = Slider(50, 50, 200, 100)

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
				if self.playButton.onButton(mse):
					return True, Game()

				elif self.editorButton.onButton(mse):
					return True, Editor()

				elif self.optionButton.onButton(mse):
					return True, Option()

				elif self.quitButton.onButton(mse):
					return False, self

				elif self.sliderTest.onSlider(mse):
					self.sliderTest.setValue(mse[0])

				elif self.checkboxTest.onCheckbox(mse):
					self.checkboxTest.changeState()

			if event.type == MOUSEMOTION:
				mse = pygame.mouse.get_pos()
				if self.sliderTest.onSlider(mse) and mouse[0]:
					self.sliderTest.setValue(mse[0])

		self.screen.blit(self.background, self.background.get_rect(), self.background.get_rect())

		self.playButton.update()
		self.editorButton.update()
		self.optionButton.update()
		self.quitButton.update()

		self.sliderTest.update()

		self.checkboxTest.update()

		pygame.display.update()

		return True, self