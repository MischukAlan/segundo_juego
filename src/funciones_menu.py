import pygame
from pygame.locals import *
from label import *
from boton import Boton
from config_2 import *
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configuración de la pantalla

pygame.display.set_caption("Menú Principal")

font = pygame.font.Font(None, 36)

def main_menu(screen):
    while True:
        screen.fill(BLACK)
        boton_nueva_partida = Boton(300, 100, 100,100, "Nueva partida", WHITE, verde, rojo, None)
        boton_levels = Boton(300, 300, 100,100, "LEVELS", WHITE, verde, rojo, None)
        boton_quit = Boton(300, 500, 100,100, "quit", WHITE, verde, rojo, None)

        niveles = Boton(300, 500, 100,100, "quit", WHITE, verde, rojo, None)
        # boton_quit = Boton(300, 500, 200,100, "quit", BLANCO, verde, rojo, No rojo
        
        # Verificar clic del mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        boton_nueva_partida.draw(screen)
        boton_levels.draw(screen)
        boton_quit.draw(screen)

        if boton_nueva_partida.flag:
            return 1

        if boton_levels.flag:
            return 2
        
        if boton_quit.flag:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
 
def levels(screen):
    while True:
        # levels = Label(300, 50, "niveles", 24, WHITE)
        juego = 0
        level_1 = Boton(300, 100, 100,100, "level_1", WHITE, verde, rojo, None)
        level_2 = Boton(300, 300, 100,100, "level_2", WHITE, verde, rojo, None)
        level_3 = Boton(300, 500, 100,100, "level_3", WHITE, verde, rojo, None)

        back = Boton(50, 50, 100,100, "back", WHITE, verde,  rojo, None)
        # Obtener posición del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Verificar clic del mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if back.rect.collidepoint(mouse_x, mouse_y):
                        main_menu(screen)
                    elif level_1.rect.collidepoint(mouse_x, mouse_y):
                        print("hola")
                        juego = 1
                        
                    elif level_2.rect.collidepoint(mouse_x, mouse_y):
                        print("hola")
                        juego = 2
                        
                    elif level_3.rect.collidepoint(mouse_x, mouse_y):
                        print("hola")
                        juego = 3

                    return juego    

                    
        level_1.draw(screen)
        level_2.draw(screen)
        level_3.draw(screen)
        back.draw(screen)

        pygame.display.flip()