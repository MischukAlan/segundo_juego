from pygame.locals import *
from main2 import Level_1
from main3 import Level_2
from main4 import Level_3


class ManejadorNiveles:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.niveles = {"Nivel_uno" : Level_1 , "Nivel_2":Level_2, "Nivel_3":Level_3}

    def get_niveles(self, nombre_nivel):
        return self.niveles[nombre_nivel](self.niveles)

