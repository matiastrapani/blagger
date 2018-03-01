import pygame, sys
from levels import levels, levelSprites
import blaggerPlayer, baddiesPlayer
from copy import deepcopy

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

#carga sonidos
pygame.mixer.init()
key_sound = pygame.mixer.Sound('wav/blagger_llave.wav')
step_sound = pygame.mixer.Sound('wav/blagger_paso.wav')
fall_sound = pygame.mixer.Sound('wav/blagger_caida.wav')
jump_sound = pygame.mixer.Sound('wav/blagger_salto.wav')
live_sound = pygame.mixer.Sound('wav/blagger_vida.wav')

#carga pantalla
screen = pygame.display.set_mode((640, 480))
fondo = pygame.Surface((640,480))
font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('The Bank')

#variables
lNro = 0
level = deepcopy(levels[lNro])
lSpr = levelSprites[lNro]
game_over = False
clktcks = 40
blagger_sounds = True
clock = pygame.time.Clock()
tmr = pygame.time.get_ticks()

#carga sprites y tiles
transColor = pygame.Color(0, 0, 0)
sprites = pygame.image.load('img/blagger_sprites_.png')
sprites.set_colorkey(transColor)

tiles = pygame.image.load('img/blagger_tiles_.png')
animTiles = pygame.image.load('img/anim_tiles_.png')
animTiles.set_colorkey(transColor)

#carga tiles
bricks = {}
for y in range(4):
    for x in range(32):
        bricks[int(x + y * 32)]  = (x * 16, y * 16, 16, 16)
animIndex = {}
for y in range(5):
    for x in range(16):
        animIndex[int(x + y * 16)] = (x * 16, y * 16, 16, 16)       
#-------------------------------------------------------------------------

#carga fondo de nivel
def bloques(level, fondo, bricks):
    bloque1 = ()
    bloque2 = ()
    bloque3 = ()
    keys = 0
    fondo.fill((0,0,0))
    for y, valY in enumerate(level):
        for x, valX in enumerate(level[y]):
            if valX != 38 and valX != 78 and valX != 42 and valX<128:
                tile = tiles.subsurface(bricks[valX])
                fondo.blit(tile, (int(x * 16),int(y * 16)))
            if valX == 33:
                keys += 1
            if valX == 38:
                bloque1 += (int(x * 16),int(y * 16)),
            if valX == 78:
                bloque2 += (int(x * 16),int(y * 16)),
            if valX == 42:
                bloque3 += (int(x * 16),int(y * 16)),
    fondo.set_colorkey(transColor)
    return keys, bloque1, bloque2, bloque3

#inica los sprites
blagger = blaggerPlayer.Spr(sprites, **lSpr[0])
safe = blaggerPlayer.Safe(sprites, **lSpr[1])
badGuys = []
for badspr in lSpr[2:]:
    badGuys.append(baddiesPlayer.Spr(sprites, **badspr))

keys = 0
bloque1 = ()
bloque2 = ()
bloque3 = ()
keys, bloque1, bloque2, bloque3 = bloques (level, fondo, bricks)

fondo.blit(safe.image, safe.rect)

