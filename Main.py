#!/usr/bin/python

import sys
import os
import math
import random
import pygame
from pygame.locals import *
from Rabbit import *
from Animation import *
from Object import *
from Resources import *
from Map import *

class BumpNJump():
	def __init__(self):
		pygame.init()
		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Bump'N'Jump")

		# self.music = pygame.mixer.Sound("resources/sound/music.wav")
		# self.music.play(-1)

		backgroundImage, backgroundRect = loadPNG("background.png")

		background = pygame.Surface(screen.get_size())
		background = backgroundImage

		self.level = Map()

		john = Rabbit(1, "john" ,(200, 50, 50) , self.level.objectList, self.level.objectSpritesList)
		animJohnSprite = pygame.sprite.RenderPlain(john.getAnim())
		john.getAnim().stopAnim()

		regis = Rabbit(2, "regis" ,(50, 50, 200) , self.level.objectList, self.level.objectSpritesList)
		animRegisSprite = pygame.sprite.RenderPlain(regis.getAnim())
		regis.getAnim().stopAnim()

		john.appendRabbit(regis)
		regis.appendRabbit(john)

		clock = pygame.time.Clock()
		
		pygame.display.flip()

		while 1:
			key = pygame.key.get_pressed()
			for event in pygame.event.get():
				if event.type == QUIT:
					return

				elif event.type == MOUSEMOTION and (key[K_LSHIFT] or key[K_LCTRL]):
					mse = pygame.mouse.get_pos()
					if not any(obj.rect.collidepoint(mse) for obj in self.level.objectList):
						x = (int(mse[0]) / 50)*50
						y = (int(mse[1]) / 50)*50
						if key[K_LSHIFT]:
							self.level.addObject(x, y, "earth")
						else:
							self.level.addObject(x, y, "boing")

				elif event.type == MOUSEMOTION and key[K_LALT]:
					mse = pygame.mouse.get_pos()
					self.level.removeObjectFromPos(mse)

				elif event.type == KEYDOWN:
					if event.key == K_UP:
						john.jump()
					if event.key == K_LEFT:
						john.moveLeftStart()
					if event.key == K_RIGHT:
						john.moveRightStart()
					if event.key == K_w:
						regis.jump()
					if event.key == K_a:
						regis.moveLeftStart()
					if event.key == K_d:
						regis.moveRightStart()

				elif event.type == KEYUP:
					if event.key == K_LEFT:
						john.moveLeftStop()
					if event.key == K_RIGHT:
						john.moveRightStop()
					if event.key == K_a:
						regis.moveLeftStop()
					if event.key == K_d:
						regis.moveRightStop()

			screen.blit(background, backgroundRect, backgroundRect)
			screen.blit(background, john.rect, john.rect)
			screen.blit(background, john.getAnim().getRect(), john.getAnim().getRect())

			screen.blit(background, regis.rect, regis.rect)
			screen.blit(background, regis.getAnim().getRect(), regis.getAnim().getRect())

			self.level.blitMap(screen, background)

			john.update()
			regis.update()

			if pygame.font:
				font = pygame.font.Font(None, 36)
				text = font.render(str(john.getPoints()) + " : " + str(regis.getPoints()), 1, (10, 10, 10))
				textpos = text.get_rect(centerx=background.get_width()/2)
				screen.blit(text, textpos)

			animJohnSprite.update()
			animJohnSprite.draw(screen)

			animRegisSprite.update()
			animRegisSprite.draw(screen)

			john.getAnim().update()
			regis.getAnim().update()

			self.level.update(screen)

			pygame.display.update()

			clock.tick(60)

if __name__ == '__main__': 
	BumpNJump()
	