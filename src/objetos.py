import pygame
from pygame import *
from config_2 import *

class Objeto(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos_x, pos_y, puntaje, tamaño_x, tamaño_y, habilidad=None):
        super().__init__(groups)
        self.sprite_sheet = image
        self.contador_frames = 0
        self.tamaño_x = tamaño_x
        self.tamaño_y = tamaño_y
        self.image, self.cantidad_frames = self.sprite_sheet.get_imagen(self.contador_frames, self.tamaño_x, self.tamaño_y)
        self.rect = pygame.rect.Rect(pos_x, pos_y, 5, 5) 
        self.mascara = pygame.mask.from_surface(self.image)
        self.puntaje = puntaje
        self.habilidad = habilidad

    def update(self):
        self.frames()

    def draw(self, pantalla):
        self.mascara = pygame.mask.from_surface(self.image)
        pygame.draw.rect(pantalla, rojo, self.rect)  
        pantalla.blit(self.image, self.rect)

    def frames(self):
        self.contador_frames = (self.contador_frames + 1) % self.cantidad_frames
        self.image, _ = self.sprite_sheet.get_imagen(self.contador_frames, self.tamaño_x , self.tamaño_y)





                