import pygame
from pygame import *
from random import * 
from pygame.locals import *

FPS = 25

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
negro = (0,0,0)

WIDTH  = 800   #ANCHO
HEIGHT = 600     #ALTO
TAMAÑO_PANTALLA = (WIDTH , HEIGHT)
CENTRO_PANTALLA = (WIDTH  // 2, HEIGHT // 2)
CENTRO_PANTALLA_X = WIDTH // 2
CENTRO_PANTALLA_Y = HEIGHT // 2 

WIDTH_PLAYER  = 120  
HEIGTH_PLAYER = 80

VELOCIDAD_FONDO = 5


VELOCIDAD = 10
VELOCIDAD_DISPARO = 10


GRAVEDAD = 1

def salir ():
    pygame.quit()
    exit()



def mostrar_texto(pantalla, texto, ubicacion, color=(255, 255, 255), fuente=None):
    if fuente is None:
        fuente = pygame.font.Font(None, 36)  
    superficie_texto = fuente.render(texto, True, color)
    rectangulo_texto = superficie_texto.get_rect()
    rectangulo_texto.topleft = ubicacion
    pantalla.blit(superficie_texto, rectangulo_texto)


def offset(rect_1 , rect_2):
        return (rect_1.x - rect_2.x , rect_1.y - rect_2.y)
