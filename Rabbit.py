#!/usr/bin/python

import pygame
import Resources
from Animation import *
from pygame.locals import *

class Rabbit():
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.mixer.init()

	def __init__(self, id = -1, name = "", objectList = [], objectSpritesList = []):
		self.rect = pygame.Rect(0, 0, 50, 50)
		self.walkAnim = Animation("rabbit_walk", 8)
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()

		self.floorLevel = screen.get_height() - self.rect.h

		self.objectList = objectList
		self.objectSpritesList = objectSpritesList

		self.movingLeft = False
		self.movingRight = False
		self.isJumping = False
		self.isOnBlock = False

		self.speed = 8
		self.id = id
		self.name = name

		self.jumpSound = pygame.mixer.Sound("resources/sound/jump.wav")

		self.yVelocity = 0
		self.xVelocity = 7
		self.gravity = 1.2
		self.jumpVelocity = -15

		self.movePos = [0,0]
		self.rect.topleft = (100, self.floorLevel)

	def __repr__(self):
		print("Rabbit " + self.id + ": " + self.name)

	def update(self):

		if self.movingLeft == True:
			self.movePos[0] = -self.xVelocity

		if self.movingRight == True:
			self.movePos[0] = self.xVelocity

		#if self.isJumping == True:

		if self.yVelocity is not 0:
			self.yVelocity += self.gravity
			self.rect.y += self.yVelocity

			if self.rect.y > self.floorLevel:
				print "HEY"
				self.rect.y = self.floorLevel
				self.yVelocity = 0
				#self.isJumping = False 

		self.checkForCollision()

		newpos = self.rect.move(self.movePos)
		if self.area.contains(newpos):
			self.rect = newpos

		self.walkAnim.getRect().x = self.rect.x
		self.walkAnim.getRect().y = self.rect.y

		pygame.event.pump()

	def checkForCollision(self):
		if not self.movingLeft and not self.movingRight and self.yVelocity == 0 and self.xVelocity == 0:#and not self.isJumping:
			return

		for obj in self.objectList:
			if self.movingLeft:
				if ((obj.rect.x + obj.rect.w) > self.rect.x) and (obj.rect.x < self.rect.x):
					if (self.rect.y + self.rect.h) > obj.rect.y:
						if self.rect.y < (obj.rect.y + obj.rect.h):
							self.movePos[0] = 0

			if self.movingRight:
				if (self.rect.x + self.rect.w) > (obj.rect.x) and (obj.rect.x > self.rect.x):
					if (self.rect.y + self.rect.h) > obj.rect.y:
						if self.rect.y < (obj.rect.y + obj.rect.h):
							self.movePos[0] = 0

			if ((self.rect.y + self.rect.h) >= obj.rect.y) and ((self.rect.y + self.rect.h) < (obj.rect.y + 10)) and (self.rect.y < obj.rect.y):
				if (self.rect.x + self.rect.w) > obj.rect.x:
					if (self.rect.x < (obj.rect.x + obj.rect.w)):
						if self.yVelocity >= 0 and not self.isOnBlock:
							self.rect.y = obj.rect.y - self.rect.h
							self.isJumping = False
							self.isOnBlock = True
							self.yVelocity = 0

			else:
				if self.isOnBlock:
					self.isOnBlock = False
					self.yVelocity = 2

	def jump(self):
		#if self.isJumping == False:
		self.jumpSound.play()
		self.yVelocity = self.jumpVelocity
		#self.isJumping = True
 	
 	def moveLeftStart(self):
 		if(self.walkAnim.getFlip()):
 			self.walkAnim.flipAnim()
 		self.walkAnim.playAnim()
 		self.movingLeft = True
 		self.movingRight = False

 	def moveLeftStop(self):
 		if not self.movingRight:
	 		self.walkAnim.stopAnim()
	 		self.walkAnim.rewind()
 		self.movingLeft = False
 		self.movePos[0] = 0

 	def moveRightStart(self):
 		if(not self.walkAnim.getFlip()):
 			self.walkAnim.flipAnim()
 		self.walkAnim.playAnim()
 		self.movingRight = True
 		self.movingLeft = False
	
	def moveRightStop(self):
		if not self.movingLeft:
			self.walkAnim.stopAnim()
			self.walkAnim.rewind()
		self.movingRight = False
		self.movePos[0] = 0

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getAnim(self):
		return self.walkAnim

	def setId(self, id):
		self.id = id

	def setName(self):
		self.name = name
