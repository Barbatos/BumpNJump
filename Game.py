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

class Game():
	def __init__(self, color1, color2):
		self.butterflies = []
		self.butterfliesSpritesList = pygame.sprite.Group()

		self.screen = pygame.display.get_surface()

		self.backgroundImage, self.backgroundRect = loadPNG("background.png")

		self.active = True

		self.level = Map()

		self.john = Rabbit(1, "john" ,color1 , self.level.objectList, self.level.objectSpritesList)
		self.animJohnSprite = pygame.sprite.RenderPlain(self.john.getAnim())
		self.john.getAnim().stopAnim()

		self.regis = Rabbit(2, "regis" ,color2 , self.level.objectList, self.level.objectSpritesList)
		self.animRegisSprite = pygame.sprite.RenderPlain(self.regis.getAnim())
		self.regis.getAnim().stopAnim()

		self.john.appendRabbit(self.regis)
		self.regis.appendRabbit(self.john)

		self.pauseMenu = PauseGameMenu()
		
		#self.butterflyTest = Butterfly((255, 10, 100), self.level.objectList, self.level.objectSpritesList)
		#self.butterflyTestSprite = pygame.sprite.RenderPlain(self.butterflyTest.getAnim())

		for l in range(0, 10):
			while True:
				randPos = random.randint(0, 46)
				if not self.level.isInBlock(self.level.objectList[randPos].getX() + 10, self.level.objectList[randPos].getY() - 26):
					break

			butterfly = Butterfly(self.level.objectList[randPos].getX() + 10, self.level.objectList[randPos].getY() - 26, (255, 10, 100), self.level.objectList, self.level.objectSpritesList)
			self.butterflies.append(butterfly)
			self.butterfliesSpritesList.add(pygame.sprite.RenderPlain(butterfly.getAnim()))

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
					if event.key == K_UP:
						self.john.jump()
					if event.key == K_LEFT:
						self.john.moveLeftStart()
					if event.key == K_RIGHT:
						self.john.moveRightStart()
					if event.key == K_w:
						self.regis.jump()
					if event.key == K_a:
						self.regis.moveLeftStart()
					if event.key == K_d:
						self.regis.moveRightStart()
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

			self.john.update()
			self.regis.update()

			#self.butterflyTest.update()
			#self.butterflyTestSprite.draw(self.screen)

			for b in self.butterflies:
				b.update()

			self.butterfliesSpritesList.draw(self.screen)

			self.animJohnSprite.update()
			self.animJohnSprite.draw(self.screen)

			self.animRegisSprite.update()
			self.animRegisSprite.draw(self.screen)

			self.john.getAnim().update()
			self.regis.getAnim().update()

			self.level.update(self.screen)

			self.john.explosion.update()
			self.regis.explosion.update()

			if pygame.font:
				font = pygame.font.Font(None, 36)
				text = font.render(str(self.john.getPoints()) + " : " + str(self.regis.getPoints()), 1, (10, 10, 10))
				textpos = text.get_rect(centerx = self.screen.get_width()/2)
				self.screen.blit(text, textpos)

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