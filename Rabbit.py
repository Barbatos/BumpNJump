#!/usr/bin/python

import pygame
import Resources
from Animation import *
from pygame.locals import *

class Rabbit():
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

		self.speed = 8
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

		if self.movingLeft == True:
			self.movePos[0] = -self.xVelocity

		if self.movingRight == True:
			self.movePos[0] = self.xVelocity

		self.checkForCollision()

		if self.isJumping == True:

			self.yVelocity += self.gravity
			self.rect.y += self.yVelocity

			if self.rect.y > self.floorLevel:
				self.rect.y = self.floorLevel
				self.isJumping = False 

		self.checkForCollision()

		newpos = self.rect.move(self.movePos)
		if self.area.contains(newpos):
			self.rect = newpos

		self.walkAnim.getRect().x = self.rect.x
		self.walkAnim.getRect().y = self.rect.y

		pygame.event.pump()

	def checkForCollision(self):
		if not self.movingLeft and not self.movingRight and not self.isJumping:
			return

		for obj in [self.objectList[i] for i in self.rect.collidelistall(self.objectList)]:
			if self.xVelocity > 0: 
				self.rect.right = obj.rect.left

			if self.xVelocity < 0:
				self.rect.left = obj.rect.right

			if self.yVelocity > 0:
				self.rect.bottom = obj.rect.top
				self.isJumping = False

			if self.yVelocity < 0:
				self.rect.top = obj.rect.bottom

		#object_hit_list = pygame.sprite.spritecollide(self, self.objectSpritesList, False)
		#for obj in object_hit_list:
		#	if self.movingLeft and (self.rect.left >= obj.rect.left):
		#		self.rect.left = obj.rect.right
		#	if self.movingRight and (self.rect.right <= obj.rect.right):
		#		self.rect.right = obj.rect.left
		#	#if self.isJumping and (self.rect.top <= obj.rect.top):
		#	#	self.rect.top = obj.rect.bottom
		#	if self.isJumping and (self.rect.bottom <= obj.rect.bottom):
		#		self.rect.bottom = obj.rect.top
		#		self.isJumping = False
		#	else:
		#		self.rect.top = self.floorLevel
		#		self.isJumping = False

		#for obj in self.objectList:
		#	if self.movingLeft:
		#		if ((obj.rect.x + obj.rect.w) >= self.rect.x) and (obj.rect.x <= self.rect.x):
		#			if ((obj.rect.y + obj.rect.h) >= self.rect.y):
		#				self.movePos[0] = 0

		#	if self.movingRight:
		#		if ((obj.rect.x + obj.rect.w) <= self.rect.x) and (obj.rect.x >= self.rect.x):
		#			if ((obj.rect.y + obj.rect.h) >= self.rect.y):
		#				self.movePos[0] = 0

	def jump(self):
		if self.isJumping == False:
			self.yVelocity = self.jumpVelocity
			self.isJumping = True
 	
 	def moveLeftStart(self):
 		if(self.walkAnim.getFlip()):
 			self.walkAnim.flipAnim()
 		self.walkAnim.playAnim()
 		self.movingLeft = True

 	def moveLeftStop(self):
 		self.walkAnim.stopAnim()
 		self.walkAnim.rewind()
 		self.movingLeft = False
 		self.movePos[0] = 0

 	def moveRightStart(self):
 		if(not self.walkAnim.getFlip()):
 			self.walkAnim.flipAnim()
 		self.walkAnim.playAnim()
 		self.movingRight = True
	
	def moveRightStop(self):
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
