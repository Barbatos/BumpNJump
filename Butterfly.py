#!/usr/bin/python

import pygame
import Resources
import random
from Animation import *
from pygame.locals import *
from Explosion import *
from random import randint

class Butterfly():

	def __init__(self, color = (255, 255, 255), objectList = [], spriteList = []):
		self.objectList = objectList
		self.spriteList = spriteList

		self.rect = pygame.Rect(randint(0, 800), randint(0, 600), 15, 15)
		self.screen = pygame.display.get_surface()

		self.butterflyAnim = Animation("butterfly", 2)
		self.butterflyAnim.updateColor(color)
		self.butterflyAnim.setFrameRange(1, 8);

		self.area = self.screen.get_rect()
		self.color = color

		self.floorLevel = self.screen.get_height() - self.rect.h

		self.movingLeft = False
		self.movingRight = False
		self.movingUp = False
		self.movingDown = False

		self.collide = False

		self.movePos = [0,0.01]

		self.butterflyAnim.playAnim()

	def update(self):
		self.movePos[0] = randint(-8, 8)
		self.movePos[1] = randint(-8, 8)

		self.checkForCollision()

		newpos = self.rect.move(self.movePos)
		if self.area.contains(newpos) and not self.collide:
			self.rect = newpos

		self.butterflyAnim.getRect().x = self.rect.x
		self.butterflyAnim.getRect().y = self.rect.y

		pygame.event.pump()

	def collisionDetection(self, obj, rabbit = False):
		if (self.rect.x < (obj.rect.x + obj.rect.w)) and (obj.rect.x < self.rect.x):
			if (self.rect.y + self.rect.h) > (obj.rect.y + 1):
				if self.rect.y < (obj.rect.y + obj.rect.h):
					self.movePos[0] = 5

		if (obj.rect.x < (self.rect.x + self.rect.w)) and (obj.rect.x > self.rect.x):
			if (self.rect.y + self.rect.h) > (obj.rect.y + 1):
				if self.rect.y < (obj.rect.y + obj.rect.h):
					self.movePos[0] = -5

		if (self.rect.y <= (obj.rect.y + obj.rect.h)) and (obj.rect.y <= self.rect.y):
			if (self.rect.x + self.rect.w) > (obj.rect.x + 3):
				if self.rect.x < (obj.rect.x + obj.rect.w - 5):
					self.movePos[1] = 5

		if ((self.rect.y + self.rect.h) >= obj.rect.y) and (self.rect.y <= obj.rect.y):
			if (self.rect.x + self.rect.w) > (obj.rect.x + 3):
				if self.rect.x < (obj.rect.x + obj.rect.w - 5):
					if self.movePos[1] >= 0:
						self.rect.y = obj.rect.y - self.rect.h
						self.movePos[1] = -5

	def checkForCollision(self):
		#if not self.movingLeft and not self.movingRight and self.movePos[1] == 0 and self.velocity == 0:
		#	return

		for obj in self.objectList:
			if obj.getType() is not "carrot":
				self.collisionDetection(obj, False)

		#for rabbit in self.rabbitList:
		#	self.collisionDetection(rabbit, True)
 	
 	def moveLeftStart(self):
 		self.movingLeft = True
 		self.movingRight = False

 	def moveLeftStop(self):
 		self.movingLeft = False
 		self.movePos[0] = 0

 	def moveRightStart(self):
 		self.movingRight = True
 		self.movingLeft = False
	
	def moveRightStop(self):
		self.movingRight = False
		self.movePos[0] = 0

	def getAnim(self):
		return self.butterflyAnim

