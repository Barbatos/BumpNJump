#!/usr/bin/python

import sys
import os
import math
import random
import pygame
import pickle
from pygame.locals import *
from Object import *
from Resources import *
from Map import *

class Editor():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		# self.music = pygame.mixer.Sound("resources/sound/music.wav")
		# self.music.play(-1)

		backgroundImage, backgroundRect = loadPNG("background.png")

		blockList = [Object(type = "earth"), Object(type = "boing"), Object(type = "ice")]

		currentBlockNumber = 0
		currentBlock = blockList[currentBlockNumber]
		currentSpriteBlock = pygame.sprite.RenderPlain(currentBlock)

		grid = False

		self.level = Map(True)

		clock = pygame.time.Clock()
		
		pygame.display.flip()

		while 1:
			key = pygame.key.get_pressed()
			mouse = pygame.mouse.get_pressed()
			for event in pygame.event.get():
				mse = pygame.mouse.get_pos()
				currentBlock.rect.topleft = ((int(mse[0]) / 50)*50, (int(mse[1]) / 50)*50)

				if event.type == QUIT or (key[K_F4] and key[K_LALT]):
					return

				elif event.type == MOUSEBUTTONDOWN:
					if event.button == 5:
						currentBlockNumber = (currentBlockNumber - 1) % len(blockList)
					if event.button == 4:
						currentBlockNumber = (currentBlockNumber + 1) % len(blockList)
					if event.button == 3:
						self.level.removeObjectFromPos(mse)
					if event.button == 1:
						if not any(obj.rect.collidepoint(mse) for obj in self.level.objectList):
							if self.level.objectFromPos((mse[0], mse[1] + 50)).getType() != "boing" and self.level.objectFromPos((mse[0], mse[1] - 50)).getType() != "boing":
								self.level.addObject(currentBlock.rect.x, currentBlock.rect.y, currentBlock.getType())

					currentBlock = blockList[currentBlockNumber]
					currentSpriteBlock = pygame.sprite.RenderPlain(currentBlock)
					currentBlock.rect.topleft = ((int(mse[0]) / 50)*50, (int(mse[1]) / 50)*50)

					self.level.updateFloor()

				elif event.type == MOUSEMOTION:
					if mouse[0]:
						if not any(obj.rect.collidepoint(mse) for obj in self.level.objectList):
							if self.level.objectFromPos((mse[0], mse[1] + 50)).getType() != "boing" and self.level.objectFromPos((mse[0], mse[1] - 50)).getType() != "boing":
								self.level.addObject(currentBlock.rect.x, currentBlock.rect.y, currentBlock.getType())
								self.level.updateFloor()

					elif mouse[2]:
						self.level.removeObjectFromPos(mse)
						self.level.updateFloor()

				elif event.type == KEYDOWN:
					if event.key == K_g:
						if grid:
							grid = False
						else:
							grid = True

			self.screen.blit(backgroundImage, backgroundRect, backgroundRect)

			self.level.update(self.screen)

			currentBlock.update()
			currentSpriteBlock.draw(self.screen)

			if grid:
				self.drawGrid()

			pygame.display.update()

			clock.tick(60)

	def drawGrid(self):
		for i in range(50, self.screen.get_height(), 50):
			pygame.draw.line(self.screen, (5, 5, 5), (0, i - 1), (self.screen.get_width(), i - 1))
		for j in range(50, self.screen.get_width(), 50):
			pygame.draw.line(self.screen, (5, 5, 5), (j - 1, 0), (j - 1, self.screen.get_height()))

if __name__ == '__main__': 
	Editor()
	