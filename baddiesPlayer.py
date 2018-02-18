import pygame
class Spr(pygame.sprite.Sprite):
    def __init__(self, general_sprites, position=(0,0), name='', nro=1, endpoints=(0,100), color=(0,0,0), direction='right'):
        self.sheet = general_sprites
        self.sheet.set_clip(pygame.Rect(200, 44, 47, 41))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = (position[0], position[1])
        self.frame = 0
        self.count = 0
        if   nro == 1 : self.states  = { 0: (200,  44, 47, 41), 1: (250,  44, 47, 41) }
        elif nro == 2 : self.states  = { 0: (300,  44, 47, 41), 1: (350,  44, 47, 41) }
        elif nro == 3 : self.states  = { 0: (400,  44, 47, 41), 1: (450,  44, 47, 41) }
        elif nro == 4 : self.states  = { 0: (500,  44, 47, 41), 1: (550,  44, 47, 41) }
        elif nro == 5 : self.states  = { 0: (  0,  88, 47, 41), 1: ( 50,  88, 47, 41) }
        elif nro == 6 : self.states  = { 0: (100,  88, 47, 41), 1: (150,  88, 47, 41) }
        elif nro == 7 : self.states  = { 0: (200,  88, 47, 41), 1: (250,  88, 47, 41) }
        elif nro == 8 : self.states  = { 0: (300,  88, 47, 41), 1: (350,  88, 47, 41) }
        elif nro == 9 : self.states  = { 0: (400,  88, 47, 41), 1: (450,  88, 47, 41) }
        elif nro == 10: self.states  = { 0: (500,  88, 47, 41), 1: (550,  88, 47, 41) }
        elif nro == 11: self.states  = { 0: (  0, 132, 47, 41), 1: ( 50, 132, 47, 41) }
        elif nro == 12: self.states  = { 0: (100, 132, 47, 41), 1: (150, 132, 47, 41) }
        elif nro == 13: self.states  = { 0: (200, 132, 47, 41), 1: (250, 132, 47, 41) }
        self.posX = position[0]
        self.posY = position[1]
        self.vel  = 2
        self.dir  = direction
        self.name = name
        iniPos = endpoints[0]
        endPos = endpoints[1]
        if iniPos > endPos:
            iniPos, endPos = endPos, iniPos
        self.iniPos = iniPos
        self.endPos = endPos
        self.color = color

    def get_frame(self, frame_set):
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        if self.color!=(0,0,0):
            self.sheet.set_palette_at(1, self.color)
        return clipped_rect
    
    def update(self):
        self.count += 1
        if self.count == 10:
            self.count = 0
            self.frame += 1
        self.clip(self.states)
        if self.dir == 'right':
            x0 = self.posX
            self.posX += self.vel
            if self.posX > self.endPos:
                self.dir = 'left'
                self.posX = self.endPos - (self.posX - self.endPos)

        elif self.dir == 'left':
            x0 = self.posX
            self.posX -= self.vel
            if self.posX < self.iniPos:
                self.dir = 'right'
                self.posX = self.iniPos - (self.iniPos - self.posX)

        elif self.dir == 'down':
            y0 = self.posY
            self.posY += self.vel
            if self.posY > self.endPos:
                self.dir = 'up'
                self.posY = self.endPos - (self.posY - self.endPos)

        elif self.dir == 'up':
            y0 = self.posY
            self.posY -= self.vel
            if self.posY < self.iniPos:
                self.dir = 'down'
                self.posY = self.iniPos - (self.iniPos - self.posY)

        self.rect.center = (self.posX, self.posY)
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if self.posX > (640+47/2) : self.posX -= (640+47)
        if self.posX < (0-47/2) : self.posX += (640+47)
        if self.posY > 480 : self.posY -= 480
        if self.posY < 0 : self.posY += 480
        self.update()
        

        
