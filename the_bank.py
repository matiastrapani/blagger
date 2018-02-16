import pygame, sys
from levels import level3 as level
import blaggerPlayer, baddiesPlayer

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

screen = pygame.display.set_mode((640, 480))
fondo = pygame.Surface((640,480))

font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('The Bank')

game_over = False
clktcks = 40
blagger_sounds = True
keys = 0

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
for y, valY in enumerate(level):
    for x, valX in enumerate(level[y]):
        tile = tiles.subsurface(bricks[valX])
        fondo.blit(tile, (int(x * 16),int(y * 16)))
        if valX == 33:
            keys += 1
        if valX == 38:
            bloque1 += (int(x * 16),int(y * 16)),
        if valX == 78:
            bloque2 += (int(x * 16),int(y * 16)),
fondo.set_colorkey(transColor)

blagger = blaggerPlayer.Spr((240+16*10, 148-16*6), sprites)

badGuy = baddiesPlayer.Spr((22+16*11,-13+16*18), sprites, 'waldo', 3, (181,239,148), 195, 367)
idx = 0
tile = animTiles.subsurface(animIndex[idx])

#carga sonidos
pygame.mixer.init()
key_sound = pygame.mixer.Sound('wav/blagger_llave.wav')
step_sound = pygame.mixer.Sound('wav/blagger_paso.wav')
fall_sound = pygame.mixer.Sound('wav/blagger_caida.wav')
jump_sound = pygame.mixer.Sound('wav/blagger_salto.wav')

clock = pygame.time.Clock()

while blagger.game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
    blagger.handle_event(event, level)
    badGuy.update()
    screen.fill((0,0,0))

    if blagger_sounds:
        if blagger.sound == 'jump':
            jump_sound.stop()
            jump_sound.play()
            blagger.sound = ''
            
        if blagger.sound == 'step':
            if blagger.frame == 4:
                step_sound.play()
            blagger.sound = ''

        if blagger.sound == 'fall' and blagger.fallcount == 1:
            fall_sound.play()
            blagger.sound = ''
            
        if blagger.sound == 'stop_fall':
            fall_sound.stop()
            blagger.sound = ''

        if blagger.sound == 'key':
            key_sound.stop()
            key_sound.play()
            blagger.sound = ''
        
    if blagger.fallcount > 32:
        blagger.image.set_palette_at(3,(255,0,0))
        
    screen.blit(blagger.image, blagger.rect)
    
    i,j = blagger.get_levelPos()
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

    screen.blit(fondo, (0,0))
                        
    #pygame.draw.rect(screen, (255, 255, 255), (i*16,j*16,16,16), 1)
    #pygame.draw.rect(screen, (255,0, 0), ((blagger.posX-7)//16*16,(blagger.posY//16+1)*16,32,16), 1)
    tile = animTiles.subsurface(animIndex[idx])
    for pos in bloque1:
        screen.blit(tile, pos)

    tile = animTiles.subsurface(animIndex[idx+16])
    for pos in bloque2:
        screen.blit(tile, pos)
    screen.blit(badGuy.image, badGuy.rect)

    pygame.display.flip()
    clock.tick(clktcks)
    idx += 1
    if idx>15:
        idx = 0
        

print ('game over')
pygame.mixer.stop()
pygame.quit()
sys.exit()
