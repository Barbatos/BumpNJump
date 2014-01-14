#!/usr/bin/python

import pygame
import Resources
from pygame.locals import *

class Rabbit(pygame.sprite.Sprite):
	def __init__(self, id = -1, name = ""):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = Resources.loadPNG("test.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.id = id
		self.name = name

	def __repr__(self):
		print("Rabbit " + self.id + ": " + self.name)

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def setId(self, id):
		self.id = id

	def setName(self):
		self.name = name