#!/usr/bin/python

import pygame
import Resources
import random
from Object import *

class Map():
	def __init__(self, empty = False):
		self.objectList = []
		self.objectSpritesList = pygame.sprite.Group()
		self.screen = pygame.display.get_surface()

		if not empty:
			for i in range(0, 16):
				objType = random.randint(1, 2)

				if objType == 1:
					self.objectList.append(Object(len(self.objectList), i * 50, 550, "earth"))
				elif objType == 2:
					self.objectList.append(Object(len(self.objectList), i * 50, 550, "ice"))
				# else:
				# 	self.objectList.append(Object(len(self.objectList), i * 50, 550, "boing"))

			# for j in range(0, 30):
			# 	objType = random.randint(1, 2)

			# 	while True:
			# 		randPosX = random.randint(0, 15) * 50 
			# 		randPosY = random.randint(1, 10) * 50
			# 		if not self.isInBlock(randPosX + 10, randPosY + 10):
			# 			break

			# 	if objType == 1:
			# 		self.objectList.append(Object(len(self.objectList), randPosX, randPosY, "earth"))
			# 	else:
			# 		self.objectList.append(Object(len(self.objectList), randPosX, randPosY, "ice"))

			for k in range(0, 5):
				while True:
					randPos = random.randint(0, len(self.objectList) - 1)
					if not self.isInBlock(self.objectList[randPos].getX() + 10, self.objectList[randPos].getY() - 26):
						break

				if self.objectList[randPos].getType() != "carrot":
					self.objectList.append(Object(len(self.objectList), self.objectList[randPos].getX() + 10, self.objectList[randPos].getY() - 26, "carrot"))

			for obj in self.objectList:
				if not self.isFloor(obj):
					obj.replaceImage(obj.getType())

				self.objectSpritesList.add(pygame.sprite.RenderPlain(obj))

			self.save("tempServer")

	def update(self):
		self.objectSpritesList.update()
		self.objectSpritesList.draw(self.screen)

		pygame.event.pump()

	def updateFloor(self):
		for obj in self.objectList:
			if not self.isFloor(obj):
				if obj.getType() == "boing":
					obj.replaceImage("earth")
				else:
					obj.replaceImage(obj.getType())

			else:
				obj.replaceImage(obj.getType(), True)

			self.objectSpritesList.add(pygame.sprite.RenderPlain(obj))

	def addObject(self, x, y, type):
		self.objectList.append(Object(len(self.objectList), x, y, type))
		self.objectSpritesList.add(pygame.sprite.RenderPlain(self.objectList[-1]))
		self.updateFloor()

	def removeObject(self, obj):
		self.objectSpritesList.remove(obj)
		self.objectList.remove(obj)
		self.updateFloor()

	def removeObjectFromPos(self, (x, y)):
		for obj in self.objectList:
			if obj.isInBlock(x, y):
				self.objectSpritesList.remove(obj)
				self.objectList.remove(obj)

		self.updateFloor()

	def getObjectFromPos(self, (x, y)):
		for obj in self.objectList:
			if obj.isInBlock(x, y):
				return obj

		return Object(type = "empty")

	def isInBlock(self, x, y):
		for obj in self.objectList:
			if obj.isInBlock(x, y):
				return True

		return False

	def isFloor(self, object):
		if self.isInBlock(object.getX() + 5, object.getY() - 5):
			return False

		return True

	def getObjectList(self):
		return self.objectList

	def setObjectList(self, objectList):
		self.objectList = objectList

		for obj in self.objectList:
			self.objectSpritesList.add(pygame.sprite.RenderPlain(obj))

	def addCarrot(self):
		while True:
			randPos = random.randint(0, len(self.objectList) - 1)
			if not self.isInBlock(self.objectList[randPos].getX() + 10, self.objectList[randPos].getY() - 26):
				break

		if self.objectList[randPos].getType() != "carrot":
			self.objectList.append(Object(len(self.objectList), self.objectList[randPos].getX() + 10, self.objectList[randPos].getY() - 26, "carrot"))

		for obj in self.objectList:
			if not self.isFloor(obj):
				obj.replaceImage(obj.getType())

			self.objectSpritesList.add(pygame.sprite.RenderPlain(obj))

	def save(self, name):
		with open("save/maps/" + name + ".mabbit", "w") as f:
			for obj in self.objectList:
				f.write(obj.getType() + ":" + str(obj.getX()) + ", " + str(obj.getY()) + "\n")

	def saveFromStr(self, name, string):
		with open("save/maps/" + name + ".mabbit", "w") as f:
			f.write(string)

	def load(self, name):
		self.objectList = []
		self.objectSpritesList = pygame.sprite.Group()

		with open("save/maps/" + name + ".mabbit", "r") as f:
			for line in f:
				line = line.strip("\n")

				self.objectList.append(Object(len(self.objectList), int(line.split(":")[1].split(",")[0]), int(line.split(":")[1].split(",")[1]), line.split(":")[0]))

		for obj in self.objectList:
			self.objectSpritesList.add(pygame.sprite.RenderPlain(obj))

		self.updateFloor()

	def getMapStr(self):
		mapStr = ""
		for obj in self.objectList:
			mapStr = mapStr + obj.getType() + ":" + str(obj.getX()) + ", " + str(obj.getY()) + "\n"

		return mapStr