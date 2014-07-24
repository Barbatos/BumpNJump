#!/usr/bin/python

import socket

class Client():
	def __init__(self, hote):
		self.hote = hote
		self.port = 12800

		self.connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.connexion_avec_serveur.connect((self.hote, self.port))
		print("Connexion etablie avec le serveur sur le port " + str(self.port))

	def beginCom(self):
		msg = b""
		while msg != b"fin":
			msg = raw_input("> ")
			self.connexion_avec_serveur.send(msg.encode())

		self.finish()

	def finish(self):
		print("Fermeture de la connexion")
		self.connexion_avec_serveur.close()