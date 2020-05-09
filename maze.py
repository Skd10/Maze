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
    global theApp
    x = 60
    y = 60
    speed = 1
    arrows = {"left": False, "right": False, "up": False, "down": False}
 
    def moveRight(self):
        if not any([self.arrows["right"], self.arrows["down"], self.arrows["left"], self.arrows["up"]]):
            self.arrows["right"] = True
            # if theApp.check_impact():
            #     self.x = self.x - self.speed - 10
            # else:
            #     self.x = self.x + self.speed
            # self.arrows["right"] = False

    def moveLeft(self):
        if not any([self.arrows["left"], self.arrows["down"], self.arrows["right"], self.arrows["up"]]):
            self.arrows["left"] = True
            # if theApp.check_impact():
            #     self.x = self.x + self.speed + 10
            # else:
            #     self.x = self.x - self.speed
            # self.arrows["left"] = False
 
    def moveUp(self):
        if not any([self.arrows["up"], self.arrows["down"], self.arrows["right"], self.arrows["left"]]):
            self.arrows["up"] = True
            # if theApp.check_impact():
            #     self.y = self.y + self.speed + 10
            # else:
            #     self.y = self.y - self.speed
            # self.arrows["up"] = False
 
    def moveDown(self):
        if not any([self.arrows["down"], self.arrows["left"], self.arrows["right"], self.arrows["up"]]):
            self.arrows["down"] = True
            # if theApp.check_impact():
            #     self.y = self.y - self.speed - 10
            # else:
            #     self.y = self.y + self.speed
            # self.arrows["down"] = False
 
class Maze:
    def __init__(self):
       self.M = 10
       self.N = 8
       self.maze_blocks = []
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,1,1,1,1,1,1,0,1,
                     1,0,1,0,0,0,0,0,0,1,
                     1,0,1,0,1,1,1,1,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,1,1,1,]
       self.create_blocks()

    def create_blocks(self):
        bx = 0
        by = 0
        for i in range(0,self.M*self.N):
            if self.maze[ bx + (by*self.M) ] == 1:
                self.maze_blocks.append([bx * 44 , by * 44])
            bx = bx + 1
            if bx > self.M-1:
                bx = 0 
                by = by + 1


    def draw(self,display_surf,image_surf):
       for block in self.maze_blocks:
           display_surf.blit(image_surf,( block[0] , block[1]))


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

    def check_impact(self, top, right, bottom, left):
        for block in self.maze.maze_blocks:
            block_left = block[0]
            block_right = block[0] + 45
            block_top = block[1]
            block_bottom = block[1] + 45
            left = self.player.x
            right = self.player.x + 33
            top = self.player.y
            bottom = self.player.y + 33
            if (block_right > right > block_left) or (block_right > left > block_left):
                if (block_top < top < block_bottom) or (block_top < bottom < block_bottom):
                    return True

    def on_init(self):
        speed = self.player.speed
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
        speed = self.player.speed
        if self.player.arrows ["up"] and not any([self.player.arrows["down"],self.player.arrows["right"],self.player.arrows["left"]]):
            potential_top = self.player.y - speed
            potential_bottom = self.player.y + 33 - speed
            potential_left = self.player.x
            potential_right = self.player.x + 33
            # check for impact
            if not self.check_impact(potential_top, potential_right, potential_bottom, potential_left):
                self.player.y -= speed
        if self.player.arrows ["down"] and not any([self.player.arrows["up"],self.player.arrows["right"],self.player.arrows["left"]]):
            potential_top = self.player.y + speed
            potential_bottom = self.player.y + 33 + speed
            potential_left = self.player.x
            potential_right = self.player.x + 33
            # check for impact
            if not self.check_impact(potential_top, potential_right, potential_bottom, potential_left):
                self.player.y += speed
        if self.player.arrows ["right"] and not any([self.player.arrows["down"],self.player.arrows["up"],self.player.arrows["left"]]):
            potential_top = self.player.y
            potential_bottom = self.player.y + 33
            potential_left = self.player.x + speed
            potential_right = self.player.x + 33 + speed
            # check for impact
            if not self.check_impact(potential_top, potential_right, potential_bottom, potential_left):
                self.player.x += speed
        if self.player.arrows ["left"] and not any([self.player.arrows["down"],self.player.arrows["right"],self.player.arrows["up"]]):
            potential_top = self.player.y
            potential_bottom = self.player.y + 33
            potential_left = self.player.x - speed
            potential_right = self.player.x + 33 - speed
            # check for impact
            if not self.check_impact(potential_top, potential_right, potential_bottom, potential_left):
                self.player.x -= speed

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
            else:
                self.player.arrows["right"] = False
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
            else:
                self.player.arrows["left"] = False
 
            if (keys[K_UP]):
                self.player.moveUp()
            else:
                self.player.arrows["up"] = False
 
            if (keys[K_DOWN]):
                self.player.moveDown()
            else:
                self.player.arrows["down"] = False
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()

theApp = App()
theApp.on_execute()