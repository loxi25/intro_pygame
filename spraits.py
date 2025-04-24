# En gráficos de computadora y videojuegos, un "sprite" es una imagen o animación bidimensional que se integra en una escena más grande. Suelen representar personajes, objetos o efectos especiales. Los sprites, en el contexto de los videojuegos, se han convertido en un término fundamental para la creación de personajes y objetos en movimiento en juegos 2D

import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ANCHO = 600
ALTO = 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Evita los obstáculos")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Jugador
jugador_ancho = 50
jugador_alto = 50
jugador_x = ANCHO // 2 - jugador_ancho // 2
jugador_y = ALTO - jugador_alto - 10
jugador_velocidad = 7

# Obstáculos
obstaculos = []
obstaculo_ancho = 50
obstaculo_alto = 50
obstaculo_velocidad = 5
frecuencia_obstaculo = 30  # cada X frames

# Reloj
clock = pygame.time.Clock()
FPS = 60

# Puntuación
puntuacion = 0
fuente = pygame.font.SysFont(None, 36)

def mostrar_puntuacion():
    texto = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    ventana.blit(texto, (10, 10))

# Loop del juego
frame_count = 0
jugando = True
while jugando:
    clock.tick(FPS)
    ventana.fill(NEGRO)

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= jugador_velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_ancho:
        jugador_x += jugador_velocidad

    # Crear obstáculos
    if frame_count % frecuencia_obstaculo == 0:
        x_aleatorio = random.randint(0, ANCHO - obstaculo_ancho)
        obstaculos.append(pygame.Rect(x_aleatorio, 0, obstaculo_ancho, obstaculo_alto))

    # Mover obstáculos
    for obstaculo in obstaculos[:]:
        obstaculo.y += obstaculo_velocidad
        if obstaculo.y > ALTO:
            obstaculos.remove(obstaculo)
            puntuacion += 1
        if obstaculo.colliderect(pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)):
            jugando = False

    # Dibujar jugador
    pygame.draw.rect(ventana, BLANCO, (jugador_x, jugador_y, jugador_ancho, jugador_alto))

    # Dibujar obstáculos
    for obstaculo in obstaculos:
        pygame.draw.rect(ventana, ROJO, obstaculo)

    # Mostrar puntuación
    mostrar_puntuacion()

    # Actualizar ventana
    pygame.display.flip()
    frame_count += 1

# Salir del juego
pygame.quit()
sys.exit()






