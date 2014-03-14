#!/usr/bin/python

import sys
import os
import math
import random
import pygame
import MainMenu
from pygame.locals import *
from Object import *
from Resources import *
from Map import *
from PauseEditorMenu import *

class Editor():
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.backgroundImage, self.backgroundRect = loadPNG("background.png")

		self.blockList = [Object(type = "earth"), Object(type = "boing"), Object(type = "ice")]

		self.currentBlockNumber = 0
		self.currentBlock = self.blockList[self.currentBlockNumber]
		self.currentSpriteBlock = pygame.sprite.RenderPlain(self.currentBlock)

		self.grid = False

		self.level = Map(True)

		self.active = True

		self.pauseMenu = PauseEditorMenu()
		
		pygame.display.flip()

	def update(self):
		key = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()

		if self.active:
			pygame.mouse.set_cursor(*pygame.cursors.arrow)
			
			for event in pygame.event.get():
				mse = pygame.mouse.get_pos()
				self.currentBlock.rect.topleft = ((int(mse[0]) / 50)*50, (int(mse[1]) / 50)*50)

				if event.type == QUIT or (key[K_F4] and key[K_LALT]):
					return False, self

				elif key[K_LCTRL] and key[K_s]:
					self.level.save("test")

				elif key[K_LCTRL] and key[K_l]:
					self.level.load("test")

				elif event.type == MOUSEBUTTONDOWN:
					if event.button == 5:
						self.currentBlockNumber = (self.currentBlockNumber - 1) % len(self.blockList)
					if event.button == 4:
						self.currentBlockNumber = (self.currentBlockNumber + 1) % len(self.blockList)
					if event.button == 3:
						self.level.removeObjectFromPos(mse)
					if event.button == 1:
						if not any(obj.rect.collidepoint(mse) for obj in self.level.objectList):
							if self.currentBlock.getType() == "boing":
								if self.level.objectFromPos((mse[0], mse[1] + 50)).getType() != "boing":
									if not self.level.isInBlock(mse[0], mse[1] - 50):
										self.level.addObject(self.currentBlock.rect.x, self.currentBlock.rect.y, self.currentBlock.getType())
							else:
								if self.level.objectFromPos((mse[0], mse[1] + 50)).getType() != "boing":
									self.level.addObject(self.currentBlock.rect.x, self.currentBlock.rect.y, self.currentBlock.getType())

					self.currentBlock = self.blockList[self.currentBlockNumber]
					self.currentSpriteBlock = pygame.sprite.RenderPlain(self.currentBlock)
					self.currentBlock.rect.topleft = ((int(mse[0]) / 50)*50, (int(mse[1]) / 50)*50)

				elif event.type == MOUSEMOTION:
					if mouse[0]:
						if not any(obj.rect.collidepoint(mse) for obj in self.level.objectList):
							if self.currentBlock.getType() == "boing":
								if self.level.objectFromPos((mse[0], mse[1] + 50)).getType() != "boing":
									if not self.level.isInBlock(mse[0], mse[1] - 50):
										self.level.addObject(self.currentBlock.rect.x, self.currentBlock.rect.y, self.currentBlock.getType())
							else:
								if self.level.objectFromPos((mse[0], mse[1] + 50)).getType() != "boing":
									self.level.addObject(self.currentBlock.rect.x, self.currentBlock.rect.y, self.currentBlock.getType())

					elif mouse[2]:
						self.level.removeObjectFromPos(mse)
						self.level.updateFloor()

				elif event.type == KEYDOWN:
					if event.key == K_g:
						if self.grid:
							self.grid = False
						else:
							self.grid = True

					elif event.key == K_ESCAPE:
						self.active = False

			self.screen.blit(self.backgroundImage, self.backgroundRect, self.backgroundRect)

			self.level.update(self.screen)

			self.currentBlock.update()
			self.currentSpriteBlock.draw(self.screen)

			if self.grid:
				self.drawGrid()

		else:
			for event in pygame.event.get():
				if event.type == QUIT or (key[K_F4] and key[K_LALT]):
					return False, self

				elif event.type == MOUSEBUTTONDOWN:
					mse = pygame.mouse.get_pos()

					if self.pauseMenu.buttons["resume"].onButton(mse):
						self.active = True

					elif self.pauseMenu.buttons["save"].onButton(mse):
						self.active = True
						self.level.save("test")

					elif self.pauseMenu.buttons["load"].onButton(mse):
						self.active = True
						self.level.load("test")

					elif self.pauseMenu.buttons["mainMenu"].onButton(mse):
						return True, MainMenu.MainMenu()

				elif event.type == MOUSEMOTION:
					mse = pygame.mouse.get_pos()

					pygame.mouse.set_cursor(*pygame.cursors.arrow)

					for button in self.pauseMenu.buttons.values():
						if button.onButton(mse):
							pygame.mouse.set_cursor(*pygame.cursors.tri_left)

				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.active = True

			self.pauseMenu.update()

		pygame.display.update()

		return True, self

	def drawGrid(self):
		for i in range(50, self.screen.get_height(), 50):
			pygame.draw.line(self.screen, (5, 5, 5), (0, i - 1), (self.screen.get_width(), i - 1))
		for j in range(50, self.screen.get_width(), 50):
			pygame.draw.line(self.screen, (5, 5, 5), (j - 1, 0), (j - 1, self.screen.get_height()))