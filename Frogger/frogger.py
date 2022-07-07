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

#Declaramos las dimensiones de la pantalla del videojuego
g_vars = {}
g_vars['width'] = 416
g_vars['height'] = 416
g_vars['fps'] = 30
g_vars['grid'] = 32
g_vars['window'] = pygame.display.set_mode( [g_vars['width'], g_vars['height']], pygame.HWSURFACE)
