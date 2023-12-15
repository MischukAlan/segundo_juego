import pygame
from config_2 import *

class SpriteSheet:
    def __init__(self, hoja_sprite):
        self.hoja = hoja_sprite

    def get_imagen(self, frame, width, height, escala=1):
        total_ancho_sprites = self.hoja.get_width()
        cantidad_frames = total_ancho_sprites // width
        imagen = pygame.Surface((width, height), pygame.SRCALPHA)
        imagen.blit(self.hoja.subsurface((frame * width, 0, width, height)), (0, 0))
        imagen = pygame.transform.scale(imagen, (int(imagen.get_width() * escala), int(imagen.get_height() * escala)))
        return imagen, cantidad_frames - 1
