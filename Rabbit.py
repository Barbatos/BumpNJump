#!/usr/bin/python

import pygame
import Resources
from Animation import *
from pygame.locals import *

class Rabbit():
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.mixer.init()

	def __init__(self, id = -1, name = "", objectList = [], objectSpritesList = []):
		self.rect = pygame.Rect(0, 0, 45, 48)
		self.rabbitAnim = Animation("rabbit", 15)
		self.rabbitAnim.setFrameRange(1, 8);
		self.screen = pygame.display.get_surface()
		self.area = self.screen.get_rect()

		self.floorLevel = self.screen.get_height() - self.rect.h

		self.objectList = objectList
		self.objectSpritesList = objectSpritesList

		self.movingLeft = False
		self.movingRight = False
		self.movingUp = False
		self.movingDown = False
		self.isJumping = False
		self.isOnBlock = False

		self.collide = False

		self.speed = 8
		self.id = id
		self.name = name

		self.jumpSound = pygame.mixer.Sound("resources/sound/jump.wav")

		self.velocity = 7
		self.gravity = 0.6
		self.jumpVelocity = -8

		self.movePos = [0,0]
		self.rect.topleft = (300, self.floorLevel)

	def __str__(self):
		print "Rabbit ", self.id,  ": ", self.name

	def update(self):

		if self.movingLeft == True:
			self.movePos[0] = -self.velocity

		if self.movingRight == True:
			self.movePos[0] = self.velocity

		if self.movePos[1] is not 0:
			self.movePos[1] += self.gravity
			self.rect.y += self.movePos[1]

			if self.rect.y > self.floorLevel:
				self.rect.y = self.floorLevel
				self.movePos[1] = 0
				self.isJumping = False

		if self.movePos[1] < 0:
			self.movingUp = True
			self.movingDown = False

		elif self.movePos[1] > 0:
			self.movingUp = False
			self.movingDown = True

		else:
			self.movingUp = False
			self.movingDown = False

		self.checkForCollision()

		newpos = self.rect.move(self.movePos)
		if self.area.contains(newpos) and not self.collide:
			self.rect = newpos

		if self.isJumping:
			self.rabbitAnim.setFrameRange(9, 15)
			if self.movingUp:
				self.rabbitAnim.stopAnim()
				self.rabbitAnim.setCurrentFrame(9)
			else:
				self.rabbitAnim.playAnim()

		else:
			self.rabbitAnim.setFrameRange(1, 8)
			if not self.movingLeft and not self.movingRight:
				self.rabbitAnim.stopAnim()
				self.rabbitAnim.rewind()

		self.rabbitAnim.getRect().x = self.rect.x
		self.rabbitAnim.getRect().y = self.rect.y

		pygame.event.pump()

	def checkForCollision(self):
		if not self.movingLeft and not self.movingRight and self.movePos[1] == 0 and self.velocity == 0 and not self.isJumping:
			return

		for obj in self.objectList:
			if self.movingLeft:
				if (self.rect.x < (obj.rect.x + obj.rect.w)) and (obj.rect.x < self.rect.x):
					if (self.rect.y + self.rect.h) > (obj.rect.y + 1):
						if self.rect.y < (obj.rect.y + obj.rect.h):
							self.movePos[0] = 0

			if self.movingRight:
				if (obj.rect.x < (self.rect.x + self.rect.w)) and (obj.rect.x > self.rect.x):
					if (self.rect.y + self.rect.h) > (obj.rect.y + 1):
						if self.rect.y < (obj.rect.y + obj.rect.h):
							self.movePos[0] = 0

			if self.movingUp:
				if (self.rect.y < (obj.rect.y + obj.rect.h)) and (obj.rect.y < self.rect.y):
					if (self.rect.x + self.rect.w) > obj.rect.x:
						if self.rect.x < (obj.rect.x + obj.rect.w):
							self.movePos[1] = 0.01

			if ((self.rect.y + self.rect.h) > obj.rect.y) and (self.rect.y < obj.rect.y):
				print "bla1"
				if (self.rect.x + self.rect.w) > obj.rect.x:
					print "bla2"
					if self.rect.x < (obj.rect.x + obj.rect.w):
						print "bla3"
						if self.movePos[1] >= 0 and not self.isOnBlock:
							print "bla4"
							self.rect.y = obj.rect.y - self.rect.h
							self.movePos[1] = 0
							self.isJumping = False
							self.isOnBlock = True

			else:
				if self.isOnBlock:
					self.isOnBlock = False
					self.movePos[1] = 0.01

			print self.isOnBlock

			# if ((self.rect.y + self.rect.h) > obj.rect.y) and ((self.rect.y + self.rect.h) < (obj.rect.y + 25)) and (self.rect.y < obj.rect.y):
			# 	if (self.rect.x + self.rect.w) > obj.rect.x:
			# 		if (self.rect.x < (obj.rect.x + obj.rect.w)):
			# 			if self.movePos[1] >= 0 and not self.isOnBlock:
			# 				self.rect.y = obj.rect.y - self.rect.h
			# 				self.isJumping = False
			# 				self.isOnBlock = True
			# 				self.movePos[1] = 0

			# else:
			# 	if self.isOnBlock:
			# 		self.isOnBlock = False
			# 		self.movePos[1] = 0.01

	def jump(self):
		if not self.isJumping:
			self.jumpSound.play()
			self.movePos[1] = self.jumpVelocity
		self.isJumping = True
 	
 	def moveLeftStart(self):
 		if(self.rabbitAnim.getFlip()):
 			self.rabbitAnim.flipAnim()
 		self.rabbitAnim.playAnim()
 		self.movingLeft = True
 		self.movingRight = False

 	def moveLeftStop(self):
 		if not self.movingRight:
	 		self.rabbitAnim.stopAnim()
	 		self.rabbitAnim.rewind()
 		self.movingLeft = False
 		self.movePos[0] = 0

 	def moveRightStart(self):
 		if(not self.rabbitAnim.getFlip()):
 			self.rabbitAnim.flipAnim()
 		self.rabbitAnim.playAnim()
 		self.movingRight = True
 		self.movingLeft = False
	
	def moveRightStop(self):
		if not self.movingLeft:
			self.rabbitAnim.stopAnim()
			self.rabbitAnim.rewind()
		self.movingRight = False
		self.movePos[0] = 0

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getAnim(self):
		return self.rabbitAnim

	def setId(self, id):
		self.id = id

	def setName(self):
		self.name = name
