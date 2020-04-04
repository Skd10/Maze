from pygame.locals import *
import pygame
block_size = 45
def show_text(_image_surf):
    global block_size
    X = 600
    Y = 100
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128)
    display_surface = _image_surf
   
    font = pygame.font.Font('freesansbold.ttf', 32) 
 
    text = font.render(str(block_size), True, green, blue) 
    
    textRect = text.get_rect()  
    
    textRect.center = (X // 2, Y // 2) 

    display_surface.blit(text, textRect)  
    for event in pygame.event.get() :   
        pygame.display.update()

class Player:
    x = 10
    y = 10
    speed = 1
 
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def moveUp(self):
        self.y = self.y - self.speed
 
    def moveDown(self):
        self.y = self.y + self.speed
 
class Maze:
    def __init__(self):
       self.M = 10
       self.N = 8
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,1,1,1,1,1,1,0,1,
                     1,0,1,0,0,0,0,0,0,1,
                     1,0,1,0,1,1,1,1,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,1,1,1,]

    def draw(self,display_surf,image_surf):
       global block_size
       block_size -= 0.01
    #    self._block_surf = pygame.transform.scale(self._block_surf, (int(block_size), int(block_size)))
    #    image_surf = pygame.transform.scale(image_surf, (int(45), int(45)))

       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 44 , by * 44))

           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1


class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player()
        self.maze = Maze()

 
    def on_init(self):
        global block_size
        w = self.windowWidth
        h = self.windowHeight
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("Green_Block.png").convert()
        self._block_surf = pygame.image.load("wooden_Block.jpg").convert()
        self._block_surf = pygame.transform.scale(self._block_surf, (int(45), int(45)))
        self._image_surf = pygame.transform.scale(self._image_surf, (int(block_size), int(block_size)))

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._image_surf = pygame.transform.scale(self._image_surf, (int(33), int(33)))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        # self._display_surf = pygame.transform.scale(self._display_surf, (40, 40))
        # self._image_surf = pygame.transform.scale(self._display_surf, (int(45), int(45)))
        self.maze.draw(self._display_surf, self._block_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()

theApp = App()
theApp.on_execute()