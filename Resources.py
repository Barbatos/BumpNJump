#!/usr/bin/python

import os
import pygame
from pygame.locals import *

def loadPNG(name, anim = False):
	if anim:
		fullname = os.path.join('resources/anim', name)
	else:
		fullname = os.path.join('resources/img', name)
	try:
		print fullname
		image = pygame.image.load(fullname)

		if image.get_alpha() is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error, message:
		print 'Cannot load image: ', fullname
		raise SystemExit, message
	return image, image.get_rect()