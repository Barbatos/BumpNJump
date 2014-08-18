#!/usr/bin/python

import pygame
import Resources
from Animation import *
from pygame.locals import *

class Carrot():
	def __init__(self, direction, posX, posY, objectList = [], rabbitList = []):
		self.objectList = objectList
		self.rabbitList = rabbitList

		self.carrotAnim = Animation("carrot", 24)
		self.carrotAnim.setFrameRange(1, 12);

		self.rect = pygame.Rect(posX, posY, 25, 25)
		self.carrotAnim.setRect(self.rect)

		self.carrotAnim.playAnim()

		self.sprite = pygame.sprite.RenderPlain(self.carrotAnim)

		self.screen = pygame.display.get_surface()
		self.area = self.screen.get_rect()
		self.area.h += 500
		self.area.y -= 550
		self.area.w -= 200

		self.smoked = False
		self.countDown = 60

		self.moveX = posX

		self.direction = direction

		if self.direction == "left":
			self.carrotAnim.flipAnim()

	def update(self):
		if self.smoked:
			self.carrotAnim.setRect(self.rect)
			self.countDown -= 1

			if self.countDown == 0:
				return True

		else:
			if self.direction == "right":
				self.moveX += 6
			else:
				self.moveX -= 6

			self.rect.x = self.moveX

			self.carrotAnim.setRect(self.rect)

			self.checkForCollision()

			if self.rect.x > self.area.w + 10:
				return True
			elif (self.rect.x + self.rect.w) < self.area.x - 10:
				return True

		self.sprite.update()
		self.sprite.draw(self.screen)
		self.carrotAnim.update()

		pygame.event.pump()

		return False

	def collisionDetection(self, obj, rabbit = False):
		if rabbit:
			if (self.rect.y + self.rect.h) > obj.rect.y and self.rect.y < (obj.rect.y + obj.rect.h):
				if self.direction == "right":
					if (self.rect.x + self.rect.w) > obj.rect.x:
						obj.touch()
						self.smoke()

				else:
					if self.rect.x < (obj.rect.x + obj.rect.w):
						obj.touch()
						self.smoke()



		else:
			if obj.isInBlock(self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2):
				self.smoke()

	def checkForCollision(self):
		for obj in self.objectList:
			self.collisionDetection(obj)

		for rabbit in self.rabbitList:
			self.collisionDetection(rabbit, True)

	def getAnim(self):
		return self.carrotAnim

	def smoke(self):
		self.smoked = True
		self.rect.x -= 25
		self.rect.y -= 25
		self.rect.w = 75
		self.rect.h = 75
		self.carrotAnim = Animation("carrot_smoke", 25)
		self.carrotAnim.setFrameRange(1, 25);
		self.carrotAnim.setRect(self.rect)
		self.sprite = pygame.sprite.RenderPlain(self.carrotAnim)
		self.carrotAnim.playAnim(False)