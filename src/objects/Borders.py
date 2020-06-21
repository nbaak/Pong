from .Border import Border
import pygame



class Borders():
    
    def __init__(self):
        self.borders = []
        
    
    def add_border(self, x0, y0, x1, y1, value ,color = pygame.Color("green")):
        self.borders.append(Border(x0,y0, x1,y1, value, color))
        
        
    def draw(self, surface):
        for border in self.borders:
            border.draw(surface)
            
            
    def collision(self, ball):
        for border in self.borders:
            collided = border.collision(ball)           
            
            if collided:
                #print("collision with", collided)
                #print (ball.box)
                return collided