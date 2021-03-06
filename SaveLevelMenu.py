#!/usr/bin/python

import pygame
import glob
import Editor
import Resources
from Button import *
from pygame.locals import *

class SaveLevelMenu():
	pygame.mixer.pre_init(44100, -16, 2, 1024)
	pygame.mixer.init()

	def __init__(self, level):
		self.screen = pygame.display.get_surface()

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((50, 50, 50))

		self.buttonSound = pygame.mixer.Sound("resources/sound/button.wav")
		self.buttonSound.set_volume(float(Resources.getOptionValue("sound"))/100)

		self.level = level

		self.buttons = {}

		pos = 25

		for f in glob.glob("save/maps/*.mabbit"):
			name = f.split("\\")[-1].split(".")[0]

			if(name != "last"):
				self.buttons[name] = Button(self.screen.get_width()/2 - 200/2, pos, 200, 40, name.upper())

				pos +=100

		self.buttons["new"] = Button(self.screen.get_width()/2 - 200/2, pos, 200, 40, "NEW")
		self.buttons["back"] = Button(self.screen.get_width()/2 - 200/2, pos + 100, 200, 40, "BACK")

		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()
		
		for event in pygame.event.get():
			if event.type == QUIT or (key[K_F4] and key[K_LALT]):
				return False, self

			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 5:
					if self.buttons[self.buttons.keys()[0]].getY() > self.screen.get_height() - 65:
						for button in self.buttons.values():
							button.setY(button.getY() - 25)
				if event.button == 4:
					if self.buttons[self.buttons.keys()[1]].getY() <= 25:
						for button in self.buttons.values():
							button.setY(button.getY() + 25)

				for name, button in self.buttons.items():
					mse = pygame.mouse.get_pos()

					if event.button == 1:
						if button.onButton(mse):
							self.buttonSound.play()
							if name == "new":
								self.level.save("level" + str(len(self.buttons)))
								return True, Editor.Editor("level" + str(len(self.buttons)))

							elif name == "back":
								return True, Editor.Editor("last")

							else:
								self.level.save(name)
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