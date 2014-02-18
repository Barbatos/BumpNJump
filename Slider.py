#!/usr/bin/python

import pygame
from pygame.locals import *

class Slider():
	def __init__(self, surface, x, y, width, value = 0, max = 100):
		self.surface = surface
		self.value = value
		self.max = max

		self.sliderRect = pygame.Rect(x, y, width, 20)
		self.squareRect = pygame.Rect(x, y, 20, 20)

		self.color = pygame.Color(200, 100, 100, 50)

		if pygame.font:
			self.font = pygame.font.Font(None, 22)
	
	def update(self):
		pygame.draw.rect(self.surface, (150, 150, 150), self.sliderRect)
		self.squareRect.x = self.sliderRect.x + (self.value/float(self.max) * (self.sliderRect.w - 20))
		pygame.draw.rect(self.surface, self.color, self.squareRect)

		if pygame.font:
			self.textDisp = self.font.render(str(self.value), 1, (50, 50, 50))

		self.textRect = self.textDisp.get_rect(centerx = self.sliderRect.x + self.sliderRect.w/2, centery = self.sliderRect.y + 11)
		self.surface.blit(self.textDisp, self.textRect)

	def onSlider(self, (x, y)):
		if x >= self.getX() and x <= (self.getX() + self.getWidth()) and y >= self.getY() and y <= (self.getY() + 20):
			return True
		else:
			return False

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

	def setColor(self, color):
		self.color = color