#!/usr/bin/python

import sys
import os
import math
import random
import pygame
from pygame.locals import *
from Rabbit import *

class Main():
	def main():
		pygame.init()
		screen = pygame.display.set_mode((1200, 675))
		pygame.display.set_caption("Bump'N'Jump")

		background = pygame.Surface(screen.get_size())
		background = background.convert()
		background.fill((100, 150, 100))

		rabbit = Rabbit(1, "john")

		rabbitSprite = pygame.sprite.RenderPlain(rabbit)

		screen.blit(background, (0, 0))
		pygame.display.flip()

		clock = pygame.time.Clock()

		while 1:
			clock.tick(60)

			for event in pygame.event.get():
				if event.type == QUIT:
					return

				elif event.type == KEYDOWN:
					if event.key == K_UP:
						rabbit.moveUp()
					if event.key == K_DOWN:
						rabbit.moveDown()
					if event.key == K_LEFT:
						rabbit.moveLeft()
					if event.key == K_RIGHT:
						rabbit.moveRight()

				elif event.type == KEYUP:
					if event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
						rabbit.standStill()

			screen.blit(background, rabbit.rect, rabbit.rect)
			rabbitSprite.update()
			rabbitSprite.draw(screen)

			pygame.display.flip()

	if __name__ == '__main__': main()