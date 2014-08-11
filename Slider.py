#!/usr/bin/python

import pygame
from pygame.locals import *

class Slider():
	def __init__(self, x, y, width, value = 50, max = 100):
		self.screen = pygame.display.get_surface()
		self.value = value
		self.max = max

		self.sliderRect = pygame.Rect(x, y, width, 20)
		self.squareRect = pygame.Rect(x, y, width/2, 20)

		if pygame.font:
			self.font = pygame.font.Font(None, 22)
	
	def update(self):
		pygame.draw.rect(self.screen, (150, 150, 150), self.sliderRect)
		self.squareRect.w = self.value/float(self.max) * self.sliderRect.w
		pygame.draw.rect(self.screen, (125, 125, 200), self.squareRect)

		if pygame.font:
			self.textDisp = self.font.render(str(self.value), 1, (50, 50, 50))

		self.textRect = self.textDisp.get_rect(centerx = self.sliderRect.x + self.sliderRect.w/2, centery = self.sliderRect.y + 11)
		self.screen.blit(self.textDisp, self.textRect)

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

	def setValueByMousePos(self, x):
		if x < self.sliderRect.x:
			self.value = 0
		elif x > (self.sliderRect.x + self.sliderRect.w):
			self.value = self.max
		else:
			self.value =  int((x - self.sliderRect.x) / float(self.sliderRect.w) * self.max)
		
	def setValueByNumber(self, value):
		self.value = value