#!/usr/bin/python

import pygame
import Resources

class Object(pygame.sprite.Sprite):
	def __init__(self, name = "", img = "", x = 0, y = 0):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = Resources.loadPNG(img, False)
		screen = pygame.display.get_surface()

		self.name = name
		self.posX = x
		self.posY = y

		self.rect.topleft = (self.posX, self.posY)

	def __repr__(self):
		return "Object ", self.name, " (", str(self.posX), ",", str(self.posY), ")"

	def getName(self):
		return self.name

	def getPosX(self):
		return self.posX

	def getPosY(self):
		return self.posY
