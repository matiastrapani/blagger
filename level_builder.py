import pygame, sys
from pygame.locals import *
import brickPlayer

#level builder 
#	get tile
#	bug self.frame max y min
#	edit saved level


# Controles
# teclas de cursor
# a y z para cambiar el tile
# spacebar para aplicar
# backspace para borrar
# tab para tomar tile 

pygame.init()

Sprites = pygame.image.load('blagger_tiles.png')


if False:
    screenRect = (31,19)
    level = []
    for y in range(screenRect[1]+1):
        n = bytearray()
        for x in range(screenRect[0]+1):
            n.append(32)
        level.append(n)

    levels = tuple(level)
    level = []
    screen = pygame.display.set_mode((screenRect[0]*16, screenRect[1]*16))
    fondo = pygame.Surface((screenRect[0]*16, screenRect[1]*16))
else:
    from levels import *
    #get level background
    bricks = {}
    for y in range(4):
        for x in range(32):
            bricks[int(x + y * 32)]  = (x * 16, y * 16, 16, 16)

    levels = level3
    screenRect = (len(levels[0]),len(levels))
    screen = pygame.display.set_mode((screenRect[0]*16, screenRect[1]*16))
    fondo = pygame.Surface((screenRect[0]*16, screenRect[1]*16))
    for y, valY in enumerate(levels):
        for x, valX in enumerate(levels[y]):
            tile = Sprites.subsurface(bricks[valX])
            fondo.blit(tile, (int(x * 16),int(y * 16)))
    

font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('The Level Builder')

game_over = False
clktcks = 25


tile = brickPlayer.Spr((8, 8), Sprites)


clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT + 1, 100)

while tile.game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
    tile.handle_event(event)
    #screen.fill((0,0,0))
    screen.blit(fondo, (0, 0))
    screen.blit(tile.image, tile.rect)
    pygame.draw.rect(screen,(255,255,255),tile.rect,1)
    pygame.display.flip()
    if tile.action == 'set':
        tile.action = ''
        fondo.blit(tile.image, tile.rect)
        levels[tile.posY//16][tile.posX//16] = tile.frame
    elif tile.action == 'unset':
        tile.action = ''
        fondo.fill((0,0,0), tile.rect)
        levels[tile.posY//16][tile.posX//16] = 32
    elif tile.action == 'get':
        tile.action = ''
        tile.frame = levels[tile.posY//16][tile.posX//16]
    clock.tick(clktcks)


print levels
pygame.quit()
sys.exit()
