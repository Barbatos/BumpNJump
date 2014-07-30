#!/usr/bin/python

import pygame
import Resources
from Animation import *
from pygame.locals import *

class Carrot():
	def __init__(self, direction, posX, posY):
		self.carrotAnim = Animation("carrot", 50)
		self.carrotAnim.setFrameRange(1, 25);
		self.carrotAnim.playAnim()

		self.screen = pygame.display.get_surface()
		self.area = self.screen.get_rect()
		self.area.h += 500
		self.area.y -= 550

		self.rect = pygame.Rect(posX, posY, 50, 50)
		self.carrotAnim.setRect(self.rect)

		self.moveX = posX

		self.direction = direction

	def update(self):
		if(self.direction == "right"):
			self.moveX += 6
		else:
			self.moveX -= 6

		self.rect.x = self.moveX

		self.carrotAnim.setRect(self.rect)

	def getAnim(self):
		return self.carrotAnim