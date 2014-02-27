#!/usr/bin/python

import pygame
from pygame.locals import *

class Toolbar():
	def __init__(self, type):
		self.screen = pygame.display.get_surface()
		self.type = type
		self.barRect = pygame.Rect(0, self.screen.get_rect().y - 50, self.screen.get_rect().w, 50)
	
	def update(self):
		pygame.draw.rect(self.screen, (150, 150, 150), self.barRect)

	def playingUpdate():
		print "bla"

	def getX(self):
		return self.sliderRect.x

	def getY(self):
		return self.sliderRect.y

	def getWidth(self):
		return self.sliderRect.w

	def getValue(self):
		return self.value

	def setValue(self, x):
		self.value =  int((x - self.sliderRect.x) / float(self.sliderRect.w) * self.max)
		