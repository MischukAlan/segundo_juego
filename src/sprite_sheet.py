import pygame
from config_2 import *

class SpriteSheet:
    def __init__(self, hoja_sprite):
        self.hoja = hoja_sprite

    def get_imagen(self, frame, width, height, flip = None):
        total_ancho_sprites = self.hoja.get_width()
        cantidad_frames = total_ancho_sprites // width
        imagen = pygame.Surface((width, height), pygame.SRCALPHA)
        imagen.blit(self.hoja.subsurface((frame * width, 0, width, height)), (0, 0))
        return imagen, cantidad_frames - 1

