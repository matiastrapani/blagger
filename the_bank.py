import pygame, sys
from pygame.locals import *
from levels import *
import blaggerPlayer, baddiesPlayer

pygame.init()

screen = pygame.display.set_mode((640, 480))
fondo = pygame.Surface((640,480))

font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('The Bank')

game_over = False
clktcks = 40

transColor = pygame.Color(0, 0, 0)
sprites = pygame.image.load('img/blagger_sprites_.png')
sprites.set_colorkey(transColor)

tiles = pygame.image.load('img/blagger_tiles_.png')
animTiles = pygame.image.load('img/anim_tiles_.png')

#get level background
bricks = {}
for y in range(4):
    for x in range(32):
        bricks[int(x + y * 32)]  = (x * 16, y * 16, 16, 16)
animIndex = {}
for y in range(5):
    for x in range(16):
        animIndex[int(x + y * 16)] = (x * 16, y * 16, 16, 16)       

bloque1=()
bloque2=()
for y, valY in enumerate(level3):
    for x, valX in enumerate(level3[y]):
        tile = tiles.subsurface(bricks[valX])
        fondo.blit(tile, (int(x * 16),int(y * 16)))
        if valX == 38:
            bloque1 += (int(x * 16),int(y * 16)),
        if valX == 78:
            bloque2 += (int(x * 16),int(y * 16)),
fondo.set_colorkey(transColor)

blagger = blaggerPlayer.Spr((240, 148), sprites)

badGuy = baddiesPlayer.Spr((22+16*11,-13+16*18), sprites, 'waldo', 3, (181,239,148), 195, 367)
idx = 0
tile = animTiles.subsurface(animIndex[idx])

#badGuyJon = baddiesPlayer.Spr((19+16*11,-6+16*12), sprites, 'joni', (0,255,0), 195, 351)
#badGuyJon.dir = 'up'

#Sprites.set_palette_at(3,(255,0,0))
clock = pygame.time.Clock()
#pygame.time.set_timer(USEREVENT + 1, 100)

while blagger.game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
    blagger.handle_event(event, level3)
    badGuy.update()
#    badGuyJon.update()
    screen.fill((0,0,0))
    
    #if blagger.posX>320:
        #blagger.image.set_palette_at(3,(255,0,0))
        
    screen.blit(blagger.image, blagger.rect)
    screen.blit(fondo, (0,0))
    #pygame.draw.rect(screen, (255, 255, 255), (blagger.posX-7,blagger.posY-16,16,32), 1)
    #pygame.draw.rect(screen, (255,0, 0), ((blagger.posX-7)//16*16,(blagger.posY//16+1)*16,32,16), 1)
    tile = animTiles.subsurface(animIndex[idx])
    #if level4[blagger.posY//16+1][(blagger.posX-7)//16]==32 and \
       #level4[blagger.posY//16+1][(blagger.posX-7)//16+1]==32:
            #pass
            #print 'fall'
    for pos in bloque1:
        screen.blit(tile, pos)

    tile = animTiles.subsurface(animIndex[idx+16])
    for pos in bloque2:
        screen.blit(tile, pos)
    screen.blit(badGuy.image, badGuy.rect)
#    screen.blit(badGuyJon.image, badGuyJon.rect)

    pygame.display.flip()
    clock.tick(clktcks)
    idx += 1
    if idx>15:
        idx = 0

print ('game over')
pygame.quit()
sys.exit()
