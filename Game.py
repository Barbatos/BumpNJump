#!/usr/bin/python

import sys
import os
import math
import random
import pygame
import MainMenu
from pygame.locals import *
from Rabbit import *
from Butterfly import *
from Animation import *
from Object import *
from Resources import *
from PauseGameMenu import *
from Map import *
from GameToolbar import *

class Game():
	def __init__(self, color1, color2):
		self.butterflies = []

		self.screen = pygame.display.get_surface()

		self.backgroundImage, self.backgroundRect = loadPNG("background.png")

		self.active = True

		self.level = Map()

		self.toolbar = GameToolbar()

		self.regis = Rabbit(1, "regis" ,color1 , self.level.objectList, self.level.objectSpritesList)

		self.john = Rabbit(2, "john" ,color2 , self.level.objectList, self.level.objectSpritesList)

		self.john.appendRabbit(self.regis)
		self.regis.appendRabbit(self.john)

		self.pauseMenu = PauseGameMenu()

		self.deltaCarrot = 0
		self.timeCarrot = random.randint(1, 4)

		for l in range(0, 4):
			while True:
				randPos = random.randint(0, 46)
				if not self.level.isInBlock(self.level.objectList[randPos].getX() + 10, self.level.objectList[randPos].getY() - 26):
					break

			butterfly = Butterfly(self.level.objectList[randPos].getX() + 10, self.level.objectList[randPos].getY() - 26, (255, 10, 100), self.level.objectList, self.level.objectSpritesList)
			self.butterflies.append(butterfly)

		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()

		if self.active:
			pygame.mouse.set_visible(0)

			for event in pygame.event.get():
				if event.type == QUIT or (key[K_F4] and key[K_LALT]):
					return False, self

				elif event.type == MOUSEMOTION and (key[K_LSHIFT] or key[K_LCTRL]):
					mse = pygame.mouse.get_pos()
					if not any(obj.rect.collidepoint(mse) for obj in self.level.objectList):
						x = (int(mse[0]) / 50)*50
						y = (int(mse[1]) / 50)*50
						if key[K_LSHIFT]:
							self.level.addObject(x, y, "earth")
						else:
							self.level.addObject(x, y, "boing")

				elif event.type == MOUSEMOTION and key[K_LALT]:
					mse = pygame.mouse.get_pos()
					self.level.removeObjectFromPos(mse)

				elif event.type == KEYDOWN:
					if not self.john.isTouched():
						if event.key == K_UP:
							self.john.jump()
						if event.key == K_LEFT:
							self.john.moveLeftStart()
						if event.key == K_RIGHT:
							self.john.moveRightStart()
						if event.key == K_KP0:
							self.john.throwCarrot()

					if not self.regis.isTouched():
						if event.key == K_w:
							self.regis.jump()
						if event.key == K_a:
							self.regis.moveLeftStart()
						if event.key == K_d:
							self.regis.moveRightStart()
						if event.key == K_e:
							self.regis.throwCarrot()

					if event.key == K_c:
						self.level.addCarrot()

					if event.key == K_ESCAPE:
						self.active = False
						self.john.moveLeftStop()
						self.john.moveRightStop()
						self.regis.moveLeftStop()
						self.regis.moveRightStop()

				elif event.type == KEYUP:
					if event.key == K_LEFT:
						self.john.moveLeftStop()
					if event.key == K_RIGHT:
						self.john.moveRightStop()
					if event.key == K_a:
						self.regis.moveLeftStop()
					if event.key == K_d:
						self.regis.moveRightStop()

			self.screen.blit(self.backgroundImage, self.backgroundRect, self.backgroundRect)

			#LEVEL UPDATE
			self.level.update()

			#RABBITS UPDATE
			self.john.update()
			self.regis.update()

			#TOOLBAR UPDATE
			self.toolbar.update(self.john, self.regis)

			#BUTTERFLIES UPDATE
			for b in self.butterflies:
				b.update()

			#NEW CARROTS
			if(self.deltaCarrot == self.timeCarrot * 3600):
				self.level.addCarrot()
				self.deltaCarrot = 0
				self.timeCarrot = random.randint(1, 4)
			else:
				self.deltaCarrot += 1

		else:
			pygame.mouse.set_visible(1)

			for event in pygame.event.get():
				if event.type == QUIT or (key[K_F4] and key[K_LALT]):
					return False, self

				elif event.type == MOUSEBUTTONDOWN:
					mse = pygame.mouse.get_pos()

					if self.pauseMenu.buttons["resume"].onButton(mse):
						self.active = True

					elif self.pauseMenu.buttons["mainMenu"].onButton(mse):
						return True, MainMenu.MainMenu()


				elif event.type == MOUSEMOTION:
					mse = pygame.mouse.get_pos()

					pygame.mouse.set_cursor(*pygame.cursors.arrow)

					for button in self.pauseMenu.buttons.values():
						if button.onButton(mse):
							pygame.mouse.set_cursor(*pygame.cursors.tri_left)

				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.active = True

			self.pauseMenu.update()

		pygame.display.update()

		return True, self