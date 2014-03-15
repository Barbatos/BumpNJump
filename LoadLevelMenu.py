#!/usr/bin/python

import pygame
import glob
import Editor
from Button import *
from pygame.locals import *

class LoadLevelMenu():
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.buttons = {}

		pos = 100

		for f in glob.glob("save/maps/*.mabbit"):
			name = f.split("\\")[-1].split(".")[0]

			self.buttons[name] = Button(self.screen.get_width()/2 - 200/2, pos, 200, 40, name.upper())

			pos +=100

		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()
		
		for event in pygame.event.get():
			if event.type == QUIT or (key[K_F4] and key[K_LALT]):
				return False, self

			elif event.type == MOUSEBUTTONDOWN:
				for name, button in self.buttons.items():
					mse = pygame.mouse.get_pos()

					if button.onButton(mse):
						return True, Editor.Editor(name)

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