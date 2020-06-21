import pygame
class Bar:
    
    def __init__(self, x, y, width, height, value = 'vertical', color = pygame.Color("green")):
        self.x = x 
        self.y = y 
        
        self.width = width
        self.height = height
        
        self.value = value
        self.color = color
        
        self.set_hitbox()
        
    def set_hitbox(self):
        self.box = pygame.Rect((self.x, self.y),(self.width, self.height))
        
        
    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.box)
    
    def update(self, surface, bg_color):
        self.draw(surface, bg_color)
        self.y = pygame.mouse.get_pos()[1]
        self.set_hitbox()
        self.draw(surface, self.color)
        
    def update_cheat(self, surface, bg_color, y):        
        self.draw(surface, bg_color)
        self.y = y
        self.set_hitbox()
        self.draw(surface, self.color)
        
    def collision(self, ball):
        if self.box.colliderect(ball.box):
            return self.value