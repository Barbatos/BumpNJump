#!/usr/bin/python

import pygame
import math
import Resources
from pygame.locals import *

class Rabbit(pygame.sprite.Sprite):
	def __init__(self, id = -1, name = ""):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = Resources.loadPNG("test.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.speed = 10
		self.id = id
		self.name = name
		self.standStill()

	def __repr__(self):
		print("Rabbit " + self.id + ": " + self.name)

	def update(self):
		newpos = self.rect.move(self.movePos)
		if self.area.contains(newpos):
			self.rect = newpos

		pygame.event.pump()

	def moveUp(self):
		self.movePos[1] = self.movePos[1] - self.speed
		self.state = "moveUp"
		print "moveup"

	def moveDown(self):
		self.movePos[1] = self.movePos[1] + self.speed
		self.state = "moveDown"
 	
 	def moveLeft(self):
 		self.movePos[0] = self.movePos[0] - self.speed
 		self.state = "moveLeft"

 	def moveRight(self):
 		self.movePos[0] = self.movePos[0] + self.speed
 		self.state = "moveRight"
 		
 	def standStill(self):
 		self.state = "standStill"
 		self.movePos = [0, 0]

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def setId(self, id):
		self.id = id

	def setName(self):
		self.name = name
