import pygame
from pygame.locals import *
from config_2 import *


class Plataforma (pygame.sprite.Sprite):
    def __init__(self, groups, rectangulo:pygame.Rect, imagen, movimiento_vertical=False, movimiento_horizontal=False , rango_movimiento=0, velocidad=3) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((rectangulo[2], rectangulo[3]))
        self.rect = self.image.get_rect(topleft=(rectangulo[0], rectangulo[1]))
        self.imagen_base = pygame.transform.scale(imagen, (rectangulo[2], rectangulo[3]))
        self.mascara = pygame.mask.from_surface(self.imagen_base)
        self.velocidad_movimiento = velocidad 
        self.rango_movimiento = rango_movimiento
        self.direccion = 1  
        self.contador = 0 
        self.movimiento_vertical = movimiento_vertical
        self.movimiento_horizontal = movimiento_horizontal

    def draw(self, pantalla):
        pantalla.blit(self.imagen_base, self.rect)


    def mover_verticalmente(self):
        if self.movimiento_vertical:
            if self.contador == self.rango_movimiento:
                self.direccion = -1
            elif self.contador == 0:
                self.direccion = 1
            self.rect.y += self.velocidad_movimiento * self.direccion
            self.contador += 1 * self.direccion

    def mover_horizontalmente(self):
        if self.movimiento_horizontal:
            if self.contador == self.rango_movimiento:
                self.direccion = -1
            elif self.contador == 0:
                self.direccion = 1
            self.rect.x += self.velocidad_movimiento * self.direccion
            self.contador += 1 * self.direccion

    @classmethod
    def ajustar_posicion_y(cls, velocidad, lista_plataformas):
        for plataforma in lista_plataformas:
            plataforma.rect.right += velocidad

    @classmethod
    def ajustar_posicion_y_resta(cls, velocidad, lista_plataformas):
        for plataforma in lista_plataformas:
            plataforma.rect.y -= velocidad
            
    @classmethod
    def ajustar_posicion_y_suma(cls, velocidad, lista_plataformas):
        for plataforma in lista_plataformas:
            plataforma.rect.y += velocidad


    @classmethod
    def ajustar_posicion_X_plataforma(cls, lista_plataformas,  velocidad):
            for plataforma in lista_plataformas:
                plataforma.rect.left += velocidad

    @classmethod
    def ajustar_posicion_X_resta_plataforma(cls, lista_plataformas, velocidad):
            for plataforma in lista_plataformas:
                plataforma.rect.right -= velocidad


    def colisiones_plataformas(self, player, grupo_plataformas):
        plataformas = pygame.sprite.spritecollide(player, grupo_plataformas, False)
        for platafor in plataformas:
            if self.player.rect_mov.colliderect(platafor.rect):
                if self.player.rect.top <= platafor.rect.bottom and self.player.velocidad_vertical < 0:
                    self.player.rect.top = platafor.rect.bottom
                    self.player.velocidad_vertical = 0

                elif self.player.rect.bottom >= platafor.rect.top and self.player.velocidad_vertical > 0:
                    self.player.rect.bottom = platafor.rect.top
                    self.player.velocidad_vertical = 0
                    self.bandera = True
