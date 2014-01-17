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

		self.movingLeft = False
		self.movingRight = False
		self.isJumping = False

		self.speed = 10
		self.id = id
		self.name = name

		self.yVelocity = 0
		self.xVelocity = 5
		self.gravity = 1.2

		self.movePos = [0,0]
		self.rect.topleft = (100, 550)

	def __repr__(self):
		print("Rabbit " + self.id + ": " + self.name)

	def update(self):
		if self.isJumping == True:

			self.yVelocity += self.gravity
			self.rect.y += self.yVelocity

			if self.rect.y > 550:
				self.rect.y = 550
				self.isJumping = False 

		newpos = self.rect.move(self.movePos)
		if self.area.contains(newpos):
			self.rect = newpos

		pygame.event.pump()

	def jump(self):
		if self.isJumping == False:
			self.yVelocity = -15
			self.isJumping = True
 	
 	def moveLeftStart(self):
 		self.movingLeft = True
 		self.movePos[0] -= self.speed
 		self.state = "moveLeft"

 	def moveLeftStop(self):
 		self.movingLeft = False
 		self.movePos[0] = 0

 	def moveRightStart(self):
 		self.movingRight = True
 		self.movePos[0] += self.speed
 		self.state = "moveRight"
	
	def moveRightStop(self): 
		self.movingRight = False
		self.movePos[0] = 0

 	def standStill(self):
 		self.state = "standStill"
 		self.movePos = [50, 550]

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def setId(self, id):
		self.id = id

	def setName(self):
		self.name = name
