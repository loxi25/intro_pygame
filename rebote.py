import pygame
import sys 

rojo = (255,0)

azul = ( 0,0 ,255)

pygame.init()

ventana = pygame.display.set_mode(400,400)

pygame.display.set_caption("el cuadrado  que rebota ")

clock = pygame.time.Clock()

xx = 300 
MOVIMIENTO = 3

while 1 :
    clock.tick(50)


for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()

    ventana.fill(azul)

xx = xx +MOVIMIENTO


if xx >= 320:
    xx = 320
    MOVIMIENTO = 3 
elif xx <= 0:
    xx = 0
    MOVIMIENTO = 3 

pygame.draw.rect(ventana,rojo ,(xx , 200 , 80 ))
pygame.display.flip()
    