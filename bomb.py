import pygame

class bomb:
    def __init__(self, tilesize, color):
        self.bomb = [[12,5]]
        self.tilesize = tilesize
        self.color = color
        self.offsetX = 0
        self.offsetY = 0
        
        
    def draw(self, screen):
        for elt in self.bomb:
            pygame.draw.circle(screen, self.color, [elt[0] * self.tilesize + self.tilesize // 2 + self.offsetX, elt[1] * self.tilesize + self.tilesize // 2 + self.offsetY], 15)


    def get_bomb(self, player_x, player_y):
        for elt in self.bomb:
            if (player_x, player_y) == (elt[0], elt[1]):
                self.bomb.remove(elt)
                return True
        return False
    
    def change_origin(self, X, Y):
        self.offsetX = X
        self.offsetY = Y
