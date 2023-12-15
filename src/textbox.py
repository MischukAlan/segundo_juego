import pygame
from pygame.locals import *

class TextBox:
    def __init__(self, x, y, ancho, alto, font_size=36, color_texto=(255, 255, 255), color_fondo=(0, 0, 0), fuente=None):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = ""
        self.color_texto = color_texto
        self.color_fondo = color_fondo
        self.fuente = fuente if fuente is not None else pygame.font.Font(None, font_size)
        self.activo = False

    def draw(self, pantalla):
        pygame.draw.rect(pantalla, self.color_fondo, self.rect)
        pygame.draw.rect(pantalla, self.color_texto, self.rect, 2)

        texto_renderizado = self.fuente.render(self.texto, True, self.color_texto)
        recta_texto = texto_renderizado.get_rect(center=self.rect.center)
        pantalla.blit(texto_renderizado, recta_texto)

    def manejar_eventos(self, evento):
        if evento.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.activo = not self.activo
            else:
                self.activo = False
        elif evento.type == KEYDOWN and self.activo:
            if evento.key == K_BACKSPACE:
                self.texto = self.texto[:-1]
            elif evento.key == K_RETURN:
                self.activo = False
            else:
                if len(self.texto) < 10:
                    self.texto += evento.unicode
        if self.activo:
            self.color_fondo = (200,200,200)
        else:
            self.color_fondo = (40,40,40)
        