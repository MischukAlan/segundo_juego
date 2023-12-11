import threading
import time

def imprimir_linea_1():
    print("Primera línea")

def imprimir_linea_2():
    time.sleep(2)
    print("Segunda línea después de 2 segundos")

def imprimir_linea_3():
    print("Tercera línea")

# Crear tres threads
thread_1 = threading.Thread(target=imprimir_linea_1)
thread_2 = threading.Thread(target=imprimir_linea_2)
thread_3 = threading.Thread(target=imprimir_linea_3)

# Iniciar los threads en el orden que deseas
thread_1.start()
thread_3.start()
thread_2.start()

# Esperar a que todos los threads terminen
thread_1.join()
thread_2.join()
thread_3.join()