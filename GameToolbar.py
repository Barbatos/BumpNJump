#!/usr/bin/python

import pygame
from pygame.locals import *

class GameToolbar():
	def __init__(self):
		self.screen = pygame.display.get_surface()
		self.rect = pygame.Rect(self.screen.get_rect().w - 200, 0, 200, self.screen.get_rect().h)
	
	def update(self, rabbit1 = None, rabbit2 = None):
		pygame.draw.rect(self.screen, (50, 50, 50), self.rect)

		pygame.draw.line(self.screen, (150, 150, 150), (self.screen.get_rect().w - 200, self.screen.get_rect().h/2 - 1), (self.screen.get_rect().w, self.screen.get_rect().h/2 - 1), 2)
		pygame.draw.line(self.screen, (100, 100, 100), (self.screen.get_rect().w - 200, self.screen.get_rect().h/2 + 1), (self.screen.get_rect().w, self.screen.get_rect().h/2 + 1), 2)

		if pygame.font:
			font = pygame.font.Font(None, 36)

			rabbit1Points = font.render(rabbit1.getName().capitalize() + " : " + str(rabbit1.getPoints()), 1, (220, 220, 220))
			rabbit1Carrots = font.render(str(rabbit1.getCarrots()) + "x", 1, (220, 220, 220))

			rabbit2Points = font.render(rabbit2.getName().capitalize() + " : " + str(rabbit2.getPoints()), 1, (220, 220, 220))
			rabbit2Carrots = font.render(str(rabbit2.getCarrots()) + "x", 1, (220, 220, 220))

			rabbit1PointsPos = rabbit1Points.get_rect(x = self.rect.x + 20, y = 20)
			rabbit1CarrotsPos = rabbit1Points.get_rect(x = self.rect.x + 25, y = 60)
			rabbit2PointsPos = rabbit1Points.get_rect(x = self.rect.x + 20, y = self.rect.h/2 + 20)
			rabbit2CarrotsPos = rabbit1Points.get_rect(x = self.rect.x + 25, y = self.rect.h/2 + 60)

			self.screen.blit(rabbit1Points, rabbit1PointsPos)
			self.screen.blit(rabbit1Carrots, rabbit1CarrotsPos)
			self.screen.blit(rabbit2Points, rabbit2PointsPos)
			self.screen.blit(rabbit2Carrots, rabbit2CarrotsPos)

	def getX(self):
		return self.sliderRect.x

	def getY(self):
		return self.sliderRect.y

	def getWidth(self):
		return self.sliderRect.w

	def getValue(self):
		return self.value
		