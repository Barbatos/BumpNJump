#!/usr/bin/python

import socket

class Server():
	def __init__(self, host):
		self.host = host
		self.port = 12800

		self.connectClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.connectClient.bind((self.host, self.port))
		self.connectClient.listen(5)

	def accept(self):
		self.connectClient, infosClient = self.connectClient.accept()

	def send(self, msg):
		self.connectClient.send(msg)

	def recieve(self, buff = 1024):
		msg = self.connectClient.recv(buff)
		# print msg
		return msg

	def close(self):
		self.connectClient.close()