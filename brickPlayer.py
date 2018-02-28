import pygame

class Spr(pygame.sprite.Sprite):
    game_over = False
    def __init__(self, position, general_tiles, general_sprites):
        self.sheet = general_tiles
        self.sheet.set_clip(pygame.Rect(0, 0, 16, 16))
        self.sprites = general_sprites
        self.tiles = general_tiles
        transColor = pygame.Color(0, 0, 0)
        self.sprites.set_colorkey(transColor)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = (position[0], position[1])
        self.brick_states = {}
        for y in range(4):
            for x in range(32):
                self.brick_states[ int(x + y * 32)]  = (x * 16, y * 16, 16, 16)
        self.sprite_states = {0:(0, 0, 48, 41), 1:(400, 0, 48, 41)}
        self.badGuy_states = {0:(200, 44, 48, 41), 1:(300, 44, 48, 41), 2:(400, 44, 48, 41), 3:(500, 44, 48, 41), 4:(  0, 88, 48, 41), 5:(100, 88, 48, 41), 6:(200, 88, 48, 41), 7:(300, 88, 48, 41), 8:(400, 88, 48, 41), 9:(500, 88, 48, 41), 10:(  0, 132, 48, 41), 11:(100, 132, 48, 41), 12:(200, 132, 48, 41)}
        self.safe = {0:(556, 148, 41, 26)}
        self.states = self.brick_states
        self.frame = 30
        self.direction = 'stand'
        self.posX = position[0]
        self.posY = position[1]
        self.vel  = 16
        self.nextDirection = ''
        self.game_over = False
        self.action = ''
        self.cursor = 'tiles'
        self.epX = 0
        self.epY = 0
        self.epRect = pygame.Rect(0, 0, 48, 41)
        self.epRect_minWidth = 0
        self.epRect_minHeight = 0
        
    def tab_sprite(self):
        if self.cursor == 'tiles':
            self.states = self.sprite_states
            self.sheet = self.sprites
            self.sheet.set_clip(pygame.Rect(0, 0, 48, 41))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect = self.image.get_rect()
            self.cursor = 'sprites'

        elif self.cursor == 'sprites':
            self.posX = int(self.posX//16)*16
            self.posY = int(self.posY//16)*16
            self.states = self.safe
            self.sheet.set_clip(pygame.Rect(0, 0, 41, 26))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect = self.image.get_rect()
            self.cursor = 'safe'

        elif self.cursor == 'safe':
            self.posX = int(self.posX//16)*16
            self.posY = int(self.posY//16)*16
            self.states = self.badGuy_states
            self.sheet.set_clip(pygame.Rect(0, 0, 48, 41))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect = self.image.get_rect()
            self.cursor = 'badGuy'

        elif self.cursor == 'badGuy':
            self.posX = int(self.posX//16)*16
            self.posY = int(self.posY//16)*16
            self.states = self.brick_states
            self.sheet = self.tiles
            self.frame = 30
            self.sheet.set_clip(pygame.Rect(0, 0, 16, 16))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect = self.image.get_rect()
            self.cursor = 'tiles'
        
        pygame.time.wait(100)
        return


    def get_frame(self, frame_set):
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        elif self.frame < 0:
            self.frame = (len(frame_set) - 1)
        return frame_set[self.frame]


 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    
    def update(self):
        

        x0 = self.posX
        y0 = self.posY

        if self.direction == 'shift' and self.nextDirection == '':
            self.direction = 'stand'
        
        if self.nextDirection != '':
            
            self.direction = self.nextDirection
            self.nextDirection = ''
        
        
        if self.direction == 'stand':
            self.clip(self.states)

        elif self.direction == 'left':
            if self.cursor[:16] != 'badGuy endopoint':
                self.clip(self.states)
                self.posX -= self.vel
            elif self.cursor == 'badGuy endopoint 1':
                self.epX -= self.vel
                self.epY = 0
                self.epRect.width = self.rect.width + abs(self.epX)
                self.epRect.height = self.rect.height 
                if self.epX >= 0:
                    self.epRect.topleft = self.rect.topleft
                else:
                    self.epRect.topright = self.rect.topright

            elif self.cursor == 'badGuy endopoint 2':
                if self.epRect_minWidth:
                    if self.epX < 0:
                        a = self.epRect.topleft
                    else:
                        a = self.epRect.topright
                    self.epX += self.vel
                    self.epRect.width = self.rect.width + abs(self.epX)
                    if self.epRect.width < self.epRect_minWidth:
                        self.epRect.width = self.epRect_minWidth
                        self.epX -= self.vel
                    if self.epX < 0:
                        self.epRect.topleft = a
                    else:
                        self.epRect.topright = a
                        
                
        elif self.direction == 'right':
            if self.cursor[:16] != 'badGuy endopoint':
                self.clip(self.states)
                self.posX += self.vel
            elif self.cursor == 'badGuy endopoint 1':
                self.epX += self.vel
                self.epY = 0
                self.epRect.width = self.rect.width + abs(self.epX)
                self.epRect.height = self.rect.height 
                if self.epX >= 0:
                    self.epRect.topleft = self.rect.topleft
                else:
                    self.epRect.topright = self.rect.topright

            elif self.cursor == 'badGuy endopoint 2':
                if self.epRect_minWidth:

                    if self.epX < 0:
                        a = self.epRect.topleft
                    else:
                        a = self.epRect.topright
                        
                    self.epX -= self.vel
                    self.epRect.width = self.rect.width + abs(self.epX)
                    if self.epRect.width < self.epRect_minWidth:
                        self.epRect.width = self.epRect_minWidth
                        self.epX += self.vel
                    if self.epX < 0:
                        self.epRect.topleft = a
                    else:
                        self.epRect.topright = a
                        
                    
        elif self.direction == 'up':
            if self.cursor[:16] != 'badGuy endopoint':
                self.clip(self.states)
                self.posY -= self.vel
            elif self.cursor == 'badGuy endopoint 1':
                self.epY -= self.vel
                self.epX = 0
                self.epRect.width = self.rect.width 
                self.epRect.height = self.rect.height + abs(self.epY)
                if self.epY >= 0:
                    self.epRect.topleft = self.rect.topleft
                else:
                    self.epRect.bottomleft = self.rect.bottomleft

            elif self.cursor == 'badGuy endopoint 2':
                if self.epRect_minHeight:

                    if self.epY < 0:
                        a = self.epRect.topright
                    else:
                        a = self.epRect.bottomright
                        
                    self.epY += self.vel
                    self.epRect.height = self.rect.height + abs(self.epY)
                    if self.epRect.height < self.epRect_minHeight:
                        self.epRect.height = self.epRect_minHeight
                        self.epY -= self.vel
                    if self.epY < 0:
                        self.epRect.topright = a
                    else:
                        self.epRect.bottomright = a

        elif self.direction == 'down':
            if self.cursor[:16] != 'badGuy endopoint':
                self.clip(self.states)
                self.posY += self.vel
            elif self.cursor == 'badGuy endopoint 1':
                self.epY += self.vel
                self.epX = 0
                self.epRect.width = self.rect.width 
                self.epRect.height = self.rect.height + abs(self.epY)
                if self.epY >= 0:
                    self.epRect.topleft = self.rect.topleft
                else:
                    self.epRect.bottomleft = self.rect.bottomleft

            elif self.cursor == 'badGuy endopoint 2':
                if self.epRect_minHeight:

                    if self.epY < 0:
                        a = self.epRect.topright
                    else:
                        a = self.epRect.bottomright
                        
                    self.epY -= self.vel
                    self.epRect.height = self.rect.height + abs(self.epY)
                    if self.epRect.height < self.epRect_minHeight:
                        self.epRect.height = self.epRect_minHeight
                        self.epY += self.vel
                    if self.epY < 0:
                        self.epRect.topright = a
                    else:
                        self.epRect.bottomright = a

        elif self.direction == 'shift_left':
            if self.cursor[:16] != 'badGuy endopoint':
                self.clip(self.states)
                self.posX -= 1
            elif self.cursor == 'badGuy endopoint 1':
                self.epX -= 1
                self.epY = 0
                self.epRect.width = self.rect.width + abs(self.epX)
                self.epRect.height = self.rect.height 
                if self.epX >= 0:
                    self.epRect.topleft = self.rect.topleft
                else:
                    self.epRect.topright = self.rect.topright

            elif self.cursor == 'badGuy endopoint 2':
                if self.epRect_minWidth:
                    if self.epX < 0:
                        a = self.epRect.topleft
                    else:
                        a = self.epRect.topright
                    self.epX += 1
                    self.epRect.width = self.rect.width + abs(self.epX)
                    if self.epRect.width < self.epRect_minWidth:
                        self.epRect.width = self.epRect_minWidth
                        self.epX -= 1
                    if self.epX < 0:
                        self.epRect.topleft = a
                    else:
                        self.epRect.topright = a

        elif self.direction == 'shift_right':
            if self.cursor[:16] != 'badGuy endopoint':
                self.clip(self.states)
                self.posX += 1
            elif self.cursor == 'badGuy endopoint 1':
                self.epX += 1
                self.epY = 0
                self.epRect.width = self.rect.width + abs(self.epX)
                self.epRect.height = self.rect.height 
                if self.epX >= 0:
                    self.epRect.topleft = self.rect.topleft
                else:
                    self.epRect.topright = self.rect.topright

            elif self.cursor == 'badGuy endopoint 2':
                if self.epRect_minWidth:

                    if self.epX < 0:
                        a = self.epRect.topleft
                    else:
                        a = self.epRect.topright
                        
                    self.epX -= 1
                    self.epRect.width = self.rect.width + abs(self.epX)
                    if self.epRect.width < self.epRect_minWidth:
                        self.epRect.width = self.epRect_minWidth
                        self.epX += 1
                    if self.epX < 0:
                        self.epRect.topleft = a
                    else:
                        self.epRect.topright = a



        elif self.direction == 'shift_up':
            if self.cursor[:16] != 'badGuy endopoint':
                self.clip(self.states)
                self.posY -= 1
            elif self.cursor == 'badGuy endopoint 1':
                self.epY -= 1
                self.epX = 0
                self.epRect.width = self.rect.width 
                self.epRect.height = self.rect.height + abs(self.epY)
                if self.epY >= 0:
                    self.epRect.topleft = self.rect.topleft
                else:
                    self.epRect.bottomleft = self.rect.bottomleft

            elif self.cursor == 'badGuy endopoint 2':
                if self.epRect_minHeight:

                    if self.epY < 0:
                        a = self.epRect.topright
                    else:
                        a = self.epRect.bottomright
                        
                    self.epY += 1
                    self.epRect.height = self.rect.height + abs(self.epY)
                    if self.epRect.height < self.epRect_minHeight:
                        self.epRect.height = self.epRect_minHeight
                        self.epY -= 1
                    if self.epY < 0:
                        self.epRect.topright = a
                    else:
                        self.epRect.bottomright = a

        elif self.direction == 'shift_down':
            if self.cursor[:16] != 'badGuy endopoint':
                self.clip(self.states)
                self.posY += 1
            elif self.cursor == 'badGuy endopoint 1':
                self.epY += 1
                self.epX = 0
                self.epRect.width = self.rect.width 
                self.epRect.height = self.rect.height + abs(self.epY)
                if self.epY >= 0:
                    self.epRect.topleft = self.rect.topleft
                else:
                    self.epRect.bottomleft = self.rect.bottomleft

            elif self.cursor == 'badGuy endopoint 2':
                if self.epRect_minHeight:

                    if self.epY < 0:
                        a = self.epRect.topright
                    else:
                        a = self.epRect.bottomright
                        
                    self.epY -= 1
                    self.epRect.height = self.rect.height + abs(self.epY)
                    if self.epRect.height < self.epRect_minHeight:
                        self.epRect.height = self.epRect_minHeight
                        self.epY += 1
                    if self.epY < 0:
                        self.epRect.topright = a
                    else:
                        self.epRect.bottomright = a

        # screen size 640x480 sprite size 16x16
        w = pygame.display.Info().current_w
        h = pygame.display.Info().current_h
        if self.posX > w : self.posX -= (w)
        if self.posX < 0 : self.posX += (w)
        if self.posY > h : self.posY -= (h)
        if self.posY < 0 : self.posY += (h)

        if self.direction != 'shift':
            self.direction = 'stand'

        self.rect.topleft = (self.posX, self.posY)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            sys.exit()

        self.update()
        
        # Creo una lista vacia 
        pressed_key_text = []
        
        # Obtengo las teclas que el usuario presiona
        pressed_keys = pygame.key.get_pressed()
        # recorro la lista con un loop for 
        for key_constant, pressed in enumerate(pressed_keys):
    
            # Si la tecla esta presionada 
            if pressed:
                # Obtengo el nombre de la tecla presionada
                key_name = pygame.key.name(key_constant)
                #pygame.time.wait(1000)

                if key_name == 'left' or key_name == '[4]':
                        self.nextDirection = 'left'

                elif key_name == 'right' or key_name == '[6]':
                        self.nextDirection = 'right'

                elif key_name == 'up'  or key_name == '[8]':
                        self.nextDirection = 'up'

                elif key_name == 'down' or key_name == '[2]':
                        self.nextDirection = 'down'
                        
                elif self.cursor != 'tile' and (key_name == 'left shift' or key_name == 'right shift'):                    
                    self.nextDirection = 'shift_' + self.nextDirection
                    
                elif key_name == 'space':
                    self.action = 'set'
                    pygame.time.wait(100)

                elif key_name == 'backspace' and (self.cursor == 'tiles' or self.cursor == 'badGuy'):
                    self.action = 'unset'
                    pygame.time.wait(100)

                elif key_name == 'return' and self.cursor == 'tiles':
                    self.action = 'get'

                elif key_name == 'tab':
                    self.tab_sprite()
                    pygame.time.wait(100)

                elif key_name == 'a':
                    self.frame += 1
                    pygame.time.wait(100)

                elif key_name == 'z':
                    self.frame -= 1
                    pygame.time.wait(100)

                elif key_name == 'escape':
                    if self.cursor[:16] != 'badGuy endopoint':
                        self.game_over = True
                    else:
                        self.cursor = 'badGuy'
                        pygame.time.wait(100)
