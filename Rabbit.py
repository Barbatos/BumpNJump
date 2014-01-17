#!/usr/bin/python

import pygame
import math
import Resources
from pygame.locals import *

class Rabbit(pygame.sprite.Sprite):
	def __init__(self, id = -1, name = ""):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = Resources.loadPNG("test.png", False)
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()

		self.floorLevel = screen.get_height() - self.rect.h

		self.movingLeft = False
		self.movingRight = False
		self.isJumping = False

		self.speed = 10
		self.id = id
		self.name = name

		self.yVelocity = 0
		self.xVelocity = 7
		self.gravity = 1.2
		self.jumpVelocity = -15

		self.movePos = [0,0]
		self.rect.topleft = (100, self.floorLevel)

	def __repr__(self):
		print("Rabbit " + self.id + ": " + self.name)

	def update(self):
		if self.isJumping == True:

			self.yVelocity += self.gravity
			self.rect.y += self.yVelocity

			if self.rect.y > self.floorLevel:
				self.rect.y = self.floorLevel
				self.isJumping = False 

		if self.movingLeft == True:
			self.movePos[0] = -self.xVelocity

		if self.movingRight == True:
			self.movePos[0] = self.xVelocity

		newpos = self.rect.move(self.movePos)
		if self.area.contains(newpos):
			self.rect = newpos

		pygame.event.pump()

	def jump(self):
		if self.isJumping == False:
			self.yVelocity = self.jumpVelocity
			self.isJumping = True
 	
 	def moveLeftStart(self):
 		self.movingLeft = True
 		#self.movePos[0] -= self.speed

 	def moveLeftStop(self):
 		self.movingLeft = False
 		self.movePos[0] = 0

 	def moveRightStart(self):
 		self.movingRight = True
 		#self.movePos[0] += self.speed
	
	def moveRightStop(self): 
		self.movingRight = False
		self.movePos[0] = 0

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def setId(self, id):
		self.id = id

	def setName(self):
		self.name = name
