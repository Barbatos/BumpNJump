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

class BumpNJump():

	def initObjects(self):
		self.objectList.append(Object(1, "obj1", "earth.png", 100, 530))
		self.objectList.append(Object(2, "obj2", "earth.png", 133, 497))

		for obj in self.objectList:
			self.objectSpritesList.append(pygame.sprite.RenderPlain(obj))

	def __init__(self):
		self.objectList = []
		self.objectSpritesList = []

		pygame.init()
		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		background = pygame.Surface(screen.get_size())
		background = background.convert()
		background.fill((100, 150, 100))

		rabbit = Rabbit(1, "john")
		animRabbitSprite = pygame.sprite.RenderPlain(rabbit.getAnim())
		rabbit.getAnim().stopAnim()

		self.initObjects()

		clock = pygame.time.Clock()

		screen.blit(background, (0, 0))
		pygame.display.flip()

		while 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					return

				elif event.type == KEYDOWN:
					if event.key == K_UP or event.key == K_SPACE:
						rabbit.jump()
					if event.key == K_LEFT:
						rabbit.moveLeftStart()
					if event.key == K_RIGHT:
						rabbit.moveRightStart()
					if event.key == K_o:
						testAnim.rewind()
					if event.key == K_i:
						testAnim.flipAnim()
					if event.key == K_p:
						if testAnim.isRunning():
							testAnim.stopAnim()
						else:
							testAnim.playAnim()

				elif event.type == KEYUP:
					if event.key == K_LEFT:
						rabbit.moveLeftStop()
					if event.key == K_RIGHT:
						rabbit.moveRightStop()

			screen.blit(background, rabbit.rect, rabbit.rect)
			screen.blit(background, rabbit.getAnim().getRect(), rabbit.getAnim().getRect())

			for obj in self.objectList:
				screen.blit(background, obj.rect, obj.rect)

			rabbit.update()

			animRabbitSprite.update()
			animRabbitSprite.draw(screen)

			rabbit.getAnim().update()

			for s in self.objectSpritesList:
				s.update()
				s.draw(screen)

			pygame.display.flip()

			clock.tick(60)

if __name__ == '__main__': 
	BumpNJump()
	