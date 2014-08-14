#!/usr/bin/python

import pygame
import Resources
import random
from pygame.locals import *

class Blood():
	def __init__(self, x = 0, y = 0, xVel = 0, yVel = 0, color = (255, 255, 255), size = 10, trail = 2):
		self.screen = pygame.display.get_surface()
		self.area = self.screen.get_rect()
		self.area.h += 500
		self.area.y -= 550

		self.x = x
		self.y = y
		self.size = size
		self.color = color

		self.velocity = xVel
		self.gravity = 0.6

		self.movePos = [x, yVel]

		self.trail = []

		for i in range(0, trail):
			self.trail.append((self.x, self.y))

	def update(self):
		if self.trail[0][1] < self.screen.get_height() + 50:
			del self.trail[0]

			self.movePos[1] += self.gravity
			self.y += self.movePos[1]

			self.movePos[0] += self.velocity
			self.x = self.movePos[0]

			self.trail.append((int(self.x), int(self.y)))

			for i in range(0, len(self.trail) - 2):
				pygame.draw.circle(self.screen, (133, 6, 6), self.trail[i + 1], int((float(i + 1)/len(self.trail) * self.size)/random.randint(1, 2)))
			
			pygame.draw.circle(self.screen, self.color, self.trail[-1], self.size)