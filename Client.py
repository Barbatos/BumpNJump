#!/usr/bin/python

import socket

class Client():
	def __init__(self, hote):
		self.hote = hote
		self.port = 12800

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def send(self, msg):
		self.sock.sendto(msg, (self.hote, self.port))

	def recieve(self):
		msg, addr = self.sock.recvfrom(1024)
		print(msg)