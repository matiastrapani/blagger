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
        self.vel  = 2.75
        self.nextDirection = ''
        self.jumpDir = ''
        self.lives = 0
        self.jumpseq = [-1,-1,-2,-1,-2,-1,-2,-1,-2,-1,-1,-1,-1,-1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]
        self.jumpcount = -1
        self.clk = 0
        
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
    
    def update(self, level):
        x0 = self.posX
        y0 = self.posY


        
        self.clk += 1
        if self.clk == 1:
            self.clk =0
            if self.nextDirection != '':
                if self.direction != self.nextDirection\
                    and self.nextDirection != 'jump':
                    self.direction = self.nextDirection
                    self.nextDirection=''
 
               
                elif (self.direction == 'stand_right'\
                        or self.direction == 'stand_left')\
                        and self.nextDirection == 'jump':
                        self.jumpDir = self.direction
                        self.nextDirection = ''
                        self.direction = 'jump'
                        self.jumpcount = 0
                        
                elif self.direction == 'right'\
                        and self.nextDirection == 'jump':
                        self.jumpDir = 'stand_right'
                        self.nextDirection = ''
                        self.direction = 'jump_right'
                        self.jumpcount = 0

                elif self.direction == 'left'\
                        and self.nextDirection == 'jump':
                        self.jumpDir = 'stand_left'
                        self.nextDirection = ''
                        self.direction = 'jump_left'
                        self.jumpcount = 0
                        
       
                        
         
            if self.direction == 'stand_left':
                pass
                #self.frame = 0
                self.clip(self.left_states)

            if self.direction == 'stand_right':
                pass
                #self.frame = 0
                self.clip(self.right_states)

            elif self.direction == 'left':
                self.frame+=1
                self.clip(self.left_states)
                self.posX -= self.vel
                self.nextDirection = 'stand_left'

                
            elif self.direction == 'right':
                self.frame+=1
                self.clip(self.right_states)
                self.posX += self.vel
                self.nextDirection = 'stand_right'

            elif self.direction == 'jump':
                self.posY += (self.jumpseq[self.jumpcount]*2)
                self.nextDirection = ''
                self.jumpcount += 1

                if self.jumpDir == 'stand_right':
                    self.clip(self.right_states)
                else:
                    self.clip(self.left_states)
                    
                if self.jumpcount >= len(self.jumpseq):
                      self.direction = self.jumpDir
                      self.jumpcount = -1

            elif self.direction == 'jump_right':
                self.posY += (self.jumpseq[self.jumpcount]*2)
                self.jumpcount += 1
                self.frame += 1
                self.clip(self.right_states)
                self.posX += self.vel
                self.nextDirection = ''
                if self.jumpcount >= len(self.jumpseq):
                      self.direction = 'stand_right'
                      self.jumpcount = -1
                      
            elif self.direction == 'jump_left':
                self.posY += (self.jumpseq[self.jumpcount]*2)
                self.jumpcount += 1
                self.frame += 1
                self.clip(self.left_states)
                self.posX -= self.vel
                self.nextDirection = ''
                if self.jumpcount >= len(self.jumpseq):
                      self.direction = 'stand_left'
                      self.jumpcount = -1


            if self.jumpcount >= 0 and self.jumpcount <= 13 and \
               level[int(self.posY//16 - 2)][(int(self.posX-7)//16)] != 32:
                print y0
                self.posY = y0
                
            if level[int(self.posY//16 - 1)][(int(self.posX-7)//16)] != 32 or \
               level[int(self.posY//16)][(int(self.posX-7)//16)] != 32 or \
               level[int(self.posY//16 - 1)][(int(self.posX-7)//16 + 1)] != 32 or \
               level[int(self.posY//16)][(int(self.posX-7)//16 + 1)] != 32:
               
                self.posX = x0
        

            self.rect.center = (self.posX, self.posY)
            self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        
    def handle_event(self, event, level):
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            sys.exit()

        #print self.posX
        #scr 640x480 spr 47x41
        if self.posX > (640+47/2) : self.posX -= (640+47)
        if self.posX < (0-47/2) : self.posX += (640+47)
        if self.posY > 480 : self.posY -= 480
        if self.posY < 0 : self.posY += 480
        self.update(level)
        
        if self.jumpcount == -1:
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
                            self.jumpcount = 0
                            
                        if key_name == 'left'  or key_name == '[4]':
                            if self.nextDirection == 'jump':
                                self.nextDirection = 'jump_left'
                                self.jumpcount = 0
                            else:
                                self.nextDirection = 'left'

                        if key_name == 'right' or key_name == '[6]':
                            if self.nextDirection == 'jump':
                                self.nextDirection = 'jump_right'
                                self.jumpcount = 0
                            else:
                                self.nextDirection = 'right'


                        elif key_name == 'escape':
                            self.game_over = True
                            
