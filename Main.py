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

		test = Rabbit(1, "john")

		testSprite = pygame.sprite.RenderPlain(test)

		screen.blit(background, (0, 0))
		pygame.display.flip()

		clock = pygame.time.Clock()

		while 1:
			clock.tick(60)

			for event in pygame.event.get():
				if event.type == QUIT:
					return

			testSprite.update()
			testSprite.draw(screen)
			pygame.display.flip()

	if __name__ == '__main__': main()