#!/usr/bin/python

import pygame
import Resources
import random
import time
from pygame.locals import *
from Blood import *

class Explosion():
	def __init__(self, x = 0, y = 0, color = (255, 255, 255)):
		self.particles = []

		self.x = x
		self.y = y

		self.started = False

		for i in range(0, 10):
			if random.randint(1, 3) == 1:
				self.particles.append(Blood(x, y, random.uniform(-5, 5), random.uniform(-5, -2), (133, 6, 6), random.randint(5, 10), random.randint(5, 15)))
			else:
				self.particles.append(Blood(x, y, random.uniform(-5, 5), random.uniform(-5, -2), color, random.randint(5, 10), random.randint(5, 15)))

	def update(self):
		if self.started:
			for part in self.particles:
				part.update()

	def startExplosion(self):
		self.started = True

	def stopExplosion(self):
		self.started = False

	def getId(self):
		return self.id

	def setId(self, id):
		self.id = id