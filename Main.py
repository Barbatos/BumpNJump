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

class BumpNJump():

	def initObjects(self):
		self.objectList.append(Object("obj1", "earth.png", 250, 550))

		for obj in self.objectList:
			self.objectSpritesList.add(pygame.sprite.RenderPlain(obj))

	def __init__(self):
		self.objectList = []
		self.objectSpritesList = pygame.sprite.Group()

		pygame.init()
		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		backgroundImage, backgroundRect = loadPNG("background.png")

		background = pygame.Surface(screen.get_size())
		background = background.convert()

		john = Rabbit(1, "john", self.objectList, self.objectSpritesList)
		animJohnSprite = pygame.sprite.RenderPlain(john.getAnim())
		john.getAnim().stopAnim()

		regis = Rabbit(2, "regis", self.objectList, self.objectSpritesList)
		animRegisSprite = pygame.sprite.RenderPlain(regis.getAnim())
		regis.getAnim().stopAnim()

		self.initObjects()

		clock = pygame.time.Clock()

		screen.blit(backgroundImage, (0, 0))
		pygame.display.flip()

		while 1:
			key = pygame.key.get_pressed()
			for event in pygame.event.get():
				if event.type == QUIT:
					return

				elif event.type == MOUSEMOTION and (key[K_LSHIFT] or key[K_LCTRL]):
					mse = pygame.mouse.get_pos()
					if not any(obj.rect.collidepoint(mse) for obj in self.objectList):
						x = (int(mse[0]) / 50)*50
						y = (int(mse[1]) / 50)*50
						if key[K_LSHIFT]:
							ob = Object("obj", "earth.png", x, y)
						else:
							ob = Object("obj", "ice.png", x, y)
						self.objectList.append(ob)
						self.objectSpritesList.add(pygame.sprite.RenderPlain(ob))

				elif event.type == MOUSEMOTION and key[K_LALT]:
					mse = pygame.mouse.get_pos()
					if any(obj.rect.collidepoint(mse) for obj in self.objectList):
						self.objectSpritesList.remove(obj)
						self.objectList.remove(obj)

				elif event.type == KEYDOWN:
					if event.key == K_UP:
						john.jump()
					if event.key == K_LEFT:
						john.moveLeftStart()
					if event.key == K_RIGHT:
						john.moveRightStart()
					if event.key == K_w:
						regis.jump()
					if event.key == K_a:
						regis.moveLeftStart()
					if event.key == K_d:
						regis.moveRightStart()

				elif event.type == KEYUP:
					if event.key == K_LEFT:
						john.moveLeftStop()
					if event.key == K_RIGHT:
						john.moveRightStop()
					if event.key == K_a:
						regis.moveLeftStop()
					if event.key == K_d:
						regis.moveRightStop()

			screen.blit(backgroundImage, backgroundRect, backgroundRect)
			screen.blit(backgroundImage, john.rect, john.rect)
			screen.blit(backgroundImage, john.getAnim().getRect(), john.getAnim().getRect())

			screen.blit(backgroundImage, regis.rect, regis.rect)
			screen.blit(backgroundImage, regis.getAnim().getRect(), regis.getAnim().getRect())

			for obj in self.objectList:
				screen.blit(backgroundImage, obj.rect, obj.rect)

			john.update()
			regis.update()

			animJohnSprite.update()
			animJohnSprite.draw(screen)

			animRegisSprite.update()
			animRegisSprite.draw(screen)

			john.getAnim().update()
			regis.getAnim().update()

			self.objectSpritesList.update()
			self.objectSpritesList.draw(screen)

			pygame.display.update()

			clock.tick(60)

if __name__ == '__main__': 
	BumpNJump()
	