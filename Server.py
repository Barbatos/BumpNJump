#!/usr/bin/python

import socket

class Server():
	def __init__(self, hote):
		self.hote = hote
		self.port = 12800

		self.connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connexion_principale.bind((self.hote, self.port))
		self.connexion_principale.listen(5)

		self.connexion_avec_client = None
		self.infos_connexion = None

	def connect(self):
		print("Le serveur ecoute a present sur le port " + str(self.port))
		self.connexion_avec_client, self.infos_connexion = self.connexion_principale.accept()

	def beginCom(self):
		msg = b""
		while msg != b"end":
			msg = self.connexion_avec_client.recv(1024)
			print(msg.decode())

		self.finish()

	def finish(self):
		print("Fermeture de la connexion")
		self.connexion_avec_client.close()
		self.connexion_principale.close()