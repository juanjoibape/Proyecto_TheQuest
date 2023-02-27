
#importar librerias
import pygame as pg
import random

W = 800
H = 600

#iniciar pygame
pg.init()

#iniciar musica
pg.mixer.init()

#crear pantalla
pantalla = pg.display.set_mode((W, H))
pg.display.set_caption("TheQuest")
clock = pg.time.Clock()

#musica de fondo
pg.mixer.music.load("musica/Intergalactic_Odyssey.ogg")
pg.mixer.music.play(-1)

#crear nave jugador
class Nave(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pg.image.load("imagenes/nave1.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = W // 2
		self.rect.bottom = H - 10
		self.speed_x = 0

	def update(self):
		self.speed_x = 0
		keystate = pg.key.get_pressed()
		if keystate[pg.K_LEFT]:
			self.speed_x = -5
		if keystate[pg.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > W:
			self.rect.right = W
		if self.rect.left < 0:
			self.rect.left = 0

#crear meteoritos enemigos
class Meteorito(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pg.image.load("imagenes/meteorito2.png")
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(W - self.rect.w)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 22 :
			self.rect.x = random.randrange(W - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)
			
#cargar fondo
fondo = pg.image.load("imagenes/fondo_galaxia2.png")

#cargar nave y meteoritos
all_sprites = pg.sprite.Group()
meteorito_list = pg.sprite.Group()

Nave = Nave()
all_sprites.add(Nave)

for i in range(10):
	meteorito = Meteorito()
	all_sprites.add(meteorito)
	meteorito_list.add(meteorito)

#bucle principal
running = True
while running:
	clock.tick(60)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		

	# actualizar nave y meteoritos
	all_sprites.update()
	'''
	colision = pg.sprite.spritecollide(Nave, meteorito_list, False)
	if colision:
		meteorito.image = pg.image.load("imagenes/explosion.png")
	'''
    #pintar pantalla y fondo
	pantalla.blit(fondo, [0, 0])
	all_sprites.draw(pantalla)
        
	pg.display.flip()

pg.quit()