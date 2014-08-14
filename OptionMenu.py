#!/usr/bin/python

import pygame
import MainMenu
from Button import *
from Slider import *
from Checkbox import *
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

		self.currentSlider = None

		self.checkboxes = {}

		self.checkboxes["blood"] = Checkbox(self.screen.get_width()/2 - 50, 300, "Blood", True)
		self.checkboxes['fullscreen'] = Checkbox(self.screen.get_width()/2 - 50, 350, "Fullscreen", False)

		self.loadOptions()

		self.buttons = {}

		self.buttons["save"] = Button(self.screen.get_width() - self.screen.get_width()/4 - 200/2, 450, 200, 40, "SAVE")
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

				if self.buttons["save"].onButton(mse):
					self.saveOptions()
					return True, MainMenu.MainMenu()

				elif self.buttons["back"].onButton(mse):
					return True, MainMenu.MainMenu()

				elif self.checkboxes["blood"].onCheckbox(mse):
					self.checkboxes["blood"].changeState()

				elif self.checkboxes["fullscreen"].onCheckbox(mse):
					self.checkboxes["fullscreen"].changeState()

			elif event.type == MOUSEMOTION:
				mse = pygame.mouse.get_pos()

				pygame.mouse.set_cursor(*pygame.cursors.arrow)

				for slider in self.sliders.values():
					if slider.onSlider(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)

				if self.currentSlider != None and mouse[0]:
					pygame.mouse.set_cursor(*pygame.cursors.tri_left)
					self.sliders[self.currentSlider].setValueByMousePos(mse[0])

				for button in self.buttons.values():
					if button.onButton(mse):
						pygame.mouse.set_cursor(*pygame.cursors.tri_left)

			elif event.type == MOUSEBUTTONUP:
				if self.currentSlider != None:
					self.currentSlider = None

		pygame.mixer.music.set_volume(float(self.sliders["music"].getValue())/100)

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

		for button in self.buttons.values():
			button.update()

		for checkbox in self.checkboxes.values():
			checkbox.update()

		pygame.display.update()

		return True, self

	def saveOptions(self):
		with open("save/options.mabbit", "w") as f:
			for key, sli in self.sliders.items():
				f.write(key + ":" + str(sli.getValue()) + "\n")

			for key, check in self.checkboxes.items():
				if check.isChecked():
					f.write(key + ":1\n")
				else:
					f.write(key + ":0\n")

	def loadOptions(self):
		with open("save/options.mabbit", "r") as f:
			for line in f:
				line = line.strip("\n")

				if line.split(":")[0] in self.sliders:
					self.sliders[line.split(":")[0]].setValueByNumber(int(line.split(":")[1]))
				else:
					if int(line.split(":")[1]) == 0:
						self.checkboxes[line.split(":")[0]].uncheck()
					else:
						self.checkboxes[line.split(":")[0]].check()