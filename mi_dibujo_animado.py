import pygame
import sys
import math
import random 


rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (225,225,225)
naranja = (255,165,0)
cian = (0, 255, 255)
gris = (127, 140, 141)
azulo = (33, 47, 60 )
pygame.init()

ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("tren ")

clock = pygame.time.Clock()



llantas = [(450, 300), (350, 300), (250, 300), (160, 250)]
radio_llanta = 50
angulo = 0



def dibujar_llanta_con_rayos(surface, centro, radio, angulo, rayos=6):
    pygame.draw.circle(surface, negro, centro, radio)
    for i in range(rayos):
        a = math.radians(angulo + (360 / rayos) * i)
        x = centro[0] + int((radio - 5) * math.cos(a))
        y = centro[1] + int((radio - 5) * math.sin(a))
        pygame.draw.line(surface, gris, centro, (x, y), 2)

rect_x = 70 
rect_y = 20
rect_w = 500
rect_h = 500

while 1:
    clock.tick(10)
    ventana.fill(azul)

    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("Colegio Guanenta", 1, negro)
    ventana.blit(texto, (70, 30))
    texto = fuente_arial.render("sistemas ", 1, negro )
    ventana.blit(texto, (70, 70))
    texto = fuente_arial.render("oscar sanchez ", 1,negro )
    ventana.blit(texto, (70, 400))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
  
# aaaaaa

    pygame.draw.rect(ventana, blanco, ((rect_x, rect_y), (rect_w, rect_h)), 1)
    pygame.draw.rect(ventana, gris , (200,200, 300,100))
    pygame.draw.rect(ventana, blanco, ( 350, 100 ,  150 , 100))
    pygame.draw.rect(ventana, azulo , (325, 70 , 200 , 50 ))
    pygame.draw.rect(ventana, gris , ( 375, 130 , 100   , 50  ))
    pygame.draw.circle(ventana, negro , (450,300),50,70)
    pygame.draw.circle(ventana, negro , (350,300),50,70)
    pygame.draw.circle(ventana, negro , (250,300),50,70)
    pygame.draw.circle(ventana, negro , (160,250),40,40)
    pygame.draw.rect(ventana, blanco , (220, 125 , 70  , 25 ))
    pygame.draw.rect(ventana, azulo , (240, 150 , 25  , 50 ))
    pygame.draw.rect(ventana, blanco , (175   , 205 , 25, 80 ))

    for centro in llantas:
        dibujar_llanta_con_rayos(ventana, centro, radio_llanta, angulo)

# Emoji en la ventana
    pygame.draw.circle(ventana, amarillo, (440, 160), 30)         
    pygame.draw.circle(ventana, blanco, (408, 160), 7)            
    pygame.draw.circle(ventana, blanco, (432, 160), 7)            
    pygame.draw.circle(ventana, negro, (408, 160), 3)             
    pygame.draw.circle(ventana, negro, (432, 160), 3)            
    pygame.draw.circle(ventana, rojo, (420, 175), 9)              
    pygame.draw.rect(ventana, azulo , (410, 130 , 50 , 8 ))
    pygame.draw.rect(ventana, azulo , (425, 128 , 35 , 8 ))
    
    angulo = (angulo + 5) % 360

    pygame.display.flip()

