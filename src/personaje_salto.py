# import pygame
# from player import Personaje
# from sprite_sheet import SpriteSheet
# from config_2 import *

# class PersonajeSaltando(Personaje):
#     def __init__(self, groups, sprite, velocidad, ancho, alto, pantalla):
#         super().__init__(groups, sprite, velocidad, ancho, alto)
#         self.velocidad_vertical = 0
#         self.esta_saltando = False 
#         self.pantalla = pantalla

#     def update(self):
#         self.velocidad_vertical += GRAVEDAD
#         self.rect.y += self.velocidad_vertical

#         if self.rect.bottom >= HEIGHT:
#             self.rect.bottom = HEIGHT
#             self.velocidad_vertical = 0 
#         return super().update()
    
#     def salto(self):
#         self.velocidad_vertical = -17
        



