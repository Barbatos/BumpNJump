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

class Editor():
	def initObjects(self):
		for i in range(0, 16):
			objType = random.randint(1, 2)

			if objType == 1:
				self.objectList.append(Object("obj1" + str(i), i * 50, 550, "earth"))
			else:
				self.objectList.append(Object("obj1" + str(i), i * 50, 550, "ice"))

		for j in range(0, 30):
			objType = random.randint(1, 2)

			if objType == 1:
				self.objectList.append(Object("obj2" + str(j), random.randint(0, 15) * 50, random.randint(1, 10) * 50, "earth"))
			else:
				self.objectList.append(Object("obj2" + str(j), random.randint(0, 15) * 50, random.randint(1, 10) * 50, "ice"))

		for k in range(0, 5):
			randPos = random.randint(0, 46)
			self.objectList.append(Object("obj3" + str(k), self.objectList[randPos].getX() + 10, self.objectList[randPos].getY() - 26, "carrot"))

		for obj in self.objectList:
			self.objectSpritesList.add(pygame.sprite.RenderPlain(obj))

	def __init__(self):
		self.objectList = []
		self.objectSpritesList = pygame.sprite.Group()

		pygame.init()
		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		self.music = pygame.mixer.Sound("resources/sound/music.wav")
		self.music.play(-1)

		backgroundImage, backgroundRect = loadPNG("background.png")

		background = pygame.Surface(screen.get_size())
		background = backgroundImage

		clock = pygame.time.Clock()
		
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
							ob = Object("obj", x, y, "earth")
						else:
							ob = Object("obj", x, y, "boing")
						self.objectList.append(ob)
						self.objectSpritesList.add(pygame.sprite.RenderPlain(ob))

				elif event.type == MOUSEMOTION and key[K_LALT]:
					mse = pygame.mouse.get_pos()
					if any(obj.rect.collidepoint(mse) for obj in self.objectList):
						self.objectSpritesList.remove(obj)
						self.objectList.remove(obj)

			screen.blit(background, backgroundRect, backgroundRect)

			for obj in self.objectList:
				screen.blit(background, obj.rect, obj.rect)

			self.objectSpritesList.update()
			self.objectSpritesList.draw(screen)

			pygame.display.update()

			clock.tick(60)

if __name__ == '__main__': 
	Editor()
	