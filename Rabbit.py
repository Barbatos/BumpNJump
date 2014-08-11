#!/usr/bin/python

import pygame
import Resources
import random
from Animation import *
from pygame.locals import *
from Explosion import *
from Carrot import *

class Rabbit():
	pygame.mixer.pre_init(44100, -16, 2, 1024)
	pygame.mixer.init()

	def __init__(self, id = -1, name = "", color = (255, 255, 255), objectList = [], spriteList = []):
		self.objectList = objectList
		self.spriteList = spriteList

		self.rabbitList = []

		self.color = color
		self.rect = pygame.Rect(0, 0, 43, 30)
		self.rabbitAnim = Animation("rabbit", 30)
		self.rabbitAnim.updateColor(self.color)
		self.rabbitAnim.setFrameRange(1, 8);
		self.screen = pygame.display.get_surface()
		self.area = self.screen.get_rect()
		self.area.h += 500
		self.area.y -= 550

		self.floorLevel = self.screen.get_height() - self.rect.h

		self.explosion = Explosion()

		self.movingLeft = False
		self.movingRight = False
		self.movingUp = False
		self.movingDown = False
		self.isJumping = False
		self.isOnBlock = False

		self.direction = "left"

		self.collide = False

		self.touched = False
		self.touchDelay = 0

		self.id = id
		self.name = name

		self.jumpSound = pygame.mixer.Sound("resources/sound/jump.wav")
		self.splashSound = pygame.mixer.Sound("resources/sound/splash.wav")
		self.carrotSound = pygame.mixer.Sound("resources/sound/carrot.wav")

		self.jumpSound.set_volume(float(Resources.getOptionValue("sound"))/100)
		self.splashSound.set_volume(float(Resources.getOptionValue("sound"))/100)
		self.carrotSound.set_volume(float(Resources.getOptionValue("sound"))/100)

		self.velocity = 5
		self.gravity = 0.6

		self.movePos = [0,0.01]

		self.replaceRabbit()

		self.points = 0
		self.carrots = 0

		self.thrownCarrots = []

		self.blood = Resources.getOptionValue("blood")

	def __str__(self):
		print "Rabbit ", self.id,  ": ", self.name

	def update(self):
		if self.touched:
			touchDelayCalculation()

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
				self.rabbitAnim.playAnim(False)

		else:
			self.rabbitAnim.setFrameRange(1, 8)
			if not self.movingLeft and not self.movingRight:
				self.rabbitAnim.stopAnim()
				self.rabbitAnim.rewind()
			else:
				self.rabbitAnim.playAnim()

		self.rabbitAnim.getRect().x = self.rect.x
		self.rabbitAnim.getRect().y = self.rect.y - 18

		pygame.event.pump()

	def collisionDetection(self, obj, rabbit = False):
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
			if (self.rect.y <= (obj.rect.y + obj.rect.h)) and (obj.rect.y <= self.rect.y):
				if (self.rect.x + self.rect.w) > (obj.rect.x + 3):
					if self.rect.x < (obj.rect.x + obj.rect.w - 5):
						self.movePos[1] = 0.01

		if ((self.rect.y + self.rect.h) >= obj.rect.y) and (self.rect.y <= obj.rect.y):
			if (self.rect.x + self.rect.w) > (obj.rect.x + 3):
				if self.rect.x < (obj.rect.x + obj.rect.w - 5):
					if self.movePos[1] >= 0 and not self.isOnBlock:
						self.isJumping = False
						
						if rabbit:
							self.jump(5)
							if self.blood == 1:
								obj.explosion = Explosion(obj.rect.x, obj.rect.y, obj.color)
								obj.explosion.startExplosion()
								self.splashSound.play()
							obj.replaceRabbit()
							self.points += 1

						elif obj.getType() == "boing":
							self.jump(12.7)

						else:
							self.rect.y = obj.rect.y - self.rect.h
							self.movePos[1] = 0
							self.isOnBlock = True

		if self.isJumping:
			self.isOnBlock = False

		if self.isOnBlock:
			if (self.rect.x > (obj.rect.x + obj.rect.w)) or ((self.rect.x + self.rect.w) < obj.rect.x):
				self.isOnBlock = False
				self.movePos[1] = 0.01

	def checkForCollision(self):
		if not self.movingLeft and not self.movingRight and self.movePos[1] == 0 and self.velocity == 0 and not self.isJumping:
			return

		for obj in self.objectList:
			if obj.getType() == "carrot" and obj.isInBlock(self.rect.x + self.rect.w/2, self.rect.y + self.rect.h -5):
				self.carrotSound.play()
				self.carrots += 1
				self.objectList.remove(obj)
				self.spriteList.remove(obj)

			if obj.getType() is not "carrot":
				self.collisionDetection(obj, False)

		for rabbit in self.rabbitList:
			self.collisionDetection(rabbit, True)

	def jump(self, velocity = 8.1):
		if not self.isJumping:
			self.jumpSound.play()
			self.movePos[1] = -velocity
		self.isJumping = True
 	
 	def moveLeftStart(self):
 		if self.rabbitAnim.getFlip():
 			self.rabbitAnim.flipAnim()
 		self.rabbitAnim.playAnim()
 		self.movingLeft = True
 		self.movingRight = False
 		self.direction = "left"

 	def moveLeftStop(self):
 		if not self.movingRight:
	 		self.rabbitAnim.stopAnim()
	 		self.rabbitAnim.rewind()
 		self.movingLeft = False
 		self.movePos[0] = 0

 	def moveRightStart(self):
 		if not self.rabbitAnim.getFlip():
 			self.rabbitAnim.flipAnim()
 		self.rabbitAnim.playAnim()
 		self.movingRight = True
 		self.movingLeft = False
 		self.direction = "right"
	
	def moveRightStop(self):
		if not self.movingLeft:
			self.rabbitAnim.stopAnim()
			self.rabbitAnim.rewind()
		self.movingRight = False
		self.movePos[0] = 0

	def appendRabbit(self, rabbit):
		self.rabbitList.append(rabbit)

	def replaceRabbit(self):
		while True:
			randObj = self.objectList[random.randint(1, len(self.objectList)) - 1]
			if self.isFloor(randObj):
				break

		self.rect.topleft = (randObj.rect.x, randObj.rect.y - randObj.rect.h)

	def isInBlock(self, x, y):
		for obj in self.objectList:
			if obj.isInBlock(x, y):
				return True

		return False

	def isFloor(self, object):
		if self.isInBlock(object.getX() + 5, object.getY() - 5):
			return False

		return True

	def touch(self):
		self.touched = True
		self.touchDelay = 300

	def touchDelayCalculation(self):
		self.touchDelay -= 1

		if(self.touchDelay == 0):
			self.touched = False

	def isTouched(self):
		return self.touched

	def throwCarrot(self):
		if(self.carrots > 0):
			if(self.direction == "right"):
				self.thrownCarrots.append(Carrot(self.direction, self.rect.x + 40, self.rect.y - 18, self.objectList))
			else:
				self.thrownCarrots.append(Carrot(self.direction, self.rect.x - 42, self.rect.y - 18, self.objectList))
			self.carrots -= 1

	def updateColor(self, color):
		self.rabbitAnim.updateColor(color)

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getPoints(self):
		return self.points

	def getAnim(self):
		return self.rabbitAnim

	def setId(self, id):
		self.id = id

	def setName(self, name):
		self.name = name

	def setPoints(self, points):
		self.points = points
