#!/usr/bin/python

import pygame
import Resources
import random
from pygame.locals import *

class Particle():
	def __init__(self, x = 0, y = 0, xVel = 0, yVel = 0, color = (255, 255, 255), size = 10):
		self.x = x
		self.y = y
		self.xVel = xVel
		self.yVel = yVel
		self.size = size
		self.rect = pygame.Rect(x, y, size, size)
		self.screen = pygame.display.get_surface()
		self.area = self.screen.get_rect()
		self.area.h += 500
		self.area.y -= 550
		self.color = color

		self.velocity = xVel
		self.gravity = 0.6

		self.movePos = [x, yVel]

	def update(self):
		if self.rect.y < self.screen.get_height() + 50:
			self.movePos[1] += self.gravity
			self.rect.y += self.movePos[1]

			self.movePos[0] += self.velocity
			self.rect.x = self.movePos[0]

			pygame.draw.ellipse(self.screen, self.color, self.rect)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getXVel(self):
		return self.xVel

	def getYVel(self):
		return self.yVel

	def getSize(self):
		return self.size