#!/usr/bin/python

import pygame
import Resources
import MultiMenu
import MultiServerGame
import MultiClientGame
from Button import *
from Slider import *
from Game import *
from pygame.locals import *

class MultiGameRabbitMenu():
	pygame.mixer.pre_init(44100, -16, 2, 1024)
	pygame.mixer.init()

	def __init__(self, server = False):
		self.screen = pygame.display.get_surface()

		self.server = server

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.buttonSound = pygame.mixer.Sound("resources/sound/button.wav")
		self.buttonSound.set_volume(float(Resources.getOptionValue("sound"))/100)

		self.sliders = {}

		self.sliders["red"] = Slider(self.screen.get_width()/2 - 200/2, 100, 200, 200, 255)
		self.sliders["green"] = Slider(self.screen.get_width()/2 - 200/2, 150, 200, 50, 255)
		self.sliders["blue"] = Slider(self.screen.get_width()/2 - 200/2, 200, 200, 50, 255)

		self.currentSlider = None

		self.rabbit1 = Animation("rabbit", 30)
		self.rabbit1.updateColor((self.sliders["red"].getValue(), self.sliders["green"].getValue(), self.sliders["blue"].getValue()))
		self.rabbit1.setFrameRange(1, 8);
		self.rabbit1.flipAnim()
		self.rabbit1.setPos(self.screen.get_width()/2 - 21, 300)
		self.rabbit1Sprite = pygame.sprite.RenderPlain(self.rabbit1)

		self.buttons = {}

		self.buttons["play"] = Button(self.screen.get_width() - self.screen.get_width()/4 - 200/2, 450, 200, 40, "PLAY")
		self.buttons["back"] = Button(self.screen.get_width()/4 - 200/2, 450, 200, 40, "BACK")

		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()

		for event in pygame.event.get():
			if event.type == QUIT or (key[K_F4] and key[K_LALT]):
				return False, self

			elif event.type == MOUSEBUTTONDOWN:
				mse = pygame.mouse.get_pos()

				for sliderKey, slider in self.sliders.items():
					if slider.onSlider(mse):
						slider.setValueByMousePos(mse[0])
						self.currentSlider = sliderKey
						self.rabbit1.resetColor((self.sliders["red"].getValue(), self.sliders["green"].getValue(), self.sliders["blue"].getValue()))
						self.rabbit1.setPos(self.screen.get_width()/2 - 21, 300)

				if self.buttons["play"].onButton(mse):
					self.buttonSound.play()
					if not self.server:
						return True, MultiClientGame.MultiClientGame((self.sliders["red"].getValue(), self.sliders["green"].getValue(), self.sliders["blue"].getValue()))
					else:
						return True, MultiServerGame.MultiServerGame(self.server, (self.sliders["red"].getValue(), self.sliders["green"].getValue(), self.sliders["blue"].getValue()))

				elif self.buttons["back"].onButton(mse):
					self.buttonSound.play()
					return True, MultiMenu.MultiMenu()

			elif event.type == MOUSEMOTION:
				mse = pygame.mouse.get_pos()

				pygame.mouse.set_cursor(*pygame.cursors.arrow)

				for slider in self.sliders.values():
					if slider.onSlider(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)

				if self.currentSlider != None and mouse[0]:
					pygame.mouse.set_cursor(*pygame.cursors.tri_left)
					self.sliders[self.currentSlider].setValueByMousePos(mse[0])

					self.rabbit1.resetColor((self.sliders["red"].getValue(), self.sliders["green"].getValue(), self.sliders["blue"].getValue()))
					self.rabbit1.setPos(self.screen.get_width()/2 - 21, 300)

				for button in self.buttons.values():
					if button.onButton(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)

			elif event.type == MOUSEBUTTONUP:
				if self.currentSlider != None:
					self.currentSlider = None

		self.screen.blit(self.background, self.background.get_rect(), self.background.get_rect())

		for slider in self.sliders.values():
			slider.update()

		self.rabbit1.update()
		self.rabbit1Sprite.update()
		self.rabbit1Sprite.draw(self.screen)

		for button in self.buttons.values():
			button.update()

		pygame.display.update()

		return True, self