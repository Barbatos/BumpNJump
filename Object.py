#!/usr/bin/python

import pygame
import Resources

class Object(pygame.sprite.Sprite):
	def __init__(self, id = -1, x = 0, y = 0, type = "earth"):
		self.typeList = {"earth":"earth.png", "ice":"ice.png", "carrot":"carrot.png", "boing":"boing.png"}

		self.id = id
		self.posX = x
		self.posY = y
		self.type = type

		self.friction = 0.7

		if self.type == "ice":
			self.friction == 0.2

		if self.type == "empty":
			self.rect = pygame.Rect(0, 0, 0, 0)
		else:
			pygame.sprite.Sprite.__init__(self)
			self.image, self.rect = Resources.loadPNG(self.typeList[self.type])

		self.rect.topleft = (self.posX, self.posY)

	def __str__(self):
		print "Object ", self.id, " (", str(self.posX), ",", str(self.posY), self.type, ")"

	def replaceImage(self, objType, isFloor = False):
		if isFloor:
			self.image = Resources.loadPNG(self.typeList[objType])[0]
		else:
			self.image = Resources.loadPNG("middle_" + self.typeList[objType])[0]

	def getId(self):
		return self.id

	def getX(self):
		return self.posX

	def getY(self):
		return self.posY

	def getType(self):
		return self.type

	def isInBlock(self, x, y):
		if x >= self.posX and x <= (self.posX + self.rect.w) and y >= self.posY and y <= (self.posY + self.rect.h):
			return True
		else:
			return False

	def getFriction(self):
		return self.friction