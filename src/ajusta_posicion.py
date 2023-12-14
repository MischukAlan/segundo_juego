import pygame
from pygame import * 
from config_2 import *



@classmethod
def ajustar_posicion_y_enemigo(cls, lista_enemigos,  velocidad):
        for enemigo in lista_enemigos:
            enemigo.rect.y += velocidad

@classmethod
def ajustar_posicion_y_resta_enemigo(cls, lista_enemigos, velocidad):
        for enemigo in lista_enemigos:
            enemigo.rect.y -= velocidad

@classmethod
def ajustar_posicion_X_enemigo(cls, lista_enemigos,  velocidad):
        for enemigo in lista_enemigos:
            enemigo.rect.left += velocidad

@classmethod
def ajustar_posicion_X_resta_enemigo(cls, lista_enemigos, velocidad):
        for enemigo in lista_enemigos:
            enemigo.rect.right -= velocidad