#!/usr/bin/python

import sys
import os
import math
import random
import pygame
from pygame.locals import *
from Rabbit import *
from Animation import *
from Object import *
from Resources import *
from Map import *

class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		self.backgroundImage, self.backgroundRect = loadPNG("background.png")

		self.level = Map()

		self.john = Rabbit(1, "john" ,(200, 50, 50) , self.level.objectList, self.level.objectSpritesList)
		self.animJohnSprite = pygame.sprite.RenderPlain(self.john.getAnim())
		self.john.getAnim().stopAnim()

		self.regis = Rabbit(2, "regis" ,(50, 50, 200) , self.level.objectList, self.level.objectSpritesList)
		self.animRegisSprite = pygame.sprite.RenderPlain(self.regis.getAnim())
		self.regis.getAnim().stopAnim()

		self.john.appendRabbit(self.regis)
		self.regis.appendRabbit(self.john)
		
		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()
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

		self.john.explosion.update()
		self.regis.explosion.update()

		self.animJohnSprite.update()
		self.animJohnSprite.draw(self.screen)

		self.animRegisSprite.update()
		self.animRegisSprite.draw(self.screen)

		self.john.getAnim().update()
		self.regis.getAnim().update()

		self.level.update(self.screen)

		if pygame.font:
			font = pygame.font.Font(None, 36)
			text = font.render(str(self.john.getPoints()) + " : " + str(self.regis.getPoints()), 1, (10, 10, 10))
			textpos = text.get_rect(centerx = self.screen.get_width()/2)
			self.screen.blit(text, textpos)

		pygame.display.update()

		return True, self