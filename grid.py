import pygame

class Grid:
    def __init__(self, x,y, tilesize):
        self.x = x
        self.y = y
        self.offsetX = 0
        self.offsetY = 0
        self.tilesize = tilesize

    def set_color(self, v):
        self.color = v

    def draw(self, screen):
        for i in range(1,self.x):
            pygame.draw.line(screen,self.color, (self.tilesize*i + self.offsetX, self.offsetY), (self.tilesize*i + self.offsetX, self.tilesize*self.y + self.offsetY) )
        for i in range(0,self.y):
            pygame.draw.line(screen, self.color, (self.offsetX, self.tilesize*i + self.offsetY), (self.tilesize*self.x + self.offsetX, self.tilesize*i + self.offsetY) )

    def displayExit(self, screen, color, x, y):
        pygame.draw.line(screen, color, (self.tilesize*x + self.offsetX, self.tilesize*y + self.offsetY), (self.tilesize*x + self.tilesize + self.offsetX, self.tilesize*y+self.tilesize + self.offsetY), 3)
        pygame.draw.line(screen, color, (self.tilesize*x + self.offsetX, self.tilesize*y+self.tilesize + self.offsetY), (self.tilesize*x + self.tilesize + self.offsetX, self.tilesize*y + self.offsetY), 3)
        
    def change_origin(self, X, Y):
        self.offsetX = X
        self.offsetY = Y