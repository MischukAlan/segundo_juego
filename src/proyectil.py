import pygame
from pygame import * 
from config_2 import *
from sprite_sheet import * 



class Proyectil():
    def __init__(self, pos_x, pos_y, direccion):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = SpriteSheet(pygame.image.load("./src/assets_2/caballero/_acha.png"))
        self.rect = pygame.rect.Rect(pos_x, pos_y, 5, 5) 
        self.velocidad = VELOCIDAD_DISPARO
        self.direccion = direccion
        self.contador_frames = 0
        self.image, self.cantidad_frames = self.sprite_sheet.get_imagen(self.contador_frames, 120, 80)
        
    def update(self):
        self.trayectoria()
        self.contador_frames = (self.contador_frames + 1) % self.cantidad_frames

    def trayectoria(self):
        if self.direccion:
            self.rect.x = self.rect.x + self.velocidad
        else:
            self.rect.x = self.rect.x - self.velocidad
        self.image, self.cantidad_frames = self.sprite_sheet.get_imagen(self.contador_frames, 120, 80)

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)
        