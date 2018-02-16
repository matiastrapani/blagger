import pygame, sys
from levels import *
from pygame.locals import *


pygame.init()
Esc = False
screen = pygame.display.set_mode((680, 580))
fondo = pygame.Surface((680,580))
screen.fill((255,0,0))
font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('Level Representation')


Sprites = pygame.image.load('blagger_tiles.png')

bricks = {}
for y in range(4):
    for x in range(32):
        bricks[int(x + y * 32)]  = (x * 16, y * 16, 16, 16)

for y, valY in enumerate(level3):
    for x, valX in enumerate(level3[y]):
        tile = Sprites.subsurface(bricks[valX])
        fondo.blit(tile, (int(x * 16),int(y * 16)))
    #print x
#print y
transColor = pygame.Color(0, 0, 0)
fondo.set_colorkey(transColor)

screen.blit(fondo,(0,0))
pygame.display.flip()
clock = pygame.time.Clock()




# Creo una lista vacia 
pressed_key_text = []
while Esc == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
    # Obtengo las teclas que el usuario presiona
    pressed_keys = pygame.key.get_pressed()
    for key_constant, pressed in enumerate(pressed_keys):
        if pressed:
            key_name = pygame.key.name(key_constant)
            if key_name == 'escape':
                Esc = True
    #clock.tick(clktcks)



pygame.quit()
sys.exit()
