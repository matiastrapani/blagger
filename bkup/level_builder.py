import pygame, sys
from pygame.locals import *
import brickPlayer


#level builder 
#	get tile
#	bug self.frame max y min
#	edit saved level

pygame.init()

screenRect = (31,19)
level = []
for y in range(screenRect[1]+1):
    n = bytearray()
    for x in range(screenRect[0]+1):
        n.append(32)
    level.append(n)

levels = tuple(level)


font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('The Level Builder')

game_over = False
clktcks = 25


Sprites = pygame.image.load('blagger_tiles.png')
tile = brickPlayer.Spr((8, 8), Sprites)
screen = pygame.display.set_mode((screenRect[0]*16, screenRect[1]*16))
fondo = pygame.Surface((screenRect[0]*16, screenRect[1]*16))

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
    clock.tick(clktcks)


print levels
pygame.quit()
sys.exit()
