import pygame
from sys import exit
from config_2 import *
from pygame.locals import *
from sprite_sheet import *
from fondos import *
from plataforma import Plataforma
from enemigos import Enemigo
from base import *
from player import Personaje
import os
from objetos import Objeto
from boton import *


class Level_2:
    def __init__(self):
        pygame.init()
        self.reloj = pygame.time.Clock()
        self.FPS = pygame.time.Clock()
        self.FPS = pygame.time.Clock()
        self.dir_actual = os.getcwd()
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Mi segundo jueguito')
        self.all_plataformas = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.ultima_actualizacion = pygame.time.get_ticks()
        self.frames_juego = 100
        self.player_group = pygame.sprite.Group()
        self.enemigos_group = pygame.sprite.Group()
        self.imagen_plataforma = pygame.image.load("./src/assets_2/base/base.jpg")
        self.imagen_pisos = pygame.image.load("./src/assets_2/base/tile21.png")
        self.imagen_coin = SpriteSheet(pygame.image.load(os.path.join(self.dir_actual, "src/assets_2/Coin/MonedaD.png")))
        self.imagen_acha = SpriteSheet(pygame.image.load("./src/assets_2/caballero/_acha_2.png"))
        self.gema= SpriteSheet(pygame.image.load(os.path.join(self.dir_actual, "src/assets_2/Coin/spr_coin_strip4.png")))
        self.coin_grupos = pygame.sprite.Group()
        self.coins = [
        Objeto([self.coin_grupos,self.all_sprites], self.imagen_coin, 600, 100, 100,16, 16),#ok
        Objeto([self.coin_grupos,self.all_sprites], self.gema, 218, 130, 400,  16, 16 ),#ok
        Objeto([self.coin_grupos,self.all_sprites], self.imagen_coin, 1600, 200, 100,  16, 16 ), #ok
        Objeto([self.coin_grupos,self.all_sprites], self.imagen_coin, 800, 360, 100,  16, 16 ), #ok
        Objeto([self.coin_grupos,self.all_sprites], self.imagen_coin, 1300, 250, 100,  16, 16 ), #ok
        Objeto([self.coin_grupos,self.all_sprites], self.imagen_coin, 1300, 50, 100,  16, 16 ), #ok
        Objeto([self.coin_grupos,self.all_sprites], self.imagen_coin, 1500, 50, 100, 16, 16), #ok
        Objeto([self.coin_grupos,self.all_sprites], self.imagen_acha, 1000, 500, 0, 30, 20, True) #ok
       ]
        self.plataformas = [
        Plataforma([self.all_plataformas,self.all_sprites], (2040, 200, 200, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas, self.all_sprites], (1800, 80, 200, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas, self.all_sprites], (1400, 110, 200, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas, self.all_sprites], (1200, 70, 200, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas, self.all_sprites], (650, 65, 200, 20), self.imagen_plataforma, False, True, 50, 5),
        ####### para tras
        Plataforma([self.all_plataformas, self.all_sprites], (200, 150, 50, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas, self.all_sprites], (400, 150, 200, 20), self.imagen_plataforma, True, False, 70),
        Plataforma([self.all_plataformas, self.all_sprites], (700, 400, 200, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas, self.all_sprites], (900, 260, 200, 20), self.imagen_plataforma, False, True,20),
        Plataforma([self.all_plataformas, self.all_sprites], (1200, 300, 200, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas, self.all_sprites], (1500, 360, 100, 20), self.imagen_plataforma, False, True, 40),
        Plataforma([self.all_plataformas, self.all_sprites], (1800, 400, 150, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas, self.all_sprites], (2000, 500, 200, 20), self.imagen_plataforma)
        ]
        self.imagen_fondo = pygame.image.load("./src/assets_2/fondo/bg.jpg")
        self.personaje_caballero_sprites = {"idle_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Idle.png").convert_alpha()),
                "run_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Run.png").convert_alpha()), 
                "run_izquierda": SpriteSheet((pygame.image.load("./src/assets_2/caballero/_Run_izquierda.png").convert_alpha())),
                "idle_izquierda": SpriteSheet(pygame.transform.flip(pygame.image.load("./src/assets_2/caballero/_Idle.png").convert_alpha(),True, False)),
                "ataque_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Attack.png").convert_alpha()),
                "ataque_izquierda": SpriteSheet(pygame.transform.flip(pygame.image.load("./src/assets_2/caballero/_Attack.png").convert_alpha(),True, False)),
                "jump_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Jump.png").convert_alpha()),
                "jump_izquierda": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Jump_izquierda.png").convert_alpha()),
                "muerte": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Death.png").convert_alpha())}
        self.player = Personaje(self.player_group, self.personaje_caballero_sprites, VELOCIDAD, 120, 80, self.pantalla)
        self.imagen_enemigo = {"idle_izquierda": SpriteSheet(pygame.image.load("./src/assets_2/caballero/demon-idle.png").convert_alpha()), 
                                "idle_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/demon-idle_derecha.png").convert_alpha())
                                }
        self.enemigo_1 = Enemigo([self.enemigos_group, self.all_sprites], self.imagen_enemigo, 2, 160, 144, 6, self.all_plataformas.sprites()[0])
        self.enemigo_3 = Enemigo([self.enemigos_group, self.all_sprites], self.imagen_enemigo, 2, 160, 144, 6, self.all_plataformas.sprites()[7])
        self.enemigo_4 = Enemigo([self.enemigos_group, self.all_sprites], self.imagen_enemigo, 2, 160, 144, 6, self.all_plataformas.sprites()[9])
        self.enemigo_5 = Enemigo([self.enemigos_group, self.all_sprites], self.imagen_enemigo, 2, 160, 144, 6, self.all_plataformas.sprites()[12])
        self.player.rect.topleft = (CENTRO_PANTALLA_X - 60, HEIGHT - 80)
        self.posicion_X_pantalla = 0
        self.bandera = False
        self.disparo_habilitado = True

    def run(self):
        esta_jugando = True
        self.player.correcion = 150
        while esta_jugando:
            self.tiempo_actual = pygame.time.get_ticks()
            self.FPS.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    esta_jugando = False
                elif evento.type == KEYDOWN:
                    if evento.key == K_ESCAPE:
                        esta_jugando = False
                    if evento.key == K_p:
                        if self.pausa():
                            return
                    elif evento.key == K_d:
                        if self.player.habilidad:
                            if self.player.direccion:
                                x, y = self.player.rect_mov.topright
                            else:
                                x, y = self.player.rect_mov.topleft
                            self.player.disparar(x, y)
                        self.disparo_habilitado = False  

            self.update()

            self.draw()

        self.close()

    def update(self):
        keys = pygame.key.get_pressed() 
        Plataforma.colisiones_plataformas(self, self.player, self.all_plataformas)

        if keys[K_SPACE] and not self.player.esta_saltando and (self.player.rect.bottom == HEIGHT or self.bandera == True):
            self.player.salto()
            self.bandera = False
            

        if keys[K_a]:
            self.player.atacar()
            self.player.detecta_colisiones_ataque(self.enemigos_group)

        print(self.posicion_X_pantalla)

        if self.player.rect_mov.right >= 500 and  self.posicion_X_pantalla >= -1600 and keys[K_RIGHT]:
            self.posicion_X_pantalla -= VELOCIDAD_FONDO
            Plataforma.ajustar_posicion_X_resta_plataforma(self.plataformas, VELOCIDAD_FONDO)
            Plataforma.ajustar_posicion_X_resta_plataforma(self.coins, VELOCIDAD_FONDO)
            Enemigo.ajustar_posicion_X_resta_enemigo([self.enemigo_1,  self.enemigo_3, self.enemigo_4, self.enemigo_5], VELOCIDAD_FONDO)

            

        elif self.player.rect_mov.left <= 200 and not self.posicion_X_pantalla == 0 and keys[K_LEFT]:
            self.posicion_X_pantalla += VELOCIDAD_FONDO
            Plataforma.ajustar_posicion_X_plataforma(self.plataformas, VELOCIDAD_FONDO)
            Plataforma.ajustar_posicion_X_plataforma(self.coins, VELOCIDAD_FONDO)
            Enemigo.ajustar_posicion_X_enemigo([self.enemigo_1, self.enemigo_3, self.enemigo_4, self.enemigo_5], VELOCIDAD_FONDO)

        if self.tiempo_actual - self.ultima_actualizacion >= self.frames_juego:
            self.ultima_actualizacion = self.tiempo_actual
            self.player.contador_frames = (self.player.contador_frames + 1) % self.player.cantidad_frames
            for x in self.coins:
                x.contador_frames = (x.contador_frames + 1) % x.cantidad_frames
            self.enemigo_1.contador_frames = (self.enemigo_1.contador_frames + 1) % self.enemigo_1.cantidad_frames
            self.enemigo_3.contador_frames = (self.enemigo_3.contador_frames + 1) % self.enemigo_3.cantidad_frames
            self.enemigo_4.contador_frames = (self.enemigo_4.contador_frames + 1) % self.enemigo_4.cantidad_frames
            self.enemigo_5.contador_frames = (self.enemigo_5.contador_frames + 1) % self.enemigo_5.cantidad_frames
        

            

        self.player.detecta_colisiones_enemigos(self.enemigos_group)
        self.player.detecta_colisiones_coin(self.coin_grupos)
        self.player_group.update()
        self.all_sprites.update() 
        

    def draw(self):
        self.pantalla.blit(self.imagen_fondo,(self.posicion_X_pantalla,0))
        
        mostrar_texto(self.pantalla, str(self.player.vida), (50,50), negro)
        mostrar_texto(self.pantalla, str(self.player.puntaje), (50,100), negro)

        if len(self.player.lista_disparo) > 0:
            for x in self.player.lista_disparo:
                rec_right = (x.rect.right)
                rec_left = (x.rect.left)
                per_right = (self.player.rect_mov.right)
                per_lefto = (self.player.rect_mov.left)
                x.draw(self.pantalla)
                x.trayectoria()
                if rec_right > per_right + 100 or rec_left < per_lefto - 100 or pygame.sprite.spritecollide(self.player.proyectil, self.enemigos_group, True):
                    self.player.lista_disparo.remove(x) 

        self.all_sprites.draw(self.pantalla)           
        self.player.draw(self.pantalla)
        
        for plataforma in self.all_plataformas:
            plataforma.mover_horizontalmente()
            plataforma.mover_verticalmente()
            plataforma.draw(self.pantalla)



        pygame.display.flip()

    def close(self):
        pygame.quit()
        exit()


    def pausa(self):
        while True:
            reanudar = Boton(300, 100, 100,100, "reanudar", BLANCO, verde, rojo, None)
            menu_principal = Boton(300, 300, 100,100, "Menu Principal", BLANCO, verde, rojo, None)
            config = Boton(300, 500, 100,100, "Configuracion", BLANCO, verde, rojo, None)

            mouse_x, mouse_y = pygame.mouse.get_pos()
        
            reanudar.draw(self.pantalla)
            menu_principal.draw(self.pantalla)
            config.draw(self.pantalla)

            pygame.display.flip()
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                        if reanudar.rect.collidepoint(mouse_x, mouse_y):
                            return False
                        if config.rect.collidepoint(mouse_x, mouse_y):
                            pass
                        if menu_principal.rect.collidepoint(mouse_x, mouse_y):
                            return True
