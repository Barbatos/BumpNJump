#!/usr/bin/python

import pygame
import Resources
import random
import math
from Animation import *
from pygame.locals import *
from Explosion import *
from random import randint

class Butterfly():
	def __init__(self, x, y, color = (255, 255, 255), objectList = [], spriteList = []):
		self.objectList = objectList
		self.spriteList = spriteList

		self.rect = pygame.Rect(x, y, 15, 15)
		self.screen = pygame.display.get_surface()

		self.butterflyAnim = Animation("butterfly", 8)
		self.butterflyAnim.updateColor(color)
		self.butterflyAnim.setFrameRange(1, 8);
		self.butterflyAnim.setCurrentFrame(randint(1, 8))

		self.sprite = pygame.sprite.RenderPlain(self.butterflyAnim)

		self.butterflyAnim.playAnim()

		self.area = self.screen.get_rect()
		self.color = color

		self.floorLevel = self.screen.get_height() - self.rect.h

		self.movingLeft = False
		self.movingRight = False
		self.movingUp = False
		self.movingDown = False

		self.degree = randint(0, 360)
		self.speed = 4

		self.detlaUpdate = 0

		self.collide = False

		self.movePos = [0,0.01]

	def update(self):
		if(self.detlaUpdate == 1):
			self.detlaUpdate = 0

			limitBottom = self.degree - 20
			limitTop = self.degree + 20

			self.degree = randint(limitBottom, limitTop)

			self.degree = self.degree % 360

			if(randint(0, 1) == 0):
				if(self.speed < 6):
					self.speed += 1

			else:
				if(self.speed > 2):
					self.speed -= 1

			self.movePos[0] = math.cos(math.radians(self.degree)) * self.speed
			self.movePos[1] = math.sin(math.radians(self.degree)) * self.speed

			#self.movePos[0] = randint(-8, 8)
			#self.movePos[1] = randint(-8, 8)

			self.checkForCollision()

			newpos = self.rect.move(self.movePos)
			if self.area.contains(newpos) and not self.collide:
				self.rect = newpos

			self.butterflyAnim.getRect().x = self.rect.x
			self.butterflyAnim.getRect().y = self.rect.y

			if self.degree >= 90 and self.degree <= 240:
				self.movingLeft = True
				self.movingRight = False
			else:
				self.movingLeft = False
				self.movingRight = True

			if self.degree >= 0 and self.degree <= 180:
				self.movingDown = True
				self.movingUp = False
			else:
				self.movingDown = False
				self.movingUp = True

		else:
			self.detlaUpdate += 1

		self.butterflyAnim.update()
		self.sprite.update()
		self.sprite.draw(self.screen)

		pygame.event.pump()

	def collisionDetection(self, obj, rabbit = False):
		#FLEE BEHAVIOR !!!

		objCenterX = obj.rect.x + obj.rect.w/2
		objCenterY = obj.rect.y + obj.rect.h/2

		butterflyCenterX = self.rect.x + self.rect.w/2
		butterflyCenterY = self.rect.y + self.rect.h/2

		dist = math.fabs(math.sqrt(((objCenterX - butterflyCenterX) * (objCenterX - butterflyCenterX)) + ((objCenterY - butterflyCenterY) * (objCenterY - butterflyCenterY))))
		
		if dist < 50:
			distX = math.fabs(objCenterX - butterflyCenterX)
			angle = math.degrees(math.acos(distX/dist))

			if (objCenterX <= butterflyCenterX) and (objCenterY <= butterflyCenterY):
				angle = 240 - angle

			elif (objCenterX > butterflyCenterX) and (objCenterY <= butterflyCenterY):
				angle = 360 - angle

			elif (objCenterX <= butterflyCenterX) and (objCenterY > butterflyCenterY):
				angle = 180 - angle

			angle += 180
			angle = angle % 360

			self.degree = int(angle)

		#FLEE BEHAVIOR !!!

		# if (self.rect.x < (obj.rect.x + obj.rect.w)) and (obj.rect.x < self.rect.x):
		# 	if (self.rect.y + self.rect.h) > (obj.rect.y + 1):
		# 		if self.rect.y < (obj.rect.y + obj.rect.h):
		# 			self.movePos[0] = 5

		# if (obj.rect.x < (self.rect.x + self.rect.w)) and (obj.rect.x > self.rect.x):
		# 	if (self.rect.y + self.rect.h) > (obj.rect.y + 1):
		# 		if self.rect.y < (obj.rect.y + obj.rect.h):
		# 			self.movePos[0] = -5

		# if (self.rect.y <= (obj.rect.y + obj.rect.h)) and (obj.rect.y <= self.rect.y):
		# 	if (self.rect.x + self.rect.w) > (obj.rect.x + 3):
		# 		if self.rect.x < (obj.rect.x + obj.rect.w - 5):
		# 			self.movePos[1] = 5

		# if ((self.rect.y + self.rect.h) >= obj.rect.y) and (self.rect.y <= obj.rect.y):
		# 	if (self.rect.x + self.rect.w) > (obj.rect.x + 3):
		# 		if self.rect.x < (obj.rect.x + obj.rect.w - 5):
		# 			if self.movePos[1] >= 0:
		# 				self.rect.y = obj.rect.y - self.rect.h
		# 				self.movePos[1] = -5

	def screenCollisionDetection(self):
		butterflyCenterX = self.rect.x + self.rect.w/2
		butterflyCenterY = self.rect.y + self.rect.h/2

		distBorder = butterflyCenterX
		if distBorder < 10:
			self.degree = 0

		if (butterflyCenterY) < distBorder:
			distBorder = butterflyCenterY
			if distBorder < 10:
				self.degree = 90

		if (self.screen.get_rect().w - butterflyCenterX) < distBorder:
			distBorder = self.screen.get_rect().w - butterflyCenterX
			if distBorder < 10:
				self.degree = 180

		if (self.screen.get_rect().h - butterflyCenterY) < distBorder:
			distBorder = self.screen.get_rect().h - butterflyCenterY
			if distBorder < 10:
				self.degree = 240

	def checkForCollision(self):
		#if not self.movingLeft and not self.movingRight and self.movePos[1] == 0 and self.velocity == 0:
		#	return

		for obj in self.objectList:
			if obj.getType() is not "carrot":
				self.collisionDetection(obj, False)

		self.screenCollisionDetection()

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
