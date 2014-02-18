#!/usr/bin/python

import pygame
from pygame.locals import *

class Checkbox():
	def __init__(self, surface, x, y, checked = False):
		self.surface = surface
		self.checked = checked

		self.checkboxRect = pygame.Rect(x, y, 15, 15)
		self.crossRect = pygame.Rect(x + 2, y + 2, 11, 11)

		if pygame.font:
			self.font = pygame.font.Font(None, 22)
	
	def update(self):
		pygame.draw.rect(self.surface, (150, 150, 150), self.checkboxRect)

		if self.checked:
			pygame.draw.rect(self.surface, (75, 75, 75), self.crossRect)

	def onCheckbox(self, (x, y)):
		if x >= self.getX() and x <= (self.getX() + 15) and y >= self.getY() and y <= (self.getY() + 15):
			return True
		else:
			return False

	def changeState(self):
		if self.checked:
			self.checked = False
		else:
			self.checked = True

	def getX(self):
		return self.checkboxRect.x

	def getY(self):
		return self.checkboxRect.y
