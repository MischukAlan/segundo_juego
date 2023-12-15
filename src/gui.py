import pygame
from pygame.locals import *
from label import *
from boton import Boton
from config_2 import *
from funciones_menu import *
from main2 import Level_1
from main3 import Level_2
from main4 import Level_3

pygame.init()

class Juego:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.correr = True
        self.nivel_actual = Level_1()

    def run(self):
        menu = True
        while self.correr:
            self.screen.fill(BLACK)
            opcion = main_menu(self.screen)
            if opcion == 1:
                print("estoy aca")
                nivel_1 = Level_1()
                print(nivel_1)
                # self.nivel_actual = get_niveles(self, )
                if nivel_1.run():
                    print("gane")
                    nivel_2 = Level_2()
                    nivel_2.run()

                
                
            elif opcion == 2:
                nivel = levels(self.screen)
                if nivel == 1:
                    nivel = Level_1()
                    nivel.run()
                if nivel == 2:
                    nivel = Level_2()
                    nivel.run()
                if nivel == 3:
                    nivel = Level_3()
                    nivel.run()   
    
iniciar = Juego()
iniciar.run()

