import pygame
from pygame import * 
from config_2 import *
from sprite_sheet import * 



class Proyectil():
    def __init__(self, image, tamaño_x, tamaño_y, pos_x=0, pos_y=0, direccion=False, sube=False ):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = image
        self.rect = pygame.rect.Rect(pos_x, pos_y, 5, 5) 
        self.velocidad = VELOCIDAD_DISPARO
        self.direccion = direccion
        self.sube = sube
        self.contador_frames = 0
        self.tamaño_x = tamaño_x
        self.tamaño_y = tamaño_y
        self.image, self.cantidad_frames = self.sprite_sheet.get_imagen(self.contador_frames, self.tamaño_x, self.tamaño_y )
        
    def update(self):
        if self.sube:
            self.trayectoria_sube()
        else:
            self.trayectoria()
        self.contador_frames = (self.contador_frames + 1) % self.cantidad_frames

    def trayectoria(self):
        if self.direccion:
            self.rect.x = self.rect.x + self.velocidad
        else:
            self.rect.x = self.rect.x - self.velocidad
        self.image, self.cantidad_frames = self.sprite_sheet.get_imagen(self.contador_frames, self.tamaño_x, self.tamaño_y )


    def trayectoria_sube(self):
        self.rect.y = self.rect.y + self.velocidad
        self.image, self.cantidad_frames = self.sprite_sheet.get_imagen(self.contador_frames, self.tamaño_x, self.tamaño_y )

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)

    def bola_fuego (self, imagen, lista_disparo, alto, ancho): 
        for _ in range(CANTIDAD_BOLA_FUEGO):
            y =  randint(300, HEIGHT)
            if _ >= CANTIDAD_BOLA_FUEGO // 2:
                x =  randint(1200, 1800)
            else:
                x =  randint(500, 1000)
            self.proyectil = Proyectil(imagen, alto, ancho, WIDTH + x, y, False, False)
            lista_disparo.append(self.proyectil)

    def flama(self, imagen, lista_disparo, alto, ancho):
        for _ in range(CANTIDAD_FLAMA):
            if _ <= CANTIDAD_BOLA_FUEGO // 2:
                x =  randint(500, WIDTH -100)
            else:
                x =  randint(50, 500)
            y = randint(-500, -100)
            self.proyectil = Proyectil(imagen, alto, ancho, x, y, False, True)
            lista_disparo.append(self.proyectil)
            