import pygame
from pygame import * 
from config_2 import *

class Personaje(pygame.sprite.Sprite):
    def __init__(self, groups, sprite, velocidad, ancho, alto):
        super().__init__(groups)
        self.diccionario_sprites = {"idle_derecha": sprite["idle_derecha"],"idle_izquierda": sprite["idle_izquierda"], "run_derecha": sprite["run_derecha"], "run_izquierda": sprite["run_izquierda"], "ataque_derecha": sprite["ataque_derecha"], "ataque_izquierda": sprite["ataque_izquierda"], "jump_derecha": sprite["jump_derecha"], "jump_izquierda": sprite["jump_izquierda"], "muerte": sprite["muerte"]}
        self.contador_frames = 0
        self.imagen_actual = self.diccionario_sprites["idle_derecha"]
        self.rect = pygame.rect.Rect(CENTRO_PANTALLA[0], CENTRO_PANTALLA[1], ancho, alto)
        self.velocidad = velocidad
        self.direccion = True
        self.cayendo = False
        self.vida = 100
        self.imagen_caballero, self.cantidad_frames  = self.imagen_actual.get_imagen(self.contador_frames, 120, 80,self.direccion)
        self.mascara = pygame.mask.from_surface(self.imagen_caballero)
        self.rect_golpe = pygame.Rect(self.rect.right -40, self.rect.top + 40, 30, 40)
        self.puntaje = 0 
        self.rect_mov = pygame.Rect(300, 300, 25, 35)
        self.tiempo_espera_despues_muerte = 1000
        self.muerte_tiempo_inicial = 0  
    
    
    def update(self):
        self.rect_mov.midbottom = self.rect.midbottom
        self.imagen_caballero, self.cantidad_frames = self.imagen_actual.get_imagen(self.contador_frames, 120, 80, self.direccion)
        self.mascara = pygame.mask.from_surface(self.imagen_caballero)
        self.movimientos()
        self.atacar()
        self.muerte()
        super().update()
    
    def draw(self, pantalla):
        self.rect = self.imagen_caballero.get_rect(topleft=self.rect.topleft)
        pygame.draw.rect(pantalla, rojo, self.rect_mov)  
        pantalla.blit(self.imagen_caballero, self.rect)

    def movimientos(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.imagen_actual = self.diccionario_sprites["run_derecha"]
            if self.rect.right <= WIDTH:
                self.rect.x += self.velocidad
                self.direccion = True
            
        elif keys[K_LEFT]:
            self.imagen_actual = self.diccionario_sprites["run_izquierda"]
            if self.rect.x >= 0:
                self.rect.x -= self.velocidad
                self.direccion = False
        else:
            if self.direccion:
                self.imagen_actual = self.diccionario_sprites["idle_derecha"]
            else:
                self.imagen_actual = self.diccionario_sprites["idle_izquierda"]

    def detecta_colisiones_enemigos(self, grupo_enemigos):
        for enemigo in grupo_enemigos:
            if self.mascara.overlap(enemigo.mascara, offset(self.rect, enemigo.rect)):
                self.vida -= 10

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
            if self.rect_golpe.colliderect(enemigo.rect_golpe):
                enemigo.kill()
                self.puntaje += 10

    def muerte (self, ):
        self.muerte_tiempo_inicial = time.time()

        # Espera el tiempo especificado después de la muerte
        time.sleep(self.tiempo_espera_despues_muerte)

        # Verifica si ha pasado suficiente tiempo después de la muerte
        tiempo_actual = time.time()
        tiempo_transcurrido_despues_muerte = tiempo_actual - self.muerte_tiempo_inicial

        if tiempo_transcurrido_despues_muerte >= self.tiempo_espera_despues_muerte:
            # Realiza el kill después de 2 segundos
            self.kill()

