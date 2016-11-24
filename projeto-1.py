import pygame
from pygame.locals import *
from random import randrange

pygame.init() 
pygame.font.init()
pygame.mixer.pre_init(44100, 32, 2, 4096) 

font_name = pygame.font.get_default_font() 

game_font = pygame.font.SysFont(font_name, 72) 
score_font = pygame.font.SysFont(font_name, 35) 
level_font = pygame.font.SysFont(font_name, 40)

screen = pygame.display.set_mode((777, 437), 0, 32)

background_filename = 'fundo.png' 
background = pygame.image.load(background_filename).convert()

nave = {
    'tela': pygame.image.load('nave.png').convert_alpha(),
    'posicao': [350,350],
    'velocidade': {
        'x': 0,
    }
}

explosion_sound = pygame.mixer.Sound('boom.wav')
bg_sound = pygame.mixer.Sound('bg.wav')
explosion_played = False 
pygame.display.set_caption('Projeto') 



def create_inimigo():
    return {
        'tela': pygame.image.load('inimigo.png').convert_alpha(),
        'posicao': [randrange(892), -64],
        'velocidade': randrange(1)
    }

ticks_to_inimigos = 200 
inimigos = []

def move_inimigos():
    for inimigo in inimigos:
        inimigo['posicao'][1] += inimigo['velocidade']


def get_rect(obj): 
    return Rect(obj['posicao'][0],
                obj['posicao'][1],
                obj['tela'].get_width(),
                obj['tela'].get_height())


def nave_collided(): 
    nave_rect = get_rect(nave)
    for inimigo in inimigos:
        if nave_rect.colliderect(get_rect(inimigo)): 
            return True
    
    return False

collided = False
pontos = 0
ticks = 0
tick_musica = 0
while True:
    if not ticks_to_inimigos:
        ticks_to_inimigos = 200 
        inimigos.append(create_inimigo()) 
        
    else:
        ticks_to_inimigos -= 1 
        
    nave['velocidade'] = {
        'x': 0,
    }
    

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    ticks += 1
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] : 
     nave['velocidade']['x'] = -2 
    elif pressed_keys[K_RIGHT] :
     nave['velocidade']['x'] = 2
     

    screen.blit(background, (0, 0)) 
    
    
    txt = score_font.render('SCORE:'+str(pontos)+' ',1 ,(250,0,0))

    if(ticks >= 1000):

        inimigo['velocidade'] = 1
    if (ticks >= 10000):
        inimigo['velocidade'] = 2
    if (ticks >= 20000):
        inimigo['velocidade'] = 3
    if (ticks >= 35000):
        inimigo['velocidade'] = 4
    if (ticks >= 45000):
        inimigo['velocidade'] = 5
    if (ticks >= 55000):
        inimigo['velocidade'] = 6
    if (ticks >= 60000):
        inimigo['velocidade'] = 7
    if (ticks >= 70000):
        inimigo['velocidade'] = 8
    if (ticks >= 100000):
        inimigo['velocidade'] = 9
    if (ticks >= 200000):
        inimigo['velocidade'] = 10
        
        
    if collided == False:
        screen.blit(txt, (10, 10))
    else:
       screen.blit(txt, (200, 150)) 
    move_inimigos() 

    for inimigo in inimigos:
        screen.blit(inimigo['tela'], inimigo['posicao']) 

    if not collided: 
        if (tick_musica == 0):
            bg_sound.play()
            tick_musica += 1
        else:
            tick_musica += 1
        collided = nave_collided() 
        nave['posicao'][0] += nave['velocidade']['x'] 
        pontos += 1
        screen.blit(nave['tela'], nave['posicao'])
        
    else:
        if not explosion_played: 
            bg_sound.stop()
            explosion_played = True 
            explosion_sound.play() 
            nave['posicao'][0] += nave['velocidade']['x'] 
            
            
            screen.blit(nave['tela'], nave['posicao'])
        else:
            text = game_font.render('GAME OVER', 1, (255, 0, 0)) 
            
            screen.blit(text, (200, 175)) 
            

    if(nave['posicao'][0] > 725):
        nave['posicao'][0] = 725
    if(nave['posicao'][0] < 0):
        nave['posicao'][0] = 0

    pygame.display.update()
