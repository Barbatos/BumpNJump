#!/usr/bin/python

import pygame
from pygame.locals import *

class Button():
	def __init__(self, surface, x, y, width, height, text):
		self.surface = surface
		self.text = text
		self.buttonRect = pygame.Rect(x, y, width, height)

		self.color = pygame.Color(150, 150, 150)

		if pygame.font:
			font = pygame.font.Font(None, 22)
			self.textDisp = font.render(self.text, 1, (100, 100, 100))

		self.textRect = self.textDisp.get_rect(centerx = x + width/2, centery = y + height/2)
	
	def update(self):
		pygame.draw.rect(self.surface, self.color, self.buttonRect)
		self.surface.blit(self.textDisp, self.textRect)

	def onButton(self, (x, y)):
		if x >= self.getX() and x <= (self.getX() + self.getWidth()) and y >= self.getY() and y <= (self.getY() + self.getHeight()):
			return True
		else:
			return False

	def getX(self):
		return self.buttonRect.x

	def getY(self):
		return self.buttonRect.y

	def getWidth(self):
		return self.buttonRect.w

	def getHeight(self):
		return self.buttonRect.h

	def getText(self):
		return self.text

	def setColor(self, color):
		self.color = color