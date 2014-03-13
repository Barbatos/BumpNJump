#!/usr/bin/python

import pygame
import math
import Resources
from pygame.locals import *

class Animation(pygame.sprite.Sprite):
	def __init__(self, image, nbFrames):
		pygame.sprite.Sprite.__init__(self)

		self.flip = False
		self.interval = 0
		self.nbFrames = nbFrames
		self.play = True
		self.start = 0
		self.end = nbFrames - 1
		self.cyclic = True
		self.imageName = image

		self.arrAnim = []
		for i in range(0, self.nbFrames):
			if i + 1 < 10:
				self.arrAnim.append(Resources.loadPNG(self.imageName + "000" + str(i + 1) + ".png", True))
			elif i + 1 < 100:
				self.arrAnim.append(Resources.loadPNG(self.imageName + "00" + str(i + 1) + ".png", True))
			else:
				self.arrAnim.append(Resources.loadPNG(self.imageName + "0" + str(i + 1) + ".png", True))

		self.currentFrameNb = self.start
		self.image, self.rect = self.arrAnim[self.currentFrameNb]

	def update(self):
		if self.interval < 60./24:
			self.interval += 1
		else:
			self.interval = 0
			if self.play:
				self.currentFrameNb += 1

				if self.currentFrameNb > self.end:
					if self.cyclic:
						self.currentFrameNb = self.start
					else:
						self.currentFrameNb = self.end

			if self.flip:
				self.image, self.rect = self.arrAnim[self.currentFrameNb + self.nbFrames/2]
			else:
				self.image, self.rect = self.arrAnim[self.currentFrameNb]

	def updateColor(self, color):
		for img in self.arrAnim:
			img[0].fill(color, special_flags = BLEND_MULT)

	def resetColor(self, color):
		self.arrAnim = []
		for i in range(0, self.nbFrames):
			if i + 1 < 10:
				self.arrAnim.append(Resources.loadPNG(self.imageName + "000" + str(i + 1) + ".png", True))
			elif i + 1 < 100:
				self.arrAnim.append(Resources.loadPNG(self.imageName + "00" + str(i + 1) + ".png", True))
			else:
				self.arrAnim.append(Resources.loadPNG(self.imageName + "0" + str(i + 1) + ".png", True))

		for img in self.arrAnim:
			img[0].fill(color, special_flags = BLEND_MULT)

	def playAnim(self, cyclic = True):
		self.play = True
		if not cyclic:
			self.cyclic = False
		else:
			self.cyclic = True

	def stopAnim(self):
		self.play = False

	def isRunning(self):
		return self.play

	def rewind(self):
		self.currentFrameNb = 0

	def nextFrame(self):
		self.currentFrameNb += 1

	def setCurrentFrame(self, index):
		self.currentFrameNb = index - 1

	def flipAnim(self):
		if self.flip:
			self.flip = False
		else:
			self.flip = True

	def setFrameRange(self, start, end):
		self.start = start - 1
		self.end = end - 1

	def getFlip(self):
		return self.flip

	def getRect(self):
		return self.rect

	def setPos(self, x, y):
		for img in self.arrAnim:
			img[1].x = x
			img[1].y = y

	def setRect(self, rect):
		self.rect = rect
