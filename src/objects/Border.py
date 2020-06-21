import pygame

class Border(object):
    def __init__(self, x0 = 0, y0=0, x1=1,y1=1, value = 'top', color = pygame.Color("green")):
        self.x0 = x0
        self.x1 = x1
        
        self.y0 = y0
        self.y1 = y1
        
        self.value = value
        
        self.color = color
        
        self.rect = pygame.Rect((self.x0, self.y0), (self.x1, self.y1))
        
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        
        
    def collision(self, ball):
        if self.rect.colliderect(ball.box):
            return self.value
        else:
            return None       
        