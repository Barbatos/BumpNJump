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
		screen = pygame.display.set_mode((1200, 675))
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

		clock = pygame.time.Clock()

		while 1:
			clock.tick(60)

			testAnim.update()

			for event in pygame.event.get():
				if event.type == QUIT:
					return

				elif event.type == KEYDOWN:
					if event.key == K_UP:
						rabbit.moveUp()
						testAnim.playAnim()
					if event.key == K_DOWN:
						rabbit.moveDown()
						testAnim.playAnim()
					if event.key == K_LEFT:
						rabbit.moveLeft()
						testAnim.playAnim()
					if event.key == K_RIGHT:
						rabbit.moveRight()
						testAnim.playAnim()

				elif event.type == KEYUP:
					if event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
						testAnim.stopAnim()
						rabbit.standStill()

			screen.blit(background, testAnim.rect, testAnim.rect)
			screen.blit(background, rabbit.rect, rabbit.rect)
			rabbitSprite.update()
			rabbitSprite.draw(screen)
			testAnimSprite.update()
			testAnimSprite.draw(screen)

			pygame.display.flip()

	if __name__ == '__main__': main()