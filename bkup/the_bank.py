import pygame, sys
from pygame.locals import *
from levels import *
import blaggerPlayer

pygame.init()

screen = pygame.display.set_mode((640, 480))
fondo = pygame.Surface((640,480))

font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('The Bank')

game_over = False
clktcks = 35

transColor = pygame.Color(0, 0, 0)
sprites = pygame.image.load('blagger_sprites_.png')
sprites.set_colorkey(transColor)

tiles = pygame.image.load('blagger_tiles_.png')

#get level background
bricks = {}
for y in range(4):
    for x in range(32):
        bricks[int(x + y * 32)]  = (x * 16, y * 16, 16, 16)

for y, valY in enumerate(level3):
    for x, valX in enumerate(level3[y]):
        tile = tiles.subsurface(bricks[valX])
        fondo.blit(tile, (int(x * 16),int(y * 16)))

fondo.set_colorkey(transColor)

blagger = blaggerPlayer.Spr((148, 148), sprites)
#Sprites.set_palette_at(3,(255,0,0))
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT + 1, 100)

while blagger.game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
    blagger.handle_event(event)
    screen.fill((0,0,0))
    
    if blagger.posX>320:
        blagger.image.set_palette_at(3,(255,0,0))
        
    screen.blit(blagger.image, blagger.rect)
    screen.blit(fondo, (0,0))
    pygame.display.flip()
    clock.tick(clktcks)

print 'game over'
