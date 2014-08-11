#!/usr/bin/python

import pygame
import PlayModeMenu
from Button import *
from Slider import *
from Game import *
from pygame.locals import *

class GameMenu():
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.sliders = {}

		self.sliders["red1"] = Slider(self.screen.get_width()/4 - 200/2, 100, 200, 200, 255)
		self.sliders["green1"] = Slider(self.screen.get_width()/4 - 200/2, 150, 200, 50, 255)
		self.sliders["blue1"] = Slider(self.screen.get_width()/4 - 200/2, 200, 200, 50, 255)

		self.sliders["red2"] = Slider(self.screen.get_width() - self.screen.get_width()/4 - 200/2, 100, 200, 50, 255)
		self.sliders["green2"] = Slider(self.screen.get_width() - self.screen.get_width()/4 - 200/2, 150, 200, 50, 255)
		self.sliders["blue2"] = Slider(self.screen.get_width() - self.screen.get_width()/4 - 200/2, 200, 200, 200, 255)

		self.rabbit1 = Animation("rabbit", 30)
		self.rabbit1.updateColor((self.sliders["red1"].getValue(), self.sliders["green1"].getValue(), self.sliders["blue1"].getValue()))
		self.rabbit1.setFrameRange(1, 8);
		self.rabbit1.flipAnim()
		self.rabbit1.setPos(self.screen.get_width()/4 - 21, 300)
		self.rabbit1Sprite = pygame.sprite.RenderPlain(self.rabbit1)

		self.rabbit2 = Animation("rabbit", 30)
		self.rabbit2.resetColor((self.sliders["red2"].getValue(), self.sliders["green2"].getValue(), self.sliders["blue2"].getValue()))
		self.rabbit2.setFrameRange(1, 8);
		self.rabbit2.setPos(self.screen.get_width() - self.screen.get_width()/4 - 21, 300)
		self.rabbit2Sprite = pygame.sprite.RenderPlain(self.rabbit2)

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

				for slider in self.sliders.values():
					if slider.onSlider(mse):
						slider.setValueByMousePos(mse[0])

						self.rabbit2.resetColor((self.sliders["red2"].getValue(), self.sliders["green2"].getValue(), self.sliders["blue2"].getValue()))
						self.rabbit2.setPos(self.screen.get_width() - self.screen.get_width()/4 - 21, 300)
						self.rabbit1.resetColor((self.sliders["red1"].getValue(), self.sliders["green1"].getValue(), self.sliders["blue1"].getValue()))
						self.rabbit1.setPos(self.screen.get_width()/4 - 21, 300)

				if self.buttons["play"].onButton(mse):
					return True, Game((self.sliders["red1"].getValue(), self.sliders["green1"].getValue(), self.sliders["blue1"].getValue()), (self.sliders["red2"].getValue(), self.sliders["green2"].getValue(), self.sliders["blue2"].getValue()))

				elif self.buttons["back"].onButton(mse):
					return True, PlayModeMenu.PlayModeMenu()

			if event.type == MOUSEMOTION:
				mse = pygame.mouse.get_pos()

				pygame.mouse.set_cursor(*pygame.cursors.arrow)

				for slider in self.sliders.values():
					if slider.onSlider(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)
						if mouse[0]:
							slider.setValueByMousePos(mse[0])

							self.rabbit2.resetColor((self.sliders["red2"].getValue(), self.sliders["green2"].getValue(), self.sliders["blue2"].getValue()))
							self.rabbit2.setPos(self.screen.get_width() - self.screen.get_width()/4 - 21, 300)
							self.rabbit1.resetColor((self.sliders["red1"].getValue(), self.sliders["green1"].getValue(), self.sliders["blue1"].getValue()))
							self.rabbit1.setPos(self.screen.get_width()/4 - 21, 300)

				for button in self.buttons.values():
					if button.onButton(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)

		self.screen.blit(self.background, self.background.get_rect(), self.background.get_rect())

		for slider in self.sliders.values():
			slider.update()

		self.rabbit1Sprite.update()
		self.rabbit1Sprite.draw(self.screen)

		self.rabbit2Sprite.update()
		self.rabbit2Sprite.draw(self.screen)

		self.rabbit1.update()
		self.rabbit2.update()

		for button in self.buttons.values():
			button.update()

		pygame.display.update()

		return True, self