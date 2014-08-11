#!/usr/bin/python

import pygame
import Resources
from Animation import *
from pygame.locals import *

class Carrot():
	def __init__(self, direction, posX, posY, objectList = []):
		self.objectList = objectList

		self.carrotAnim = Animation("carrot", 12)
		self.carrotAnim.setFrameRange(1, 12);
		self.carrotAnim.playAnim()

		self.screen = pygame.display.get_surface()
		self.area = self.screen.get_rect()
		self.area.h += 500
		self.area.y -= 550

		self.rect = pygame.Rect(posX, posY, 50, 50)
		self.carrotAnim.setRect(self.rect)

		self.moveX = posX

		self.direction = direction

		self.end = False

	def update(self):
		if self.direction == "right":
			self.moveX += 6
		else:
			self.moveX -= 6

		self.rect.x = self.moveX

		self.carrotAnim.setRect(self.rect)

		self.checkForCollision()

		return self.end

	def collisionDetection(self, obj):
		if obj.isInBlock(self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2):
			return True
		else:
			return False

	def checkForCollision(self):
		for obj in self.objectList:
			if not self.end:
				self.end = self.collisionDetection(obj)

	def getAnim(self):
		return self.carrotAnim