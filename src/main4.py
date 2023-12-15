import pygame
from sys import exit
from config_2 import *
from pygame.locals import *
from sprite_sheet import *
from fondos import *
from plataforma import Plataforma
from base import *
from player import Personaje
import os
from objetos import Objeto
from boss import Boss
from boton import *



class Level_3:
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
        self.imagen_plataforma = pygame.image.load("./src/assets_2/base/base.jpg")
        self.imagen_fondo =pygame.image.load(os.path.join(self.dir_actual,"./src/assets_2/fondo/bg_4.jpg"))

        self.imagen_boss = {"idle": SpriteSheet(pygame.image.load("./src/assets_2/best/PNG/without-stroke/hell-beast-idle.png").convert_alpha()),
                "ataque": SpriteSheet(pygame.image.load("./src/assets_2/best/PNG/without-stroke/hell-beast-breath.png").convert_alpha()),
                "muerte": SpriteSheet((pygame.image.load("./src/assets_2/best/PNG/without-stroke/hell-beast-burn.png").convert_alpha()))}
        
        self.imagen_coin = SpriteSheet(pygame.image.load(os.path.join(self.dir_actual, "src/assets_2/Coin/MonedaD.png")))
        self.enemigos_group = pygame.sprite.Group()
        self.plataformas = [Plataforma([self.all_plataformas,self.all_sprites], (2040, 200, 200, 20), self.imagen_plataforma)]
        self.coin_grupos = pygame.sprite.Group()
        self.boss_grupo = pygame.sprite.Group()
        self.coins = [Objeto([self.coin_grupos,self.all_sprites], self.imagen_coin, 600, 100, 100,16, 16)]
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
        self.boss= Boss([self.all_sprites,self.boss_grupo], self.imagen_boss, 5, 800, 536, 64 , 64, self.pantalla )
        self.player.rect.topleft = (CENTRO_PANTALLA_X - 60, HEIGHT - 80)
        self.posicion_X_pantalla = 0
        self.bandera = False
        self.disparo_habilitado = True
        self.contador=0


    def run(self):
        esta_jugando = True
        self.player.habilidad = True
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
        
        if self.player.rect_mov.right >= 500 and not self.posicion_X_pantalla <= -600 and keys[K_RIGHT]:
            self.posicion_X_pantalla -= VELOCIDAD_FONDO
        if self.posicion_X_pantalla <= -280 and not self.posicion_X_pantalla <= -600:
            self.posicion_X_pantalla -= VELOCIDAD_FONDO
            if self.player.rect.left  >= 150:
                self.player.rect.x -= VELOCIDAD_FONDO *6
                self.player.pos_atras = 0
                Boss.ajustar_posicion_y_resta_enemigo(self.boss_grupo, VELOCIDAD_FONDO)
                self.boss.ataque = True
            
        if self.tiempo_actual - self.ultima_actualizacion >= self.frames_juego:
            self.ultima_actualizacion = self.tiempo_actual
            self.player.contador_frames = (self.player.contador_frames + 1) % self.player.cantidad_frames
            self.boss.contador_frames = (self.boss.contador_frames + 1) % self.boss.cantidad_frames
            for x in self.coins:
                x.contador_frames = (x.contador_frames + 1) % x.cantidad_frames

        self.player.detecta_colisiones_enemigos(self.enemigos_group)
        self.player.detecta_colisiones_coin(self.coin_grupos)
        self.enemigos_group.update()
        self.player_group.update()
        self.all_sprites.update() 
        
    def draw(self):
        self.pantalla.blit(self.imagen_fondo,(self.posicion_X_pantalla,0))
        
        mostrar_texto(self.pantalla, str(self.player.vida), (50,50), BLANCO)
        mostrar_texto(self.pantalla, str(self.boss.vida), (600,50), BLANCO)
        mostrar_texto(self.pantalla, str(self.player.puntaje), (50,100), negro)

        if len(self.player.lista_disparo) > 0:
            for x in self.player.lista_disparo:
                rec_right = (x.rect.right)
                rec_left = (x.rect.left)
                per_right = (self.player.rect_mov.right)
                per_lefto = (self.player.rect_mov.left)
                x.draw(self.pantalla)
                x.trayectoria()
                if rec_right > per_right + 100 or rec_left < per_lefto - 100:
                    if  pygame.sprite.spritecollide(self.player.proyectil, self.boss_grupo, False):
                        self.boss.vida -= 100
                    self.player.lista_disparo.remove(x) 



        self.boss.manejar_disparos(self.player)
        self.boss.manejar_disparos_flama(self.player)
        self.all_sprites.draw(self.pantalla)           
        self.enemigos_group.draw(self.pantalla)
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














