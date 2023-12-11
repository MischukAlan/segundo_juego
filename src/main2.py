import pygame, math
from sys import exit
from config_2 import *
from pygame.locals import *
from player import Personaje
from sprite_sheet import *
from fondos import *
from personaje_salto import PersonajeSaltando
from plataforma import Plataforma
from enemigos import Enemigo



class Juego:
    def __init__(self):
        pygame.init()
        self.reloj = pygame.time.Clock()
        self.FPS = pygame.time.Clock()
        self.FPS = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Mi segundo jueguito')
        self.all_plataformas = pygame.sprite.Group()
        self.ultima_actualizacion = pygame.time.get_ticks()
        self.frames_juego = 100
        self.player_group = pygame.sprite.Group()
        self.enemigos_group = pygame.sprite.Group()
        self.imagen_plataforma = pygame.image.load("./src/assets_2/base/base.jpg")
        self.plataformas = [
        Plataforma([self.all_plataformas], (600, 390, 200, 20), self.imagen_plataforma, True, 50),
        Plataforma([self.all_plataformas], (0, 450, 400, 20),self.imagen_plataforma),
        Plataforma([self.all_plataformas], (300, 300, 100, 20),self.imagen_plataforma),
        Plataforma([self.all_plataformas], (600, 200, 200, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas], (360, 0, 100, 20),self.imagen_plataforma, True, 40), 
        Plataforma([self.all_plataformas], (70, -50, 200, 20), self.imagen_plataforma),
        Plataforma([self.all_plataformas], (510, -50, 200, 20), self.imagen_plataforma),]
        self.imagen_fondo = pygame.image.load("./src/assets_2/fondo/fondo_castillo.jpg")
        self.personaje_caballero_sprites = {"idle_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Idle.png").convert_alpha()),
                "run_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Run.png").convert_alpha()), 
                "run_izquierda": SpriteSheet((pygame.image.load("./src/assets_2/caballero/_Run_izquierda.png").convert_alpha())),
                "idle_izquierda": SpriteSheet(pygame.transform.flip(pygame.image.load("./src/assets_2/caballero/_Idle.png").convert_alpha(),True, False)),
                "ataque_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Attack.png").convert_alpha()),
                "ataque_izquierda": SpriteSheet(pygame.transform.flip(pygame.image.load("./src/assets_2/caballero/_Attack.png").convert_alpha(),True, False)),
                "jump_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Jump.png").convert_alpha()),
                "jump_izquierda": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Jump_izquierda.png").convert_alpha()),
                "muerte": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Death.png").convert_alpha())}
        self.player = PersonajeSaltando(self.player_group, self.personaje_caballero_sprites, 10, 120, 80)
        self.enemigo_1 = Enemigo(self.enemigos_group,{"idle_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Idle.png").convert_alpha())}, 2, 120, 80, 9, self.all_plataformas.sprites()[1])
        self.enemigo_2 = Enemigo(self.enemigos_group,{"idle_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Idle.png").convert_alpha())}, 7, 120, 80, 0, self.all_plataformas.sprites()[3])
        self.enemigo_3 = Enemigo(self.enemigos_group,{"idle_derecha": SpriteSheet(pygame.image.load("./src/assets_2/caballero/_Idle.png").convert_alpha())}, 7, 120, 80, 0, self.all_plataformas.sprites()[5])
        self.player.rect.topleft = (CENTRO_PANTALLA_X - 60, HEIGHT - 80)
        self.posicion_y_pantalla = -600
        self.bandera = False
        

    def run(self):
        esta_jugando = True
        while esta_jugando:
            self.tiempo_actual = pygame.time.get_ticks()
            self.FPS.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    esta_jugando = False
                elif evento.type == KEYDOWN:
                    if evento.key == K_ESCAPE:
                        esta_jugando = False

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

        if self.player.rect.top <= 100 and not self.posicion_y_pantalla == 0:
            self.player.cayendo = True
            self.posicion_y_pantalla += VELOCIDAD_FONDO
            Plataforma.ajustar_posicion_y(VELOCIDAD_FONDO, self.plataformas)
            Enemigo.ajustar_posicion_y_enemigo([self.enemigo_1, self.enemigo_2, self.enemigo_3], VELOCIDAD_FONDO)

        elif self.player.rect.bottom == HEIGHT and not self.posicion_y_pantalla == -600:
            self.player.cayendo = False
            self.posicion_y_pantalla -= VELOCIDAD_FONDO
            Plataforma.ajustar_posicion_y_resta(VELOCIDAD_FONDO, self.plataformas)
            Enemigo.ajustar_posicion_y_resta_enemigo([self.enemigo_1, self.enemigo_2, self.enemigo_3], VELOCIDAD_FONDO)

        if self.tiempo_actual - self.ultima_actualizacion >= self.frames_juego:
            self.ultima_actualizacion = self.tiempo_actual
            self.player.contador_frames = (self.player.contador_frames + 1) % self.player.cantidad_frames
            self.enemigo_1.contador_frames = (self.enemigo_1.contador_frames + 1) % self.enemigo_1.cantidad_frames

        print(self.player.contador_frames)
        self.player.detecta_colisiones_enemigos(self.enemigos_group)
        self.all_plataformas.update()
        self.enemigos_group.update()
        self.player_group.update()

    def draw(self):
        
        self.pantalla.blit(self.imagen_fondo,(0,self.posicion_y_pantalla))    
        pygame.draw.rect(self.pantalla, rojo, self.enemigo_1.rect_golpe)    
        
        mostrar_texto(self.pantalla, str(self.player.vida), (50,50), negro)
        mostrar_texto(self.pantalla, str(self.player.puntaje), (50,100), negro)
        
        self.all_plataformas.draw(self.pantalla) 
        self.enemigos_group.draw(self.pantalla)
        self.player.draw(self.pantalla)
    
        for plataforma in self.all_plataformas:
            plataforma.mover_verticalmente()
            plataforma.draw(self.pantalla)

        pygame.draw.rect(self.pantalla, verde, self.player.rect_golpe)

        pygame.display.flip()

    def close(self):
        pygame.quit()
        exit()

juego = Juego()
juego.run()
        