#Crear juego con pygame

#importando libreria e iniciandola
import pygame
pygame.init

#definir colores
BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
GREEN   = (  0, 255,   0)
RED     = (255,   0,   0)
BLUE    = (  0,   0, 255)

#dimensiones ventana
size = (800, 500)

#crear ventana
screen = pygame.display.set_mode(size)

#coordenadas cuadrado
cord_x = 400
cord_y = 200

#velocidad a la que mueve el cuadrado
speed_x = 3
speed_y = 3

#mantener ventana abierta y poder cerrar, bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#pintar fondo de pantalla

