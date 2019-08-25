import pygame 
import random 
import sys

min_ast_size=20
max_ast_size=200
min_ast_speed=1
max_ast_speed=3

playerspeed=70
screen_width=1000
screen_height=1000

text_color=(0,255,0)
background_color=(30,0,100)

def close():
    sys.exit()
    pygame.quit()

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
def text(text,position,surface):
    text1=font.render(text,True,text_color)
    text1_rect=text1.get_rect()
    text1_rect.center=position
    surface.blit(text1,text1_rect)

def collision(player_rect,ast_list):
    for a in ast_list:
        if a['rect'].colliderect(player_rect):
                return True
    return False

def add_ast(ast_list,astroid_pic,min_ast_size,max_ast_size):
    size=random.randint(min_ast_size,max_ast_size)
    if size!=max_ast_size:
        speed=random.randint(min_ast_speed,max_ast_speed)
    else:
        speed=min_ast_speed
    new_ast={'surface':pygame.transform.scale(astroid_pic,(size,size)),
    'speed':speed,
    'rect':pygame.Rect(random.randint(0,2000),0,size,size)}
    ast_list.append(new_ast)
    return(ast_list)

def remove_ast(ast_list):
    toremove=None
    for a in ast_list:
        if a['rect'].centerx<0 or a['rect'].centery>1000:
            toremove=a
            break
    if toremove:
        ast_list.remove(toremove)
    return(ast_list) 

pygame.init()
font=pygame.font.SysFont(None,48)
displayy=pygame.display.set_mode((screen_height,screen_width))
displayy.fill(background_color)
pygame.display.flip()

pygame.display.set_caption('Asteroids!')
spaceship=pygame.image.load('rocket.png').convert_alpha()
astroid=pygame.image.load('comet.png').convert_alpha()

spaceship=pygame.transform.scale(spaceship,(100,100))
player=pygame.Rect(500,900,100,100)

while True:
    text('press any key to begin!',(500,500),displayy)
    pygame.display.flip()
    press_key()
    displayy.fill(background_color)
    displayy.blit(spaceship,player)
    player.center=(500,900)
    pygame.display.update()

    ast_list=[]
    score=0
    while True:
        score+=0.1
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
        if len(ast_list)<5:
            ast_list=add_ast(ast_list,astroid,min_ast_size,max_ast_size)
        if len(ast_list)>=5:
            ast_list=remove_ast(ast_list)
        for x in ast_list:
            x['rect'].move_ip(-1*x['speed'],x['speed'])
        displayy.fill(background_color)
        for t in ast_list:
            displayy.blit(t['surface'],t['rect'])
        displayy.blit(spaceship,player)
        text('score:'+str(score),(300,50),displayy)
        pygame.display.flip()
        if collision(player,ast_list):
            displayy.fill(background_color)
            text('game over!',(500,500),displayy)
            text('final score:'+str(score),(500,600),displayy)
            pygame.display.flip()
            displayy.fill(background_color)
            press_key()
            break



            

