import pygame, sys
import brickPlayer
from copy import deepcopy

# Controles
# teclas de cursor
# a y z para cambiar el tile
# spacebar para aplicar
# backspace para borrar
# return para tomar tile 
# tab para cambiar sprite


pygame.init()

Tiles = pygame.image.load('img/blagger_tiles_.png')
Sprites = pygame.image.load('img/blagger_sprites_.png')

transColor = pygame.Color(0, 0, 0)

blagger = pygame.Surface((48,41))
bPos = pygame.Rect(0,0,48,41)
blagger.set_colorkey(transColor)

badGuys = []
badGuy = pygame.Surface((48,41))
badGuyPos = pygame.Rect(0,0,48,41)
badGuy.set_colorkey(transColor)


safe = pygame.Surface((41,26))
safePos = pygame.Rect(0,0,41,26)
safe.set_colorkey(transColor)

levelSprites = [{},{},{}]
tile = brickPlayer.Spr((0, 0), Tiles, Sprites)

#True para empezar de cero
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
    #seleccionar nivel a editar
    from levels import levels as level
    from levels import levelSprites as levelSprite
    
    bricks = {}
    for y in range(4):
        for x in range(32):
            bricks[int(x + y * 32)]  = (x * 16, y * 16, 16, 16)


    levels = level[1]
    levelSprites = levelSprite [1]

    tile.tab_sprite()
    tile.frame = 0
    try:
        if levelSprites[0]['direction'] == 'stand_left':
            tile.frame = 1
    except Exception as e:
        pass
        
    tile.update()
    blagger = tile.image
    bPos = pygame.Rect (0,0,48,41)
    bPos.center = levelSprites[0]['position']
       
    tile.tab_sprite()
    tile.update()
    safe = tile.image
    safePos = pygame.Rect (0,0,41,26)
    safePos.center = levelSprites[1]['position']
    
    tile.tab_sprite()
    for bad in levelSprites[2:]:
        tile.frame = 0
        try:
            tile.frame = bad['nro']-1
        except Exception as e:
            pass
        
        tile.update()
        badGuy = tile.image
        badGuyPos = pygame.Rect (0,0,48,41)
        badGuyPos.center = bad['position']
        if bad['endpoints'][1] < bad['endpoints'][0]:
            bad['endpoints'][0], bad['endpoints'][1] = bad['endpoints'][1], bad['endpoints'][0]
        if bad['direction'] == 'right' or bad['direction'] == 'left':
            badGuyEP = pygame.Rect(bad['endpoints'][0] - badGuyPos.width // 2, badGuyPos.top, (bad['endpoints'][1] - bad['endpoints'][0]) + badGuyPos.width, badGuyPos.height)
        else:
            badGuyEP = pygame.Rect(badGuyPos.left, bad['endpoints'][0] - badGuyPos.height // 2, badGuyPos.width, (bad['endpoints'][1] - bad['endpoints'][0]) + badGuyPos.height-1)
        direction = 'right'
        try:
            direction = bad['direction']
        except Exception as e:
            pass

        badGuys.append ([badGuy, badGuyPos, badGuyPos.center, tile.frame, badGuyEP, direction, bad['endpoints']])
        
    
    screenRect = (len(levels[0]),len(levels))
    screen = pygame.display.set_mode((screenRect[0]*16, screenRect[1]*16))
    fondo = pygame.Surface((screenRect[0]*16, screenRect[1]*16))
    for y, valY in enumerate(levels):
        for x, valX in enumerate(levels[y]):
            tile = Tiles.subsurface(bricks[valX])
            fondo.blit(tile, (int(x * 16),int(y * 16)))
            
fondo.set_colorkey(transColor)
font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('The Level Builder')

game_over = False
clktcks = 25



clock = pygame.time.Clock()
tile = brickPlayer.Spr((0, 0), Tiles, Sprites)
while tile.game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
    tile.handle_event(event)
    screen.fill((0,0,0))
    screen.blit(blagger, bPos)
    screen.blit(fondo, (0, 0))
    screen.blit(safe, safePos)
    for bad in badGuys:
        screen.blit(bad[0], bad[1])
        pygame.draw.rect(screen, (181, 239, 148), bad[4],1)
    
    if tile.cursor[:16] != 'badGuy endopoint':
        screen.blit(tile.image, tile.rect)
        pygame.draw.rect(screen, (255,255,255), tile.rect,1)
    else:
        screen.blit(badGuy, badGuyPos)

        screen.blit(badGuy, (tile.epRect.right - tile.rect.width, tile.epRect.bottom - tile.rect.height))
        screen.blit(badGuy, (tile.epRect.left, tile.epRect.top))

        pygame.draw.rect(screen, (181, 239, 148), tile.epRect, 1)
    
    pygame.display.flip()

    if tile.action == 'set':
        tile.action = ''
        if tile.cursor == 'tiles':
            fondo.blit(tile.image, tile.rect)
            levels[tile.posY//16][tile.posX//16] = tile.frame

        elif tile.cursor == 'sprites':
            blagger = tile.image
            bPos = tile.rect[:]
            levelSprites[0]['position'] = tile.rect.center
            if tile.frame != 0:
                levelSprites[0]['direction'] = 'stand_left'
                
        elif tile.cursor == 'safe':
            safe = tile.image
            safePos = tile.rect[:]
            levelSprites[1]['position'] = tile.rect.center

        elif tile.cursor == 'badGuy':
            #para que no se superponga con el registro anterior
            if (len(badGuys) > 0 and badGuys[-1][1] != tile.rect[:] and badGuys[-1][0] != tile.image) or len(badGuys) == 0:
                badGuy = tile.image
                badGuyPos = tile.rect[:]
                #badGuys.append([badGuy, badGuyPos, tile.rect.center, tile.frame, tile.rect])
                tile.cursor = 'badGuy endopoint 1'
                tile.epRect = deepcopy(tile.rect)

        elif tile.cursor == 'badGuy endopoint 1':
            if tile.epX != 0 or tile.epY != 0:
                if tile.epX != 0:
                    tile.epRect_minWidth = tile.epRect.width

                elif tile.epY != 0:
                    tile.epRect_minHeight = tile.epRect.height

                tile.cursor = 'badGuy endopoint 2'

        elif tile.cursor == 'badGuy endopoint 2':
            if tile.epY > 0:
                direction = 'down'
                ep = tile.epRect.top + tile.rect.height // 2, tile.epRect.bottom - tile.rect.height // 2
            elif tile.epY < 0:
                direction = 'up'
                ep = tile.epRect.top + tile.rect.height // 2, tile.epRect.bottom - tile.rect.height // 2
            elif tile.epX > 0:
                direction = 'right'
                ep = tile.epRect.left + tile.rect.width // 2, tile.epRect.right - tile.rect.width // 2
            elif tile.epX < 0:
                direction = 'left'
                ep = tile.epRect.left + tile.rect.width // 2, tile.epRect.right - tile.rect.width // 2

            badGuys.append([badGuy, badGuyPos, tile.rect.center, tile.frame, tile.epRect, direction, ep])
            tile.cursor = 'badGuy'
            tile.epRect_minWidth = 0
            tile.epRect_minHeight = 0
            tile.epX = 0
            tile.epY = 0

    elif tile.action == 'unset' and tile.cursor == 'tiles':
        tile.action = ''
        fondo.fill((0,0,0), tile.rect)
        levels[tile.posY//16][tile.posX//16] = 32

    elif tile.action == 'unset' and tile.cursor == 'badGuy':
        tile.action = ''
        if len(badGuys) > 0:
            badGuys = badGuys[:-1]

    elif tile.action == 'get':
        tile.action = ''
        tile.frame = levels[tile.posY//16][tile.posX//16]
    clock.tick(clktcks)
    
print ('levels.append([ \\')
for lev in levels[:-1]:
    print ('    ' + repr(lev)+', \\')
print ('    ' + repr(levels[-1]) +'])')
print
print ('levelSprites.append([ \\')
print ('    ' + repr(levelSprites[0]) + ', \\')
print ('    ' + repr(levelSprites[1]) + ', \\')
if len(badGuys) > 1:
    for bad in badGuys[:-1]:
        print ('    {\'position\': ' + repr(tuple(bad[2])) + ', \'nro\': ' + repr(bad[3] + 1) + ', \'endpoints\': ' + repr(bad[6]) + ', \'direction\': ' + repr(bad[5]) + '}, \\')
if len(badGuys) > 0:
    print ('    {\'position\': ' + repr((badGuys[-1][2])) + ', \'nro\': ' + repr(badGuys[-1][3] + 1) + ', \'endpoints\': ' + repr(badGuys[-1][6]) + ', \'direction\': ' + repr(badGuys[-1][5]) + '}])')
else:
    print ('    {}])')

pygame.quit()
sys.exit()
