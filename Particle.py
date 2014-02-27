#!/usr/bin/python

import pygame
import Resources
import random
from pygame.locals import *

class Particle():
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.mixer.init()

	def __init__(self, id = -1, x = 0, y = 0, color = (255, 255, 255), trail = 1):
		self.rect = pygame.Rect(x, y, 20, 20)
		self.screen = pygame.display.get_surface()
		self.area = self.screen.get_rect()
		self.area.h += 500
		self.area.y -= 550
		self.id = id
		self.color = color
		self.trail = trail

		self.floorLevel = self.screen.get_height() - self.rect.h

		self.velocity = random.uniform(-5, 5)
		self.gravity = 0.6

		self.movePos = [x, random.uniform(-15, -5)]

	def update(self):
		self.movePos[1] += self.gravity
		self.rect.y += self.movePos[1]

		self.movePos[0] += self.velocity
		self.rect.x = self.movePos[0]

		pygame.draw.ellipse(self.screen, self.color, self.rect)

	def getId(self):
		return self.id

	def setId(self, id):
		self.id = id