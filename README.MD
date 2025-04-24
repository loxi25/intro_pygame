### funcion pyygame.event.wait
- esta funcion espera que ocurra un evento, y en cuanto sucede esta disponible.

```Python
while True
    event = pygame.event.wait()
    if event == pygame.QUIT: 
        break
```

### funcion pygame.event.poll
- devuelve solo uno de los eventos que estan en la cola de espera



## sonidos en pygame
- pygame.mixer: modulo que permite la gestion de sonido

- music: submodulo que gestiona la musica de fondo. necesariamente solo hay uno a la vez

- Sound: objeto de mixer, que se puede instanciar varias veces para usarlo en los efectos del sonido del juego.

### Archivo de sonido
- se recomienda usar dos formatos,principalmente:
    - formato WAV (Waveform audio file Format)
    - formato bierto y grtuito OGG


### chnne (canal) en pygame
- un juego tiene varios canales de sonido.
- se puede asignar un solo sonido al canal numero 1 y otro diferente al numero 2.
- entonces es posible

# SPRITES 
- bjeto que asocia una ubicacion,una representacion grafica (esta o aquella imagen) y un conjunto de propiedades,estas propiedades pueden ser un nombre, un texto, valores booleanos que caracterizan el objeto en cuestión (por ejemplo si el objeto se puede mover o no).
- Una posible traduccion del termino sprite podria ser "imagen-objeto" que se actualiza con cada interraccion del juego
- cuando mas complejo es el juego,mas objetos graficos tiene que gestionar y actualizar lo que puede ser tedioso.
- pygame usa no solo la nocon de sprite, sino la nocion de grupo de sprites (group)
- la nocion de grupo permite agrupar los objetos del mismo tipo. ejemplo : todos los soldados de un ejercito lo que se entiende como una colceccion de instancias de una clase Soldado 

- un determindado proceso se puede aplicaar a un conjunto o subconjunto de sprites. Ejemplo: cambiar el color de todos los enemigos o hacer invisibles algunos objetos



# explicacion de los SPRITES  
- import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
ancho = 400
alto = 300
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Sprite Simple")

# Cargar la imagen del sprite
try:
    sprite_img = pygame.image.load("cuadrado_rojo.png").convert_alpha()
except pygame.error as e:
    print(f"Error al cargar la imagen: {e}")
    sys.exit()

# Posición inicial del sprite
x = ancho // 2 - sprite_img.get_width() // 2
y = alto // 2 - sprite_img.get_height() // 2
velocidad = 5

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el sprite basado en las teclas
    if keys[pygame.K_LEFT]:
        x -= velocidad
    if keys[pygame.K_RIGHT]:
        x += velocidad
    if keys[pygame.K_UP]:
        y -= velocidad
    if keys[pygame.K_DOWN]:
        y += velocidad

    # Mantener el sprite dentro de los límites
    if x < 0:
        x = 0
    if x > ancho - sprite_img.get_width():
        x = ancho - sprite_img.get_width()
    if y < 0:
        y = 0
    if y > alto - sprite_img.get_height():
        y = alto - sprite_img.get_height()

    # Dibujar el fondo
    pantalla.fill((255, 255, 255))  # Fondo blanco

    # Dibujar el sprite en su nueva posición
    pantalla.blit(sprite_img, (x, y))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()

# que es un sprite ? 




