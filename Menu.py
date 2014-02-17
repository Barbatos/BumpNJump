#!/usr/bin/python

import pygame
from Main import *
from Button import *
from pygame.locals import *

class Menu():
	def __init__(self):
		pygame.init()

		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Menu")

		background = pygame.Surface(screen.get_size())
		background = background.convert()
		background.fill((50, 50, 50))

		playButton = Button(screen, screen.get_width()/2 - 200/2, 100, 200, 40, "PLAY")

		optionButton = Button(screen, screen.get_width()/2 - 200/2, 250, 200, 40, "OPTION")

		quitButton = Button(screen, screen.get_width()/2 - 200/2, 400, 200, 40, "QUIT")

		clock = pygame.time.Clock()

		pygame.display.flip()

		while 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					return

				elif event.type == MOUSEBUTTONDOWN:
					mse = pygame.mouse.get_pos()
					if playButton.onButton(mse):
						print playButton.getText()
						BumpNJump()

					elif optionButton.onButton(mse):
						print optionButton.getText()

					elif quitButton.onButton(mse):
						return

			playButton.update()
			optionButton.update()
			quitButton.update()

			pygame.display.update()

			clock.tick(60)

if __name__ == '__main__':
	Menu()