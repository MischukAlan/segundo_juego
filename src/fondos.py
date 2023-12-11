import pygame
from config_2 import *

class piso:
    def __init__(self, x, y, whidht_piso, height_piso, pantalla) -> None:
        self.piso = pygame.draw.rect(pantalla, (30,30,30), pygame.Rect(x , y, whidht_piso, height_piso))