idx = 0
n = 0
#loop principal
while blagger.game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
    #blagger update
    blagger.handle_event(event, level)
    #bad guys update
    for badGuy in badGuys:
        badGuy.update()

        
    #plataformas fragiles
    i,j = blagger.get_levelPos()
    if (blagger.posY-4)%16 == 0 and blagger.jumpcount == 0 and (level[j + 1][i] == 106 or 144 >= level[j + 1][i]  >= 128):
        if level[j + 1][i] == 106:
            level[j + 1][i] = 130
        elif level[j + 1][i] <= 143:
            level[j + 1][i] += 2
        if level[j + 1][i] > 142:
            level[j + 1][i] = 32
            tile = tiles.subsurface(bricks[32])
        else:
            tile = animTiles.subsurface(animIndex[32+ level[j + 1][i] - 128])
        fondo.fill((0,0,0),(i * 16,(j + 1)*16,16,16))
        fondo.blit(tile, (i * 16,(j + 1)*16))

    if (blagger.posY-4)%16 == 0 and blagger.jumpcount == 0 and (level[j + 1][i + 1] == 106 or 144 >= level[j + 1][i + 1]  >= 128):
        if level[j + 1][i + 1] == 106:
            level[j + 1][i + 1] = 130
        elif level[j + 1][i + 1] <= 143:
            level[j + 1][i + 1] += 2
        if level[j + 1][i + 1] > 142:
            level[j + 1][i + 1] = 32
            tile = tiles.subsurface(bricks[32])
        else:
            #32-47
            tile = animTiles.subsurface(animIndex[32+ level[j + 1][i + 1] - 128])
        fondo.fill((0,0,0),((i + 1) * 16,(j + 1)*16,16,16))
        fondo.blit(tile, ((i + 1) * 16,(j + 1)*16))
    
    #get keys
    if level[j][i] == 33:
        keys -= 1
        level[j][i] = 32
        fondo.fill((0,0,0),(i*16,j*16,16,16))
        if blagger_sounds:
            key_sound.stop()
            key_sound.play()

    elif level[j-1][i] == 33:
        keys -= 1
        level[j-1][i] = 32
        fondo.fill((0,0,0),(i*16,(j-1)*16,16,16))
        if blagger_sounds:
            key_sound.stop()
            key_sound.play()

    elif level[j][i+1] == 33:
        keys -= 1
        level[j][i+1] = 32
        fondo.fill((0,0,0),((i+1)*16,j*16,16,16))
        if blagger_sounds:
            key_sound.stop()
            key_sound.play()

    elif level[j-1][i+1] == 33:
        keys -= 1
        level[j-1][i+1] = 32
        fondo.fill((0,0,0),((i+1)*16,(j-1)*16,16,16))
        if blagger_sounds:
            key_sound.stop()
            key_sound.play()

    #sprite collision
    #pygame.draw.rect(screen, (255,0, 0), safe.rect, 1)
    for badGuy in badGuys:
        #pygame.draw.rect(screen, (255,0, 0), badGuy.sprCol, 1)
        if blagger.sprCol.colliderect(badGuy.sprCol):
            n += 1
            print 'collide: ', n
            blagger.sound = 'lives'

    #safe collision
    if safe.rect.collidepoint(blagger.sprCol.center):
        lNro += 1
        lSpr = levelSprites[lNro]
        level = deepcopy(levels[lNro])
        
        blagger = blaggerPlayer.Spr(sprites, **lSpr[0])
        safe = blaggerPlayer.Safe(sprites, **lSpr[1])
        badGuys = []
        for badspr in lSpr[2:]:
            badGuys.append(baddiesPlayer.Spr(sprites, **badspr))
            
        bloque1 = ()
        bloque2 = ()
        bloque3 = ()
        keys = 0
        keys, bloque1, bloque2, bloque3 = bloques (level, fondo, bricks)
        
        fondo.blit(safe.image, safe.rect)
        blagger.update(level)

    screen.fill((0,0,0))
    if blagger.fallcount > 32:
        blagger.image.set_palette_at(3,(255,0,0))
    screen.blit(blagger.image, blagger.rect)
    screen.blit(fondo, (0,0))
    #bad guys sprites 
    for badGuy in badGuys:
        screen.blit(badGuy.image, badGuy.rect)
    
    #pygame.draw.rect(screen, (255, 255, 255), (i*16,(j+1)*16,32,16), 1)
    #pygame.draw.rect(screen, (255,0, 0), (((blagger.posX-7)//16)*16,(blagger.posY//16-2)*16,32,16), 1)
    #pygame.draw.rect(screen, (255,0, 0), (blagger.posX-7, blagger.posY-32+12,16,1), 1)
    
    #tiles animados
    tile = animTiles.subsurface(animIndex[idx])
    for pos in bloque1:
        screen.blit(tile, pos)

    tile = animTiles.subsurface(animIndex[idx+16])
    for pos in bloque2:
        screen.blit(tile, pos)

    tile = animTiles.subsurface(animIndex[idx+64])
    for pos in bloque3:
        screen.blit(tile, pos)
    idx += 1
    if idx>15:
        idx = 0

    if blagger_sounds:
            if blagger.sound == 'jump':
                jump_sound.stop()
                jump_sound.play()
                blagger.sound = ''
                
            if blagger.sound == 'step':
                if blagger.frame == 4:
                    step_sound.play()
                blagger.sound = ''

            if blagger.sound == 'fall':
                fall_sound.play()
                blagger.sound = ''
                
            if blagger.sound == 'stop_fall':
                fall_sound.stop()
                blagger.sound = ''

            if blagger.sound == 'key':
                key_sound.stop()
                key_sound.play()
                blagger.sound = ''

            clk = pygame.time.get_ticks()
            if blagger.sound == 'lives' and clk-tmr > 2000:
                tmr = pygame.time.get_ticks()
                live_sound.play()
                blagger.sound = ''
                blagger.fallcount = 0
                blagger.lives -= 1

    pygame.display.flip()
    clock.tick(clktcks)

print ('game over')
pygame.mixer.stop()
pygame.quit()
sys.exit()
