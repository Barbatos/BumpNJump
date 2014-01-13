#!/usr/bin/python

class Rabbit():
	def __init__(self, id = -1, name = ""):
		self.id = id
		self.name = name

	def __repr__(self):
		print("Rabbit " + self.id + ": " + self.name)

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def setId(self, id):
		self.id = id

	def setName(self):
		self.name = name