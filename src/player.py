import pygame
from pygame import * 
from config_2 import *
from proyectil import Proyectil
from sprite_sheet import *

class Personaje(pygame.sprite.Sprite):
    def __init__(self, groups, sprite, velocidad, ancho, alto, pantalla):
        super().__init__(groups)
        self.diccionario_sprites = {"idle_derecha": sprite["idle_derecha"],"idle_izquierda": sprite["idle_izquierda"], "run_derecha": sprite["run_derecha"], "run_izquierda": sprite["run_izquierda"], "ataque_derecha": sprite["ataque_derecha"], "ataque_izquierda": sprite["ataque_izquierda"], "jump_derecha": sprite["jump_derecha"], "jump_izquierda": sprite["jump_izquierda"], "muerte": sprite["muerte"]}
        self.contador_frames = 0
        self.imagen_actual = self.diccionario_sprites["idle_derecha"]
        self.imagen_proyectil = SpriteSheet(pygame.image.load("./src/assets_2/caballero/_acha_2.png"))
        self.rect = pygame.rect.Rect(CENTRO_PANTALLA[0], CENTRO_PANTALLA[1], ancho, alto)
        self.velocidad = velocidad
        self.direccion = True
        self.cayendo = False
        self.vida = 100
        self.image, self.cantidad_frames  = self.imagen_actual.get_imagen(self.contador_frames, 120, 80)
        self.mascara = pygame.mask.from_surface(self.image)
        self.rect_golpe = pygame.Rect(self.rect.right -40, self.rect.top + 40, 30, 40)
        self.puntaje = 0 
        self.rect_mov = pygame.Rect(300, 300, 25, 35)
        self.lista_disparo = []
        self.velocidad_vertical = 0
        self.esta_saltando = False 
        self.pantalla = pantalla
        self.habilidad = False
        self.pos_atras = 150
        self.correcion = 0
        
    
    
    def update(self):
        self.rect_mov.midbottom = self.rect.midbottom
        self.image, self.cantidad_frames = self.imagen_actual.get_imagen(self.contador_frames, 120, 80)
        self.mascara = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        self.movimientos()
        self.atacar()
        for proyectil in self.lista_disparo:
            proyectil.update()
            self.lista_disparo = [proyectil for proyectil in self.lista_disparo if proyectil.rect.x < WIDTH]

        self.velocidad_vertical += GRAVEDAD
        self.rect.y += self.velocidad_vertical

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocidad_vertical = 0 

        super().update()
    
    def draw(self, pantalla):
        pygame.draw.rect(pantalla, rojo, self.rect_mov)  
        pantalla.blit(self.image, self.rect)

    def movimientos(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.imagen_actual = self.diccionario_sprites["run_derecha"]
            if self.rect.right <= WIDTH - self.correcion:
                self.rect.x += self.velocidad
                self.direccion = True
            
        elif keys[K_LEFT]:
            self.imagen_actual = self.diccionario_sprites["run_izquierda"]
            if self.rect.x >= self.pos_atras:
                self.rect.x -= self.velocidad
                self.direccion = False
        else:
            if self.direccion:
                self.imagen_actual = self.diccionario_sprites["idle_derecha"]
            else:
                self.imagen_actual = self.diccionario_sprites["idle_izquierda"]

    def detecta_colisiones_enemigos(self, grupo_enemigos):
        for enemigo in grupo_enemigos:
            if self.mascara.overlap(enemigo.mascara, offset(self.rect_mov, enemigo.rect)):
                self.vida -= 10

    def detecta_colisiones_coin(self, grupo_coins):
        for coin in grupo_coins:
            if self.mascara.overlap(coin.mascara, offset(coin.rect, self.rect_mov)):
                coin.kill()
                self.puntaje += coin.puntaje
                if coin.habilidad:
                    self.habilidad = True


    def atacar(self):
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.contador_frames = 0
            if self.direccion:
                self.imagen_actual = self.diccionario_sprites["ataque_derecha"]
                self.rect_golpe = pygame.Rect(self.rect.right - 35, self.rect.top + 40, 30, 40)
            else:
                self.imagen_actual = self.diccionario_sprites["ataque_izquierda"]
                self.rect_golpe = pygame.Rect(self.rect.left, self.rect.top + 35, 30, 40)
            return self.rect_golpe
        

    def detecta_colisiones_ataque(self, grupo_enemigos):
        for enemigo in grupo_enemigos:
            if self.rect_golpe.colliderect(enemigo.rect):
                enemigo.kill()
                self.puntaje += 10


    def disparar(self, x, y):
        self.proyectil = Proyectil(self.imagen_proyectil, 30, 20, x, y, self.direccion)
        self.lista_disparo.append(self.proyectil)

    def salto(self):
        self.velocidad_vertical = -17
