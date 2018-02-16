import pygame
class Spr(pygame.sprite.Sprite):
    game_over = False
    def __init__(self, position, general_sprites):
        self.sheet = general_sprites
        self.sheet.set_clip(pygame.Rect(0, 0, 16, 16))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = (position[0], position[1])
        self.brick_states = {}
        for y in range(4):
            for x in range(32):
                self.brick_states[ int(x + y * 32)]  = (x * 16, y * 16, 16, 16)
        self.right_states  = { 0: (0, 0, 47, 41), 1: (50, 0, 47, 41), 2: (100, 0, 47, 41), 3: (150,  0, 47, 41), 4: (200,  0, 47, 41), 5: (250,  0, 47, 41), 6: (300,  0, 47, 41), 7: (350,  0, 47, 41) }
        self.left_states = { 0: (400, 0, 47, 41), 1: (450, 0, 47, 41), 2: (500, 0, 47, 41), 3: (550, 0, 47, 41), 4: (0, 44, 47, 41), 5: (50, 44, 47, 41), 6: (100, 44, 47, 41), 7: (150, 44, 47, 41) }
        self.frame = 30
        self.direction = 'stand'
        self.posX = position[0]
        self.posY = position[1]
        self.vel  = 16
        self.nextDirection = ''
        self.game_over = False
        self.action = ''
        
    def get_frame(self, frame_set):
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
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
        
        if self.nextDirection!='':
            if self.direction == 'stand'\
                    or (self.direction=='right' and self.nextDirection=='left')\
                    or (self.direction=='left' and self.nextDirection=='right'):
                self.direction=self.nextDirection
                self.nextDirection=''
     
        if self.direction == 'stand':
            #self.frame = 0
            self.clip(self.brick_states)

        elif self.direction == 'left':
            self.clip(self.brick_states)
            self.posX -= self.vel
            
        elif self.direction == 'right':
            self.clip(self.brick_states)
            self.posX += self.vel

        elif self.direction == 'up':
            self.clip(self.brick_states)
            self.posY -= self.vel

        elif self.direction == 'down':
            self.clip(self.brick_states)
            self.posY += self.vel

        # screen size 640x480 sprite size 16x16
        w = pygame.display.Info().current_w
        h = pygame.display.Info().current_h
        if self.posX > w : self.posX -= (w)
        if self.posX < 0 : self.posX += (w)
        if self.posY > h : self.posY -= (h)
        if self.posY < 0 : self.posY += (h)

        self.direction = 'stand'

        self.rect.center = (self.posX, self.posY)
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
                if key_name == 'left'  or key_name == '[4]':
                    self.nextDirection='left'
                if key_name == 'right' or key_name == '[6]':
                    self.nextDirection='right'
                if key_name == 'up'  or key_name == '[8]':
                    self.nextDirection='up'
                if key_name == 'down' or key_name == '[2]':
                    self.nextDirection='down'

                if key_name == 'space':
                    self.action = 'set'
                if key_name == 'backspace':
                    self.action = 'unset'

                if key_name == 'a':
                    self.frame += 1
                if key_name == 'z':
                    self.frame -= 1

                
                if key_name == 'escape':
                    self.game_over = True
                    
                if self.nextDirection == self.direction:
                    self.nextDirection = ''
                #print key_name
