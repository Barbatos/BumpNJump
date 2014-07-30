#!/usr/bin/python

import socket

class Server():
	def __init__(self, hote):
		self.hote = hote
		self.port = 12800

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def connect(self):
		self.sock.bind((self.hote, self.port))

	def send(self, msg):
		self.sock.sendto(msg, (self.hote, self.port))

	def recieve(self):
		msg, addr = self.sock.recvfrom(1024)
		print(msg)