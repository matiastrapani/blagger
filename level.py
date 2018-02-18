import pygame, sys
from levels import level as level3

pygame.init()
Esc = False
screen = pygame.display.set_mode((680, 580))
fondo = pygame.Surface((680,580))
screen.fill((0,0,0))
font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('Level Representation')

Sprites = pygame.image.load('img/blagger_tiles_.png')
animTiles = pygame.image.load('img/anim_tiles_.png')

brickIndex = {}
for y in range(4):
    for x in range(32):
        brickIndex[int(x + y * 32)]  = (x * 16, y * 16, 16, 16)

animIndex = {}
for y in range(5):
    for x in range(16):
        animIndex[int(x + y * 16)] = (x * 16, y * 16, 16, 16)       

bloque1=()
bloque2=()
for y, valY in enumerate(level3):
    for x, valX in enumerate(level3[y]):
        tile = Sprites.subsurface(brickIndex[valX])
        fondo.blit(tile, (int(x * 16),int(y * 16)))
        if valX == 38:
            bloque1 += (int(x * 16),int(y * 16)),
        if valX == 78:
            bloque2 += (int(x * 16),int(y * 16)),
       
transColor = pygame.Color(0, 0, 0)
fondo.set_colorkey(transColor)

screen.blit(fondo,(0,0))
pygame.display.flip()
clock = pygame.time.Clock()
clktcks = 50
idx = 0
tile = animTiles.subsurface(animIndex[idx])

pressed_key_text = []
while Esc == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
    pressed_keys = pygame.key.get_pressed()
    for key_constant, pressed in enumerate(pressed_keys):
        if pressed:
            key_name = pygame.key.name(key_constant)
            if key_name == 'escape':
                Esc = True

    screen.fill((0,0,0))
    screen.blit(fondo,(0,0))
    tile = animTiles.subsurface(animIndex[idx])
    
    for pos in bloque1:
        screen.blit(tile, pos)

    tile = animTiles.subsurface(animIndex[idx+16])
    for pos in bloque2:
        screen.blit(tile, pos)

    pygame.display.flip()
    idx += 1
    if idx>15:
        idx = 0

    clock.tick(clktcks)

pygame.quit()
sys.exit()
