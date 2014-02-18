#!/usr/bin/python

import pygame
import Resources

class Object(pygame.sprite.Sprite):
	def __init__(self, name = "", x = 0, y = 0, type = "earth"):
		self.typeList = {"earth":"earth.png", "ice":"ice.png", "carrot":"carrot.png", "boing":"boing.png"}

		self.name = name
		self.posX = x
		self.posY = y
		self.type = type

		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = Resources.loadPNG(self.typeList[self.type], False)
		screen = pygame.display.get_surface()

		self.rect.topleft = (self.posX, self.posY)

	def __str__(self):
		print "Object ", self.name, " (", str(self.posX), ",", str(self.posY), self.type, ")"

	def getName(self):
		return self.name

	def getX(self):
		return self.posX

	def getY(self):
		return self.posY

	def getType(self):
		return self.type