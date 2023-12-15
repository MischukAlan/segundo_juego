import pygame
from pygame.locals import *

class Label:
    def __init__(self, x, y, texto, font_size=24, color=(0, 0, 0), fuente=None):
        self.x = x
        self.y = y
        self.texto = texto
        self.color = color
        self.fuente = fuente if fuente is not None else pygame.font.Font(None, font_size)

    def draw(self, pantalla):
        texto_renderizado = self.fuente.render(self.texto, True, self.color)
        recta_texto = texto_renderizado.get_rect(topleft=(self.x, self.y))
        pantalla.blit(texto_renderizado, recta_texto)