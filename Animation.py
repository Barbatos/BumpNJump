#!/usr/bin/python

import pygame
import math
import Resources
from pygame.locals import *

class Animation(pygame.sprite.Sprite):
	def __init__(self, image, nbFrames):
		pygame.sprite.Sprite.__init__(self)
		self.arrAnim = []
		for i in range(0, nbFrames):
			if i + 1 < 10:
				self.arrAnim.append(Resources.loadPNG(image + "000" + str(i + 1) + ".png", True))
			elif i + 1 < 100:
				self.arrAnim.append(Resources.loadPNG(image + "00" + str(i + 1) + ".png", True))
			else:
				self.arrAnim.append(Resources.loadPNG(image + "0" + str(i + 1) + ".png", True))
		for i in range(0, nbFrames):
			if i + 1 < 10:
				self.arrAnim.append(Resources.loadPNG(image + "000" + str(i + 1) + ".png", True, True))
			elif i + 1 < 100:
				self.arrAnim.append(Resources.loadPNG(image + "00" + str(i + 1) + ".png", True, True))
			else:
				self.arrAnim.append(Resources.loadPNG(image + "0" + str(i + 1) + ".png", True, True))

		self.currentFrameNb = 0
		self.image, self.rect = self.arrAnim[self.currentFrameNb]

		screen = pygame.display.get_surface()
		self.area = screen.get_rect()

		self.flip = False
		self.interval = 0
		self.nbFrames = nbFrames
		self.play = True

	def playAnim(self):
		self.play = True

	def stopAnim(self):
		self.play = False

	def isRunning(self):
		return self.play

	def rewind(self):
		self.currentFrameNb = 0

	def nextFrame(self):
		currentFrameNb += 1

	def flipAnim(self):
		if self.flip:
			self.flip = False
		else:
			self.flip = True

	def getFlip(self):
		return self.flip

	def getRect(self):
		return self.rect

	def setRect(self, rect):
		self.rect = rect

	def update(self):
		if self.interval < 60./24:
			self.interval += 1
		else:
			self.interval = 0
			if self.play:
				self.currentFrameNb += 1
				self.currentFrameNb %= self.nbFrames

			if self.flip:
				self.image, self.rect = self.arrAnim[self.currentFrameNb + self.nbFrames]
			else:
				self.image, self.rect = self.arrAnim[self.currentFrameNb]
