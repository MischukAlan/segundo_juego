import pygame
from pygame.locals import *
from config_2 import *


class bg_pisos():
    def __init__(self, x_pos, y_pos, imagen, cantidad) -> None:
        self.image = imagen
        self.correccion = self.image.get_width()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.cantidad = cantidad
