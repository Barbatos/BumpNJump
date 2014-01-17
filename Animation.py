#!/usr/bin/python

import pygame
import math
import Resources
from pygame.locals import *

class Animation(pygame.sprite.Sprite):
	def __init__(self, image, nbFrames, FPS):
		pygame.sprite.Sprite.__init__(self)
		self.arrAnim = []
		for i in range(0, nbFrames):
			if i + 1 < 10:
				self.arrAnim.append(Resources.loadPNG(image + "000" + str(i + 1) + ".png", True))
			elif i + 1 < 100:
				self.arrAnim.append(Resources.loadPNG(image + "00" + str(i + 1) + ".png", True))
			else:
				self.arrAnim.append(Resources.loadPNG(image + "0" + str(i + 1) + ".png", True))

		self.currentFrameNb = 0
		self.image, self.rect = self.arrAnim[self.currentFrameNb]

		screen = pygame.display.get_surface()
		self.area = screen.get_rect()

		self.FPS = FPS
		self.interval = 0
		self.nbFrames = nbFrames
		self.play = True

	def playAnim(self):
		self.play = True

	def stopAnim(self):
		self.play = False

	def isRunning(self):
		return self.play

	def update(self):
		if self.interval < float(self.FPS)/24:
			self.interval += 1
		else:
			self.interval = 0
			if self.play:
				self.currentFrameNb += 1
				self.currentFrameNb %= self.nbFrames

		self.image, self.rect = self.arrAnim[self.currentFrameNb]

		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
