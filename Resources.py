#!/usr/bin/python

import os
import pygame
from pygame.locals import *
from pygame import surfarray
import numpy as N

def loadPNG(name, color, anim = False):
	if anim:
		fullname = os.path.join('resources/anim', name)
	else:
		fullname = os.path.join('resources/img', name)
	try:
		image = pygame.image.load(fullname)

		if color == (255, 255, 255):
			if image.get_alpha() is None:
				image = image.convert()
			else:
				image = image.convert_alpha()

		else:
			array = surfarray.array3d(image)
			editImg = N.array(array)

			editImg[:,:,:] = editImg[:,:,:]/255. * color
			
			imageColor = surfarray.make_surface(editImg)

			if image.get_alpha() is None:
				image = imageColor.convert()
			else:
				image = imageColor.convert_alpha()

	except pygame.error, message:
		print 'Cannot load image: ', fullname
		raise SystemExit, message
	return image, image.get_rect()