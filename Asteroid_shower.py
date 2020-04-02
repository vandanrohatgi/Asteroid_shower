import pygame 
import random 
import sys
from functions_for_game import close,press_key,text,collision,add_ast,remove_ast
 
min_ast_size=20
max_ast_size=200
min_ast_speed=1
max_ast_speed=3

playerspeed=70
screen_width=1000
screen_height=1000

text_color=(0,255,0)
background_color=(30,0,100)


 
#initialize
pygame.init()
#start clock
clock=pygame.time.Clock()

#start display
displayy=pygame.display.set_mode((screen_height,screen_width))
displayy.fill(background_color)
pygame.display.flip()

pygame.display.set_caption('Asteroids!')

#load images of asteroids and spaceship
spaceship=pygame.image.load('rocket.png').convert_alpha()
astroid=pygame.image.load('comet.png').convert_alpha()

spaceship=pygame.transform.scale(spaceship,(100,100))
player=pygame.Rect(500,900,100,100)

#start game
while True:
    text('press any key to begin!',(500,500),displayy)
    pygame.display.flip()
    press_key()
    displayy.fill(background_color)
    displayy.blit(spaceship,player)
    player.center=(500,900)
    pygame.display.update()

    #list for current asteroids
    ast_list=[]

    score=0
    #start the game
    while True:
        score+=0.5
        #check which key is pressed and move ship accordingly
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                y=player.centery
                x=player.centerx
                if event.key==pygame.K_UP and y>100:
                    player.centery-=playerspeed
                elif  event.key==pygame.K_DOWN and y<900:
                    player.centery+=playerspeed
                elif  event.key==pygame.K_RIGHT and x<900:
                    player.centerx+=playerspeed
                elif  event.key==pygame.K_LEFT and x>100:
                    player.centerx-=playerspeed

        #keep approx. 5 asteroids on screen at once
        if len(ast_list)<5:
            ast_list=add_ast(ast_list,astroid,min_ast_size,max_ast_size)
        if len(ast_list)>=5:
            ast_list=remove_ast(ast_list)
        
        #move each asteroid 
        for x in ast_list:
            x['rect'].move_ip(-1*x['speed'],x['speed'])
        
        #update screen with new postions of objects
        displayy.fill(background_color)
        for t in ast_list:
            displayy.blit(t['surface'],t['rect'])
        displayy.blit(spaceship,player)
        text('score:'+str(score),(300,50),displayy)
        pygame.display.flip()
        clock.tick(200)

        #detect collision
        if collision(player,ast_list):
            displayy.fill(background_color)
            text('game over!',(500,500),displayy)
            text('final score:'+str(score),(500,600),displayy)
            pygame.display.flip()
            displayy.fill(background_color)
            press_key()
            break



            

