#!/usr/bin/python

import pygame
from Main import *
from Button import *
from Slider import *
from Checkbox import *
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

		editorButton = Button(screen, screen.get_width()/2 - 200/2, 200, 200, 40, "EDITOR")

		optionButton = Button(screen, screen.get_width()/2 - 200/2, 300, 200, 40, "OPTION")

		quitButton = Button(screen, screen.get_width()/2 - 200/2, 400, 200, 40, "QUIT")

		sliderTest = Slider(screen, 50, 50, 200, 100)

		checkboxTest = Checkbox(screen, 50, 100, "test")

		clock = pygame.time.Clock()

		print str(screen.get_rect())

		pygame.display.flip()

		while 1:
			mouse = pygame.mouse.get_pressed()
			for event in pygame.event.get():
				if event.type == QUIT:
					return

				elif event.type == MOUSEBUTTONDOWN:
					mse = pygame.mouse.get_pos()
					if playButton.onButton(mse):
						BumpNJump()

					elif editorButton.onButton(mse):
						print editorButton.getText()

					elif optionButton.onButton(mse):
						print optionButton.getText()

					elif quitButton.onButton(mse):
						return

					elif sliderTest.onSlider(mse):
						sliderTest.setValue(mse[0])

					elif checkboxTest.onCheckbox(mse):
						checkboxTest.changeState()

				if event.type == MOUSEMOTION:
					mse = pygame.mouse.get_pos()
					if sliderTest.onSlider(mse) and mouse[0]:
						sliderTest.setValue(mse[0])

			screen.blit(background, background.get_rect(), background.get_rect())

			playButton.update()
			editorButton.update()
			optionButton.update()
			quitButton.update()

			sliderTest.update()

			checkboxTest.update()

			pygame.display.update()

			clock.tick(60)

if __name__ == '__main__':
	Menu()