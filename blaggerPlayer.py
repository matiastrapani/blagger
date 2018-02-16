import pygame
class Spr(pygame.sprite.Sprite):
    game_over = False
    def __init__(self, position, general_sprites):
        self.sheet = general_sprites
        self.sheet.set_clip(pygame.Rect(0, 0, 47, 41))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = (position[0], position[1])
        self.frame = 0
        self.right_states  = { 0: (0, 0, 47, 41), 1: (50, 0, 47, 41), 2: (100, 0, 47, 41), 3: (150,  0, 47, 41), 4: (200,  0, 47, 41), 5: (250,  0, 47, 41), 6: (300,  0, 47, 41), 7: (350,  0, 47, 41) }
        self.left_states = { 0: (400, 0, 47, 41), 1: (450, 0, 47, 41), 2: (500, 0, 47, 41), 3: (550, 0, 47, 41), 4: (0, 44, 47, 41), 5: (50, 44, 47, 41), 6: (100, 44, 47, 41), 7: (150, 44, 47, 41) }
        self.direction = 'stand_right'
        self.posX = position[0]
        self.posY = position[1]
        self.vel  = 2
        self.nextDirection = ''
        self.jumpDir = ''
        self.lives = 5
        self.jumpseq = [-1,-1,0, -1,-1,-1, -1,-1,-1, -1,-1,-1, -1,-1,-1, -1,-1,0, -1,-1,0,    0,0,  1,1,1,  1,1,1,  1,1,1,  1,1,1,  1,1,1,  1,1,1]
        self.jumpcount = 0
        self.fallcount = 0
        self.fall = False
        self.sound = ''
        
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

    def get_levelPos(self):
        i = int((self.posX-7)//16)
        j = int((self.posY)//16)
        return i, j
    
    def update(self, level):
        x0 = self.posX
        y0 = self.posY
        
        if self.nextDirection != '':
            if self.nextDirection[:4] != 'jump' and not self.fall:
                self.jumpDir = ''
                self.direction = self.nextDirection
                self.nextDirection = ''

            elif ((self.direction == 'stand_right' or \
            self.direction == 'stand_left') and \
            self.nextDirection == 'jump') and not self.fall:
                    self.jumpDir = self.direction
                    self.direction = 'jump'
                    self.nextDirection = ''
            
            elif ((self.direction == 'right' and \
            self.nextDirection == 'jump') or \
            self.nextDirection == 'jump_right') and not self.fall:
                    self.jumpDir = 'stand_right'
                    self.direction = 'jump_right'
                    self.nextDirection = ''

            elif ((self.direction == 'left' and \
            self.nextDirection == 'jump') or \
            self.nextDirection == 'jump_left') and not self.fall:
                    self.jumpDir = 'stand_left'
                    self.direction = 'jump_left'
                    self.nextDirection = ''
                    
        if self.direction == 'stand_left':
            self.clip(self.left_states)

        if self.direction == 'stand_right':
            self.clip(self.right_states)

        elif self.direction == 'left':
            self.nextDirection = 'stand_left'
            if not(self.fall):
                self.sound = 'step'
                self.frame+=1
                self.clip(self.left_states)
                self.posX -= self.vel
            else:
                self.clip(self.left_states)

        elif self.direction == 'right':
            self.nextDirection = 'stand_right'
            if not(self.fall):
                self.sound = 'step'
                self.frame+=1
                self.clip(self.right_states)
                self.posX += self.vel
            else:
                self.clip(self.right_states)
                
        elif self.direction == 'jump':
            self.posY += (self.jumpseq[self.jumpcount]*2)
            self.jumpcount += 1
            self.nextDirection = ''

            if self.jumpDir == 'stand_right':
                self.clip(self.right_states)
            else:
                self.clip(self.left_states)
                
            if self.jumpcount >= len(self.jumpseq):
                self.direction = self.jumpDir
                self.jumpDir = ''
                self.jumpcount = 0


        elif self.direction == 'jump_right':
            self.posY += (self.jumpseq[self.jumpcount]*2)
            self.jumpcount += 1
            self.frame += 1
            self.clip(self.right_states)
            self.posX += self.vel
            self.nextDirection = ''
            if self.jumpcount >= len(self.jumpseq):
                self.direction = self.jumpDir
                self.jumpDir = ''
                self.jumpcount = 0

                  
        elif self.direction == 'jump_left':
            self.posY += (self.jumpseq[self.jumpcount]*2)
            self.jumpcount += 1
            self.frame += 1
            self.clip(self.left_states)
            self.posX -= self.vel
            self.nextDirection = ''
            if self.jumpcount >= len(self.jumpseq):
                self.direction = self.jumpDir
                self.jumpDir = ''
                self.jumpcount = 0


        i, j = self.get_levelPos()
        if level[j - 1][i]  == 30 or 100 <= level[j - 1][i]     <= 102 or \
        level[j][i]         == 30 or 100 <= level[j][i]         <= 102 or \
        level[j - 1][i + 1] == 30 or 100 <= level[j - 1][i + 1] <= 102 or \
        level[j][i + 1]     == 30 or 100 <= level[j][i + 1]     <= 102:
                self.posX = x0
                i, j = self.get_levelPos()

        if level[j+1][i] == 38 or  \
           level[j+1][i+1] == 38:
               self.posX -= self.vel
               i, j = self.get_levelPos()
        if level[j+1][i] == 78 or  \
           level[j+1][i+1] == 78:
               self.posX += self.vel
               i, j = self.get_levelPos()

        if (self.jumpcount == 0 and \
            level[j+1][i] == 32 and  \
            level[j+1][i+1] == 32) or \
            self.jumpcount >= 21:
                self.fall = True

        if self.fall:
            if (self.posY-4)%16 == 0 and \
                ((level[j+1][i] < 32 or level[j+1][i] > 33 ) or  \
                (level[j+1][i+1] < 32 or level[j+1][i+1] > 33)):
                    self.fall = False
                    self.jumpcount = 0
                    self.nextDirection = ''
                    self.sound = 'stop_fall'
                    #print self.fallcount
                    if self.fallcount <= 32:
                        self.fallcount = 0

                    if self.direction == 'jump_left' or \
                    (self.direction == 'jump' and \
                    self.jumpDir == 'stand_left'):
                        self.direction = 'stand_left'
                    elif self.direction == 'jump_right' or \
                    (self.direction == 'jump' and \
                    self.jumpDir == 'stand_right'):
                        self.direction = 'stand_right'
            else:
                    if self.jumpcount == 0 or self.jumpcount > 24:
                        self.fallcount += 1
                    if self.jumpcount == 0:
                        self.posY += self.vel                        
                        self.sound = 'fall'

        self.rect.center = (self.posX, self.posY)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        
    def handle_event(self, event, level):
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            sys.exit()

        #scr 640x480 spr 47x41
        if self.posX > (640+47/2) : self.posX -= (640+47)
        if self.posX < (0-47/2) : self.posX += (640+47)
        if self.posY > 480 : self.posY -= 480
        if self.posY < 0 : self.posY += 480
        self.update(level)
        
        if self.jumpcount == 0:
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
                        if key_name == 'up' or key_name == '[8]':
                            self.nextDirection = 'jump'
                            self.sound = 'jump'
                            
                        if key_name == 'left'  or key_name == '[4]':
                            if self.nextDirection == 'jump':
                                self.nextDirection = 'jump_left'
                                self.sound = 'jump'
                            else:
                                self.nextDirection = 'left'
                                
                        if key_name == 'right' or key_name == '[6]':
                            if self.nextDirection == 'jump':
                                self.nextDirection = 'jump_right'
                                self.sound = 'jump'
                            else:
                                self.nextDirection = 'right'


                        elif key_name == 'escape':
                            self.game_over = True
                            
