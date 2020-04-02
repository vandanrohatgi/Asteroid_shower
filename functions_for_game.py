import pygame 
import random 
import sys

ast_size=[50,150,200]
ast_speed=[1,2,3,4]

playerspeed=70
screen_width=1000
screen_height=1000

text_color=(0,255,0)
background_color=(30,0,100)
pygame.init()
fontt=pygame.font.SysFont("comicsansms",48)

#for smooth closing of game
def close():
    sys.exit()
    pygame.quit()

#for when player has to press a key to start/exit game
def press_key():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE or event.type==pygame.QUIT:
                    close()
                else:
                    return
            else:
                continue

#to display text on game screen
def text(text,position,surface):
    text1=fontt.render(text,True,text_color)
    text1_rect=text1.get_rect()
    text1_rect.center=position
    surface.blit(text1,text1_rect)

#check if player hit an asteroid
def collision(player_rect,ast_list):
    for a in ast_list:
        if a['rect'].colliderect(player_rect):
                return True
    return False

#to add new asteroids to the screen
def add_ast(ast_list,astroid_pic,min_ast_size,max_ast_size):
    size=random.choice(ast_size)
    if size!=200:
        speed=random.choice(ast_speed)
    else:
        speed=1
    #dictionary to define attributes of new asteroids
    new_ast={'surface':pygame.transform.scale(astroid_pic,(size,size)),
    'speed':speed,
    'rect':pygame.Rect(random.randint(0,2000),0,size-30,size-30)}
    ast_list.append(new_ast)
    return(ast_list)

#to remove the asteroids that have left the view 
def remove_ast(ast_list):
    toremove=None
    for a in ast_list:
        if a['rect'].centerx<0 or a['rect'].centery>1000:
            toremove=a
            break
    if toremove:
        ast_list.remove(toremove)
    return(ast_list)