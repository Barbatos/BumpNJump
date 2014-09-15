#!/usr/bin/python

import pygame
import Resources
from Button import *
from Slider import *
from Checkbox import *
from GameMenu import *
from Editor import *
from OptionMenu import *
from PlayModeMenu import *
from pygame.locals import *

class MainMenu():
	pygame.mixer.pre_init(44100, -16, 2, 1024)
	pygame.mixer.init()

	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.buttonSound = pygame.mixer.Sound("resources/sound/button.wav")
		self.buttonSound.set_volume(float(Resources.getOptionValue("sound"))/100)

		self.buttons = {}

		menuPos = 175

		self.buttons["play"] = Button(self.screen.get_width()/2 - 200/2, menuPos, 200, 40, "PLAY")
		self.buttons["editor"] = Button(self.screen.get_width()/2 - 200/2, menuPos + 100, 200, 40, "EDITOR")
		self.buttons["option"] = Button(self.screen.get_width()/2 - 200/2, menuPos + 200, 200, 40, "OPTION")
		self.buttons["quit"] = Button(self.screen.get_width()/2 - 200/2, menuPos + 300, 200, 40, "QUIT")

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
					self.buttonSound.play()
					return True, PlayModeMenu()

				elif self.buttons["editor"].onButton(mse):
					self.buttonSound.play()
					return True, Editor()

				elif self.buttons["option"].onButton(mse):
					self.buttonSound.play()
					return True, OptionMenu()

				elif self.buttons["quit"].onButton(mse):
					self.buttonSound.play()
					return False, self

			elif event.type == MOUSEMOTION:
				mse = pygame.mouse.get_pos()

				pygame.mouse.set_cursor(*pygame.cursors.arrow)

				for button in self.buttons.values():
					if button.onButton(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)

		self.screen.blit(self.background, self.background.get_rect(), self.background.get_rect())

		if pygame.font:
			font = pygame.font.Font(None, 65)
			text = font.render("BUMP'N'JUMP", 1, (220, 220, 220))
			textpos = text.get_rect(centerx = self.screen.get_width()/2, y = 70)
			self.screen.blit(text, textpos)

		for button in self.buttons.values():
			button.update()

		pygame.display.update()

		return True, self
