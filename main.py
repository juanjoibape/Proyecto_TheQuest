#Crear juego con pygame

#importando libreria e iniciandola
import pygame
pygame.init

import sys

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
#self.image.fill(WHITE)

FPS = 30

#coordenadas rectángulo
#cord_x = 400
#cord_y = 200

#velocidad a la que mueve el rectángulo
#speed_x = 3
#speed_y = 3

#mantener ventana abierta y poder cerrar, bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#pintar fondo de pantalla

#sprite del jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #rectángulo jugador
        self.image = pygame.Surface((200, 200))
        self.image.fill(RED)
        # obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # posicion del rectángulo
        self.rect.center = (400, 100)

        def update(self):
            #actualiza cada bucle
            self.rect.y += 10
            if self.rect.top > ALTO:
                self.rect.bottom = 0
