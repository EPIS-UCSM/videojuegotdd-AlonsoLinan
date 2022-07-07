""""
AUTORES:	
		Mary Anne Calle Davies
		Victor Hugo Hinojosa Pinto
		Manuel Rodrigo Ramos Sánchez
		Adriana Raquel Linares Garrafa
		Gustavo Alonso Liñán Salinas
"""

#Librerías a importar
import random
import pygame
from pygame.locals import *


#Clase Rectángulo (forma de todos los objetos)
class Rectangle:

	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def intersects(self, other):
		left = self.x
		top = self.y
		right = self.x + self.w
		bottom = self.y + self.h

		oleft = other.x
		otop = other.y
		oright = other.x + other.w
		obottom = other.y + other.h

		return not (left >= oright or right <= oleft or top >= obottom or bottom <= otop)
