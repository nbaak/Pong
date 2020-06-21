import os

import pygame
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

from objects.Ball import Ball
from objects.Borders import Borders
from objects.Bar import Bar

#from objects.Bar import Bar

# variables:
width   = 1200
height  =  600
border  =   20

bar_height = 100

velocity = 1


sample_enabled = False
data_file = os.path.dirname(os.path.realpath(__file__)) + "/data.csv"

color_bg = pygame.Color("black")
color_border = pygame.Color("green")
color_trail = pygame.Color("#ff9a9a")


# points
points_left = 0
points_right = 0


# draw inital
pygame.init()
surface = pygame.display.set_mode(size=(width, height))
game_box = pygame.Rect((0,0),(width,height))

# draw borders
borders = Borders()
borders.add_border(0, 0, width, border, 'horizontal', color_border)
#borders.add_border(0, 0, border, height, 'vertical', color_border)
borders.add_border(0, height-border, width, border, 'horizontal', color_border)
#borders.add_border(width-border, 0, border, height, 'vertical', color_border)

borders.draw(surface)

# place objectd
ball = Ball(v_x = -velocity, v_y = velocity, color=pygame.Color("red"))
ball.radius = 20
ball.set_position(width-ball.radius -30, height//2)

bar = Bar(width-border, height//2 + bar_height//2, border, bar_height)

player = Bar(0, height//2 + bar_height//2, border, bar_height)

# sample Data for AI
if sample_enabled:
    sample_data = open (data_file, "w")
    print ("x,y,v_x,v_y,bar.y", file=sample_data)
    
# setup AI
if not sample_enabled:
    data = pd.read_csv(data_file)
    data = data.drop_duplicates()
    data.describe()
    
    X = data.drop(columns="bar.y")
    y = data["bar.y"]
    
    ai = KNeighborsRegressor(n_neighbors=3)
    ai.fit(X, y)
    
    data_frame = pd.DataFrame(columns=['x','y','v_x','v_y'])

while True:
    event = pygame.event.poll()
    pressed = pygame.key.get_pressed()
    
    # exit game
    if event.type == pygame.QUIT or pressed[pygame.K_q]:        
        print (f"Scores:\nleft: {points_left}\nright: {points_right}")
        break        
    
    # ball leaves game
    if not game_box.colliderect(ball.box):
        if ball.v_x > 0:
            print ("left scores!")
            points_left += 1
        elif ball.v_x < 0:
            print ("right scores!")
            points_right += 1
        
        ball.reset(width-ball.radius -30, height//2,-velocity, surface, color_bg)
    
    # check collisions
    ball.collision(borders.collision(ball))
    ball.collision(player.collision(ball))
    ball.collision(bar.collision(ball))
    
    ball.update(surface, color_trail)
    
    player.update(surface, color_bg)
    
    if sample_enabled:
        #bar.update_cheat(surface, color_bg, ball.y-bar.height//2)
        bar.update(surface, color_bg)
        print (f"{ball.x},{ball.y},{ball.v_x},{ball.v_y},{bar.y}", file=sample_data)
        
    else:    
        predict = data_frame.append({'x':ball.x, 'y':ball.y, 'v_x': ball.v_x, 'v_y':ball.v_y}, ignore_index=True)
        move_to = ai.predict(predict)
        
        bar.update_cheat(surface, color_bg, move_to[0])
       
    pygame.display.flip()
    
    
pygame.quit()



