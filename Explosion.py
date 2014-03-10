#!/usr/bin/python

import pygame
import Resources
import random
import time
from pygame.locals import *
from Particle import *

class Explosion():
	def __init__(self, x = 0, y = 0, color = (255, 255, 255)):
		self.particles = []

		self.x = x
		self.y = y

		self.started = False

		for i in range(0, 10):
			self.particles.append(Particle(x, y, random.uniform(-5, 5), random.uniform(-5, -2), color, random.randint(10, 20)))

	def update(self):
		if self.started:
			for part in self.particles:
				part.update()

	def startExplosion(self):
		self.started = True

	def stopExplosion(self):
		self.started = False

	def setTrail(self):
		for part in self.particles:
			for j in range(10, 0, -1):
				self.particles.append(Particle(self.x, self.y, part.getXVel(), part.getYVel(), (j * 10, 20, 20), part.getSize() - (10 - j)))

				interval = 0
				while interval < 6000:
					interval += 1

	def getId(self):
		return self.id

	def setId(self, id):
		self.id = id