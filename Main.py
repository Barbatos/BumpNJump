#!/usr/bin/python

import sys
import os
import math
import random
import pygame
from pygame.locals import *
from Rabbit import *
from Animation import *

class Main():
	def main():
		pygame.init()
		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		background = pygame.Surface(screen.get_size())
		background = background.convert()
		background.fill((100, 150, 100))

		rabbit = Rabbit(1, "john")

		rabbitSprite = pygame.sprite.RenderPlain(rabbit)

		screen.blit(background, (0, 0))
		pygame.display.flip()

		testAnim = Animation("anim", 19, 60)
		testAnimSprite = pygame.sprite.RenderPlain(testAnim)
		testAnim.playAnim()

		clock = pygame.time.Clock()

		while 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					return

				elif event.type == KEYDOWN:
					if event.key == K_UP:
						rabbit.jump()
					if event.key == K_LEFT:
						rabbit.moveLeftStart()
					if event.key == K_RIGHT:
						rabbit.moveRightStart()
					if event.key == K_p:
						if testAnim.isRunning():
							testAnim.stopAnim()
						else:
							testAnim.playAnim()

				elif event.type == KEYUP:
					if event.key == K_LEFT:
						rabbit.moveLeftStop()
					if event.key == K_RIGHT:
						rabbit.moveRightStop()

			screen.blit(background, testAnim.rect, testAnim.rect)
			screen.blit(background, rabbit.rect, rabbit.rect)

			rabbitSprite.update()
			rabbitSprite.draw(screen)
			testAnimSprite.update()
			testAnimSprite.draw(screen)

			testAnim.update()

			pygame.display.flip()

			clock.tick(60)

	if __name__ == '__main__': main()