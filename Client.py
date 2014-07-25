#!/usr/bin/python

import socket

class Client():
	def __init__(self, hote):
		self.hote = hote
		self.port = 12800

		self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.server_connection.connect((self.hote, self.port))
		print("Connexion etablie avec le serveur sur le port " + str(self.port))

	def send(self, msg):
		send_msg = msg.encode()
		self.server_connection.send(send_msg)

	def recieve(self):
		rcv_msg = self.server_connection.recv(1024)
		print(rcv_msg.decode())

	def finish(self):
		print("Fermeture de la connexion")
		self.server_connection.close()