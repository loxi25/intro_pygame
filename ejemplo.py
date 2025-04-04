# importamos la libreria pygames

import pygame
import random

# inicializamos los modulos de pygame 

pygame.init

# establecer titulo a la ventana 
pygame.display.set_caption("surface")

# establecemos las dimensiones de la ventana 
ventana = pygame.display.set_mode((400,400))

# definimos un color 
azul = random.randint(0, 256)
rojo = random.randint(0,250)
verde = random.randint(0,250)

# crear una superficie 
azul_Superficie = pygame.Surface((300,300))

# rellenamos la superficie de azul
azul_Superficie.fill(azul)

# inserto o muevo la ventana  la superficie en la ventana
ventana.blit(azul_Superficie, (0,0))

# actualiza la visualizacion de la ventana 
pygame.display.flip()

# bucle del juego
while True: 
    event = pygame.event.wait()
    if event ==pygame.QUIT: 
        break 

pygame.quit()