#!/usr/bin/python

import sys
import os
import math
import random
import pygame
import MainMenu
import Resources
import struct
from pygame.locals import *
from Rabbit import *
from Butterfly import *
from Animation import *
from Object import *
from Resources import *
from PauseGameMenu import *
from Map import *
from GameToolbar import *

class MultiServerGame():
	pygame.mixer.pre_init(44100, -16, 2, 1024)
	pygame.mixer.init()

	def __init__(self, server, color, levelPreset = "empty"):
		self.server = server

		self.butterflies = []

		self.screen = pygame.display.get_surface()

		self.backgroundImage, self.backgroundRect = loadPNG("background.png")

		self.buttonSound = pygame.mixer.Sound("resources/sound/button.wav")
		self.buttonSound.set_volume(float(Resources.getOptionValue("sound"))/100)

		self.active = True

		if levelPreset == "empty":
			self.level = Map()
		else:
			self.level = Map(True)

		self.toolbar = GameToolbar()

		self.regis = Rabbit(1, "regis" , color, self.level.objectList, self.level.objectSpritesList)

		self.server.accept()
		self.server.send(b"connexion avec client : OK")
		msg = self.server.recieve()

		mapStr = self.level.getMapStr()

		#MAP STRING SEND
		self.server.send(struct.pack(str(len(mapStr)) + "s", mapStr))

		#SERVER RABBIT COLOR SEND
		self.server.send(struct.pack("iii", self.regis.color[0], self.regis.color[1], self.regis.color[2]))

		#CLIENT RABBIT COLOR RECIEVE
		clientCol = self.server.recieve()
		clientCol = struct.unpack("iii", clientCol)

		#CREATE CLIENT RABBIT
		self.john = Rabbit(2, "john" , clientCol, self.level.objectList, self.level.objectSpritesList, True)

		self.regis.appendRabbit(self.john)
		self.john.appendRabbit(self.regis)

	 	self.pauseMenu = PauseGameMenu()

		self.deltaCarrot = 0
		self.timeCarrot = random.randint(1, 4)

	# 	for l in range(0, 6):
	# 		while True:
	# 			randPos = random.randint(0, 16)
	# 			if not self.level.isInBlock(self.level.objectList[randPos].getX() + 10, self.level.objectList[randPos].getY() - 26):
	# 				break

	# 		butterfly = Butterfly(self.level.objectList[randPos].getX() + 10, self.level.objectList[randPos].getY() - 26, (255, 10, 100), self.level.objectList, self.level.objectSpritesList)
	# 		self.butterflies.append(butterfly)

	 	pygame.display.flip()

	def update(self):
	 	key = pygame.key.get_pressed()

	 	if self.active:
	 		pygame.mouse.set_visible(0)

	 		for event in pygame.event.get():
	 			if event.type == QUIT or (key[K_F4] and key[K_LALT]):
	 				self.server.close()
	 				return False, self

				elif event.type == KEYDOWN:
					if event.key == K_UP:
						self.regis.jump()
					if event.key == K_LEFT:
						self.regis.moveLeftStart()
					if event.key == K_RIGHT:
						self.regis.moveRightStart()
					if event.key == K_KP0:
						self.regis.throwCarrot()

				elif event.type == KEYUP:
					if event.key == K_LEFT:
						self.regis.moveLeftStop()
					if event.key == K_RIGHT:
						self.regis.moveRightStop()

	# 			#IF A RABBIT IS TOUCHED
	# 			elif event.type == USEREVENT + 1:
	# 				print "touche"
	# 				if self.john.isTouched():
	# 					self.john.moveLeftStop()
	# 					self.john.moveRightStop()

	# 				elif self.regis.isTouched():
	# 					self.regis.moveLeftStop()
	# 					self.regis.moveRightStop()

	# 			elif event.type == USEREVENT + 2:
	# 				print "plus touche"

			self.screen.blit(self.backgroundImage, self.backgroundRect, self.backgroundRect)

			#SERVER RABBIT POSITION SEND
			self.server.send(struct.pack("ii", self.regis.rect.x, self.regis.rect.y))

			#CLIENT RABBIT POSITION RECIEVE
			johnPos = self.server.recieve()
			johnPos = struct.unpack("ii", johnPos)
			self.john.rect.x = johnPos[0]
			self.john.rect.y = johnPos[1]

			#LEVEL UPDATE
			self.level.update()

			#RABBITS UPDATE
			self.john.update()
			self.regis.update()

			#TOOLBAR UPDATE
			self.toolbar.update(self.john, self.regis)

			#BUTTERFLIES UPDATE
			for b in self.butterflies:
				b.update()

			#NEW CARROTS
			if(self.deltaCarrot == self.timeCarrot * 3600):
				self.level.addCarrot()
				self.deltaCarrot = 0
				self.timeCarrot = random.randint(1, 4)
			else:
				self.deltaCarrot += 1

	# 	else:
	# 		pygame.mouse.set_visible(1)

	# 		for event in pygame.event.get():
	# 			if event.type == QUIT or (key[K_F4] and key[K_LALT]):
	# 				return False, self

	# 			elif event.type == MOUSEBUTTONDOWN:
	# 				mse = pygame.mouse.get_pos()

	# 				if self.pauseMenu.buttons["resume"].onButton(mse):
	# 					self.buttonSound.play()
	# 					self.active = True

	# 				elif self.pauseMenu.buttons["loadlevel"].onButton(mse):
	# 					self.buttonSound.play()
	# 					print "okay"

	# 				elif self.pauseMenu.buttons["mainMenu"].onButton(mse):
	# 					self.buttonSound.play()
	# 					return True, MainMenu.MainMenu()


	# 			elif event.type == MOUSEMOTION:
	# 				mse = pygame.mouse.get_pos()

	# 				pygame.mouse.set_cursor(*pygame.cursors.arrow)

	# 				for button in self.pauseMenu.buttons.values():
	# 					if button.onButton(mse):
	# 						pygame.mouse.set_cursor(*pygame.cursors.tri_left)

	# 			elif event.type == KEYDOWN:
	# 				if event.key == K_ESCAPE:
	# 					self.active = True

	# 		self.pauseMenu.update()

		pygame.display.update()

		return True, self