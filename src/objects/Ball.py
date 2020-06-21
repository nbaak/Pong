import pygame

class Ball(object):
    def __init__(self, x = 0, y = 0, radius = 5, v_x = 0, v_y = 0, color = pygame.Color("green")):
        self.set_position(x, y)
        # velocities
        self.v_x = v_x
        self.v_y = v_y
        
        self.color = color
        
        self.radius = radius
        
        self.set_hitbox()
        
    def set_hitbox(self):
        self.box = pygame.Rect((self.x-self.radius-1,self.y-self.radius-1),(2*(self.radius+1), 2*(self.radius+1)))
        
    def set_position(self, x, y):
        self.x = x 
        self.y = y
        
    def draw (self, surface, color):
        pygame.draw.circle(surface, color, (self.x, self.y), self.radius)
        
    def collision(self, direction):
        if direction == 'horizontal':
            self.v_y *= -1

        elif direction == 'vertical':
            self.v_x *= -1
            
        else:
            pass
        
    def update (self, surface, color):
        self.draw(surface, color)
        self.x += self.v_x 
        self.y += self.v_y 
        self.draw(surface, self.color)
        
        self.set_hitbox()
        
    def reset (self, x, y, v_x, surface, color_bg):
        self.draw(surface, color_bg)
        self.x = x 
        self.y = y 
        self.v_x = v_x
        self.draw(surface, self.color)