import pygame
from pygame.locals import *
from config_2 import *
from main2 import Level_1
from main3 import Level_2
from boton import Boton

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Mi segundo jueguito')

        self.en_pausa = False
        self.nivel_actual = None

        self.menu_principal()

    def menu_principal(self):
        while True:
            # Crear botones
            play_button = Boton(300, 100, 100, 50, "Play", BLANCO, verde, rojo, None)
            selector_niveles_button = Boton(300, 200, 100, 50, "Selector de Niveles", BLANCO, verde, rojo, None)
            quit_button = Boton(300, 300, 100, 50, "Quit", BLANCO, verde, rojo, None)

            # Dibujar botones
            play_button.draw(self.pantalla)
            selector_niveles_button.draw(self.pantalla)
            quit_button.draw(self.pantalla)

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if play_button.rect.collidepoint(evento.pos):
                        self.ejecutar_nivel(Level_1())
                    elif selector_niveles_button.rect.collidepoint(evento.pos):
                        self.selector_niveles()
                    elif quit_button.rect.collidepoint(evento.pos):
                        pygame.quit()
                        exit()

    def selector_niveles(self):
        while True:
            # Crear botones de selección de niveles
            nivel_1_button = Boton(300, 100, 100, 50, "Nivel 1", BLANCO, verde, rojo, None)
            nivel_2_button = Boton(300, 200, 100, 50, "Nivel 2", BLANCO, verde, rojo, None)
            volver_button = Boton(300, 300, 100, 50, "Volver", BLANCO, verde, rojo, None)

            # Dibujar botones
            nivel_1_button.draw(self.pantalla)
            nivel_2_button.draw(self.pantalla)
            volver_button.draw(self.pantalla)

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if nivel_1_button.rect.collidepoint(evento.pos):
                        self.ejecutar_nivel(Level_1())
                    elif nivel_2_button.rect.collidepoint(evento.pos):
                        self.ejecutar_nivel(Level_2())
                    elif volver_button.rect.collidepoint(evento.pos):
                        self.menu_principal()

    def ejecutar_nivel(self, nivel):
        self.nivel_actual = nivel
        self.en_pausa = False
        while not self.en_pausa:
            nivel.run()

        if self.nivel_actual:
            self.nivel_actual.close()
            self.nivel_actual = None

    def pausa(self):
        while True:
            # Crear botones de pausa
            resumen_button = Boton(300, 100, 100, 50, "Resumen", BLANCO, verde, rojo, None)
            quit_button = Boton(300, 200, 100, 50, "Quit", BLANCO, verde, rojo, None)
            menu_principal_button = Boton(300, 300, 100, 50, "Menu Principal", BLANCO, verde, rojo, None)
            selector_niveles_button = Boton(300, 400, 150, 50, "Selector de Niveles", BLANCO, verde, rojo, None)
            nivel_3_button = Boton(300, 500, 100, 50, "Nivel 3", BLANCO, verde, rojo, None)
            nivel_4_button = Boton(300, 600, 100, 50, "Nivel 4", BLANCO, verde, rojo, None)

            # Dibujar botones
            resumen_button.draw(self.pantalla)
            quit_button.draw(self.pantalla)
            menu_principal_button.draw(self.pantalla)
            selector_niveles_button.draw(self.pantalla)
            nivel_3_button.draw(self.pantalla)
            nivel_4_button.draw(self.pantalla)

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if resumen_button.rect.collidepoint(evento.pos):
                        self.en_pausa = False
                    elif quit_button.rect.collidepoint(evento.pos):
                        pygame.quit()
                        exit()
                    elif menu_principal_button.rect.collidepoint(evento.pos):
                        self.en_pausa = False
                        if self.nivel_actual:
                            self.nivel_actual.close()
                            self.nivel_actual = None
                        self.menu_principal()
                    elif selector_niveles_button.rect.collidepoint(evento.pos):
                        self.en_pausa = False
                        if self.nivel_actual:
                            self.nivel_actual.close()
                            self.nivel_actual = None
                        self.selector_niveles()
                    elif nivel_3_button.rect.collidepoint(evento.pos):
                        self.en_pausa = False
                        if self.nivel_actual:
                            self.nivel_actual.close()
                            self.nivel_actual = None
                        self.ejecutar_nivel(Level_3())  # Reemplaza con el nivel que desees
                    elif nivel_4_button.rect.collidepoint(evento.pos):
                        self.en_pausa = False
                        if self.nivel_actual:
                            self.nivel_actual.close()
                            self.nivel_actual = None
                        self.ejecutar_nivel(Level_4())

if __name__ == "__main__":
    juego = Juego()