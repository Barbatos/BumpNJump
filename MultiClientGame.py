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
from Client import *

class MultiClientGame():
	pygame.mixer.pre_init(44100, -16, 2, 1024)
	pygame.mixer.init()

	def __init__(self, color):
		self.butterflies = []

		self.screen = pygame.display.get_surface()

		self.backgroundImage, self.backgroundRect = loadPNG("background.png")

		self.buttonSound = pygame.mixer.Sound("resources/sound/button.wav")
		self.buttonSound.set_volume(float(Resources.getOptionValue("sound"))/100)

		self.active = True

		self.level = Map(True)

		self.toolbar = GameToolbar()

		self.client = Client('localhost')
		self.client.connect()
		self.client.recieve()
		self.client.send(b"connexion avec serveur : OK")

		#MAP STRING RECIEVE
		mapStr = self.client.recieve(4096)
		mapStr = struct.unpack(str(len(mapStr)) + "s", mapStr)[0]

		#LOAD MAP FROM STRING
		self.level.saveFromStr("tempClient", mapStr)
		self.level.load("tempClient")

		#CREATE CLIENT RABBIT
		self.regis = Rabbit(1, "regis" , color, self.level.objectList, self.level.objectSpritesList)

		#SERVER RABBIT COLOR RECIEVE
		serverCol = self.client.recieve()
		serverCol = struct.unpack("iii", serverCol)

		#CLIENT RABBIT COLOR SEND
		self.client.send(struct.pack("iii", self.regis.color[0], self.regis.color[1], self.regis.color[2]))

		#CREATE SERVER RABBIT
	 	self.john = Rabbit(2, "john" , serverCol, self.level.objectList, self.level.objectSpritesList, True)

		self.regis.appendRabbit(self.john)
	 	self.john.appendRabbit(self.regis)

	 	self.pauseMenu = PauseGameMenu()

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

			#SERVER RABBIT POSITION RECIEVE
			johnPos = self.client.recieve()
			johnPos = struct.unpack("ii", johnPos)
			self.john.rect.x = johnPos[0]
			self.john.rect.y = johnPos[1]

			#CLIENT RABBIT POSITION SEND
			self.client.send(struct.pack("ii", self.regis.rect.x, self.regis.rect.y))

			self.screen.blit(self.backgroundImage, self.backgroundRect, self.backgroundRect)

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