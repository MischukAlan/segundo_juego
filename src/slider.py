import pygame
from pygame.locals import *

class Slider:
    def __init__(self, x, y, longitud, grosor, color, color_fondo, valor_inicial=0):
        self.rect = pygame.Rect(x, y, longitud, grosor)
        self.slider_rect = pygame.Rect(x, y - grosor // 2, grosor, grosor * 2)
        self.color = color
        self.color_fondo = color_fondo
        self.valor_minimo = 0
        self.valor_maximo = 100
        self.valor = valor_inicial
        self.dragging = False

    def draw(self, pantalla):
        pygame.draw.rect(pantalla, self.color_fondo, self.rect)
        pygame.draw.rect(pantalla, self.color, self.slider_rect)
        # self.valor

    def ajustar_valor(self):
        rango = self.valor_maximo - self.valor_minimo
        posicion_relativa = self.slider_rect.centerx - self.rect.left
        porcentaje = posicion_relativa / self.rect.width
        self.valor = int(self.valor_minimo + rango * porcentaje)

    def manejar_eventos(self, evento):
        if evento.type == MOUSEBUTTONDOWN:
            if self.slider_rect.collidepoint(evento.pos):
                self.dragging = True
        elif evento.type == MOUSEBUTTONUP:
            self.dragging = False
        elif evento.type == MOUSEMOTION and self.dragging:
            self.slider_rect.centerx = min(max(evento.pos[0], self.rect.left), self.rect.right)
            self.ajustar_valor()