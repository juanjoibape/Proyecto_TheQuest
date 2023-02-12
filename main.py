#Crear juego con pygame

#importando libreria e iniciandola
import pygame

import sys

pygame.init

#definir colores
NEGRO   = (  0,   0,   0)
BLANCO  = (255, 255, 255)
VERDE   = (  0, 255,   0)
ROJO    = (255,   0,   0)
AZUL    = (  0,   0, 255)

#crear ventana y sus dimnensiones
PANTALLA = pygame.display.set_mode((800, 500))
#añadir nombre del juego
pygame.display.set_caption("TheQuest")
#pintar pantalla
PANTALLA.fill(BLANCO)

#pintar un rectángulo
pygame.draw.rect(PANTALLA, AZUL, (350, 400, 60, 40))
#pintar cirulo
pygame.draw.circle(PANTALLA, ROJO, (100, 100), 10, 0)

#mantener ventana abierta y poder cerrar, bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
