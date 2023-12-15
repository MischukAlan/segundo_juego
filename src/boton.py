import pygame
from pygame.locals import *
from config_2 import *

class Boton:
    def __init__(self, x, y, ancho, alto, texto, color_font, color_bg, color_bg_hover=None, fuente=None, accion=None):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color_font = color_font
        self.color_bg = color_bg
        self.color_bg_hover = color_bg_hover if color_bg_hover is not None else color_bg
        self.fuente = fuente if fuente is not None else pygame.font.Font(None, 36)
        self.accion = accion
        self.flag = False
        self.pausa = False
        

    def draw(self, pantalla):
        self.actualizar()
        render = self.fuente.render(self.texto, True, self.color_font)
        recta_text = render.get_rect(center=self.rect.center)

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(pantalla, self.color_bg_hover, self.rect, border_radius=5)
        else:
            pygame.draw.rect(pantalla, self.color_bg, self.rect, border_radius=5)

        pantalla.blit(render, recta_text)

    def actualizar(self):
        cursor = pygame.mouse.get_pos()
        hacer_clic = pygame.mouse.get_pressed()
        
        if self.rect.collidepoint(cursor) and hacer_clic[0] == 1:
            self.flag = True
                
            
        
    def set_texto(self, nuevo_texto):
        self.texto = nuevo_texto


# if hacer_clic[0] == False:
#             self.flag = True
# if self.flag:
#                 # self.accion()
#                 if self.pausa:
#                     self.set_texto("pausa")
#                 else:
#                     self.set_texto("play")
#                 self.pausa = not self.pausa
#                 self.flag = False
