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