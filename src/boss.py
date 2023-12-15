import pygame
from pygame import * 
from config_2 import *
from proyectil import Proyectil
from random import *
from sprite_sheet import *


class Boss(pygame.sprite.Sprite):
    def __init__(self, groups, sprite, velocidad, x, y ,ancho, alto, pantalla):
        super().__init__(groups)
        self.diccionario_sprites = {"idle": sprite["idle"], "ataque": sprite["ataque"], "muerte": sprite["muerte"]}
        self.contador_frames = 0
        self.imagen_proyectil = SpriteSheet(pygame.image.load("./src/assets_2/best/PNG/fire-ball.png"))
        self.imagen_flama = SpriteSheet(pygame.image.load("./src/assets_2/best/flama.png"))
        self.imagen_actual = self.diccionario_sprites["ataque"]
        self.rect = pygame.rect.Rect(x,  y, ancho, alto)
        self.velocidad = velocidad
        self.vida = 1000
        self.ancho = ancho
        self.alto = alto
        self.x = x
        self.y = y
        self.image, self.cantidad_frames  = self.imagen_actual.get_imagen(self.contador_frames, self.ancho, self.alto, 2)
        self.mascara = pygame.mask.from_surface(self.image)
        self.lista_disparo = []
        self.lista_flama = []
        self.pantalla = pantalla
        self.ultima_actualizacion = pygame.time.get_ticks()
        self.frames_juego = 5000
        self.tiempo_actual = None
        self.tiempo_siguiente_actualizacion = self.obtener_tiempo_siguiente_actualizacion()
        self.ataque = False 
        self.vida = 10000 
        




    def update(self):
        self.image, self.cantidad_frames = self.imagen_actual.get_imagen(self.contador_frames, self.ancho, self.alto, 2)
        self.tiempo_actual = pygame.time.get_ticks()
        self.mascara = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        if self.ataque:
            self.ataque_1()
            self.tiempo_transcurrido = self.tiempo_actual - self.ultima_actualizacion
            for proyectil in self.lista_disparo:
                proyectil.update()

        
        super().update()

    def draw(self, pantalla):
        pygame.draw.rect(pantalla, rojo, self.rect)  
        pantalla.blit(self.image, self.rect)
        
    @classmethod
    def ajustar_posicion_y_resta_enemigo(cls, lista_enemigos, velocidad):
            for enemigo in lista_enemigos:
                enemigo.rect.x -= velocidad
    
    def obtener_tiempo_siguiente_actualizacion(self):
        return randint(4000, 7000)
    
    def ataque_1(self):
        self.rect.bottom = HEIGHT
        self.rect.right = WIDTH 
        tiempo_transcurrido = self.tiempo_actual - self.ultima_actualizacion
        if tiempo_transcurrido >= self.tiempo_siguiente_actualizacion:
            self.ultima_actualizacion = self.tiempo_actual 
            self.contador_frames = 0
            if self.imagen_actual == self.diccionario_sprites["ataque"] or self.imagen_actual == self.diccionario_sprites["muerte"]:
                if self.imagen_actual == self.diccionario_sprites["muerte"]:
                    self.rect.bottom = HEIGHT + 190
                self.imagen_actual = self.diccionario_sprites["idle"]
                self.ancho = 55
                self.alto = 67
            else:
                numero_random = randint(0, 1)
                print(numero_random)
                if numero_random:
                    Proyectil.bola_fuego(self, self.imagen_proyectil, self.lista_disparo, 19, 16)
                    self.imagen_actual = self.diccionario_sprites["ataque"]
                    self.ancho = 64
                    self.alto = 64
                else:
                    self.rect.bottom = HEIGHT -190
                    Proyectil.flama(self, self.imagen_flama, self.lista_flama, 75, 160)
                    self.imagen_actual = self.diccionario_sprites["muerte"]
                    self.ancho = 74
                    self.alto = 160

            
            self.tiempo_siguiente_actualizacion = self.obtener_tiempo_siguiente_actualizacion()

    
         
    def manejar_disparos(self, player):
        for proyectil in self.lista_disparo:
            proyectil.update()
            proyectil.draw(self.pantalla)
            if player.rect_mov.colliderect(proyectil.rect):
                player.vida -= 100
                self.lista_disparo.remove(proyectil)
            if proyectil.rect.right < 0:
                self.lista_disparo.remove(proyectil)
                
    def manejar_disparos_flama(self, player):
        for proyectil in self.lista_flama:
            proyectil.update()
            proyectil.draw(self.pantalla)
            if player.rect_mov.colliderect(proyectil.rect):
                self.lista_flama.remove(proyectil)
                player.vida -= 200
            if proyectil.rect.right < 0:
                self.lista_flama.remove(proyectil)
    
