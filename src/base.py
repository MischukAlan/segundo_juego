# import pygame
# from pygame.locals import *
# from config_2 import *



# class base():
#     def __init__(self, x, y , imagen, cantidad):  
#         self.x_pos = x
#         self.y_pos = y
#         self.image = imagen
#         self.cantidad = cantidad
#         self.lista = self.crear_bloques()
    
#     def update(self):
#         pass


#     # def draw(self, pantalla):
#     #     for _ in range(self.cantidad):
#     #         pantalla.blit(self.image, (self.x_pos, self.y_pos))
#     #         self.x_pos += self.image.get_width()

#     def crear_bloques(self):
#         bloques = []
#         for _ in range(self.cantidad):
#             bloques.append((self.x_pos, self.y_pos))
#             self.x_pos += self.image.get_width()
#         return bloques
    
   