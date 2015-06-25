#!/usr/bin/python

import socket

class Client():
	def __init__(self, host):
		self.host = host
		self.port = 12800

		self.connectServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.connectServer.connect((self.host, self.port))

	def send(self, msg):
		self.connectServer.send(msg)

	def recieve(self, buff):
		msg = self.connectServer.recv(1024)
		# print msg
		return msg

	def close(self):
		self.connectServer.close()