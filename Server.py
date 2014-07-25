#!/usr/bin/python

import socket

class Server():
	def __init__(self, hote):
		self.hote = hote
		self.port = 12800

		self.main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.main_connection.bind((self.hote, self.port))
		self.main_connection.listen(5)

		self.client_connection = None
		self.connection_data = None

	def connect(self):
		print("Le serveur ecoute a present sur le port " + str(self.port))
		self.client_connection, self.connection_data = self.main_connection.accept()

	def send(self, msg):
		send_msg = msg.encode()
		self.client_connection.send(send_msg)

	def recieve(self):
		rcv_msg = self.client_connection.recv(1024)
		print(rcv_msg.decode())

	def finish(self):
		print("Fermeture de la connexion")
		self.client_connection.close()
		self.main_connection.close()