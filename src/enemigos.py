import pygame
from pygame.locals import *
from config_2 import *


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, groups, sprite, velocidad, ancho, alto, frames, plataforma):
        super().__init__(groups)
        self.diccionario_sprites = {"idle_derecha": sprite["idle_derecha"]}
        self.imagen_actual = self.diccionario_sprites["idle_derecha"]
        self.velocidad = velocidad
        self.contador_frames = 0
        self.direccion = True
        self.plataforma = plataforma
        self.rectangulo_plataforma = self.plataforma.rect 
        self.rect = pygame.rect.Rect(self.rectangulo_plataforma.left, self.rectangulo_plataforma.top - alto, ancho, alto)
        self.mover_derecha = True
        self.imagen_enemigo, self.cantidad_frames  = self.imagen_actual.get_imagen(self.contador_frames, 120, 80, False)
        self.mascara = pygame.mask.from_surface(self.imagen_enemigo)
        self.image = self.imagen_enemigo
        # self.rect_golpe = pygame.Rect(self.rect.right -50, self.rect.top + 40, 30, 40)
        self.rect_golpe = pygame.Rect(300, 300, 30, 30)
        
    
    def update(self):
        super().update()
        self.image, self.cantidad_frames  = self.imagen_actual.get_imagen(self.contador_frames, 120, 80, False)
        self.mascara = pygame.mask.from_surface(self.image)
        self.movimiento()
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        self.rect_golpe.midbottom = self.rect.midbottom


    def draw(self, pantalla):
        pantalla.blit(self.imagen_enemigo, self.rect)
        pygame.draw.rect(pantalla, rojo, self.rect_mov)






    def movimiento(self):
        if self.mover_derecha:
            self.rect.x += self.velocidad
        else:
            self.rect.x -= self.velocidad

        if self.rect.left <= self.rectangulo_plataforma.left:
            self.mover_derecha = True

        elif self.rect.right >= self.rectangulo_plataforma.right:
            self.mover_derecha = False

    @classmethod
    def ajustar_posicion_y_enemigo(cls, lista_enemigos,  velocidad):
            for enemigo in lista_enemigos:
                enemigo.rect.y += velocidad

    @classmethod
    def ajustar_posicion_y_resta_enemigo(cls, lista_enemigos, velocidad):
            for enemigo in lista_enemigos:
                enemigo.rect.y -= velocidad