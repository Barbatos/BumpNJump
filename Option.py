#!/usr/bin/python

import pygame
from Button import *
from Slider import *
from Checkbox import *
from pygame.locals import *

class Option():
	def __init__(self):
		pygame.init()

		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Menu")

		if pygame.font:
			font = pygame.font.Font(None, 22)

		background = pygame.Surface(screen.get_size())
		background = background.convert()
		background.fill((50, 50, 50))

		musicSlider = Slider(screen, screen.get_width()/2 - 200/2, 100, 200, 100)
		soundSlider = Slider(screen, screen.get_width()/2 - 200/2, 200, 200, 100)

		returnButton = Button(screen, screen.get_width()/2 - 200/2, 400, 200, 40, "RETURN")

		clock = pygame.time.Clock()

		pygame.display.flip()

		while 1:
			mouse = pygame.mouse.get_pressed()
			for event in pygame.event.get():
				if event.type == QUIT:
					return

				elif event.type == MOUSEBUTTONDOWN:
					mse = pygame.mouse.get_pos()
					if musicSlider.onSlider(mse):
						musicSlider.setValue(mse[0])

					elif soundSlider.onSlider(mse):
						soundSlider.setValue(mse[0])

					elif returnButton.onButton(mse):
						print returnButton.getText()

				elif event.type == MOUSEMOTION:
					mse = pygame.mouse.get_pos()
					if musicSlider.onSlider(mse) and mouse[0]:
						musicSlider.setValue(mse[0])

					elif soundSlider.onSlider(mse) and mouse[0]:
						soundSlider.setValue(mse[0])

			screen.blit(background, background.get_rect(), background.get_rect())

			if pygame.font:
				self.textDisp = font.render("Music volume", 1, (100, 100, 100))

			self.textRect = self.textDisp.get_rect(centerx = screen.get_width()/2, y = musicSlider.getY() - 25)
			screen.blit(self.textDisp, self.textRect)

			musicSlider.update()

			if pygame.font:
				self.textDisp = font.render("Sound volume", 1, (100, 100, 100))

			self.textRect = self.textDisp.get_rect(centerx = screen.get_width()/2, y = soundSlider.getY() - 25)
			screen.blit(self.textDisp, self.textRect)

			soundSlider.update()

			returnButton.update()

			pygame.display.update()

			clock.tick(60)

if __name__ == '__main__':
	Option()