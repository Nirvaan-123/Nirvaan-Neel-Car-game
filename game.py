import pygame
import sys
import random 
from pygame.locals import * 

FPS = 64
WIDTH , HEIGHT = 250, 450


pygame.init()
FPSCLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nirvaan and Neel car game")

# Assets
message = 'Pics/message.png'
CAR = 'Pics/redcar.png'
ENEMY = 'Pics/bluecar.png'
ROAD = 'Pics/road.png'
lane1 ='Pics/lane1.png' 
lane2 = 'Pics/lane2.png'
lane3 = 'Pics/lane3.png'


GAME_SPRITES = {}
GAME_SPRITES['message'] = pygame.image.load(message).convert_alpha()
GAME_SPRITES['car'] = pygame.image.load(CAR).convert_alpha()
GAME_SPRITES['enemy'] = pygame.image.load(ENEMY).convert_alpha()
GAME_SPRITES['enemy2'] = pygame.image.load(ENEMY).convert_alpha()
GAME_SPRITES['road'] = pygame.image.load(ROAD).convert_alpha()
GAME_SPRITES['lane1'] = pygame.image.load(lane1).convert_alpha()
GAME_SPRITES['lane2'] = pygame.image.load(lane2).convert_alpha()
GAME_SPRITES['lane3'] =pygame.image.load(lane3).convert_alpha()

lane1width, lane1height = GAME_SPRITES['lane1'].get_width(), GAME_SPRITES['lane1'].get_height()
lane2width, lane2height = GAME_SPRITES['lane2'].get_width(), GAME_SPRITES['lane2'].get_height()
lane3width, lane3height = GAME_SPRITES['lane3'].get_width(), GAME_SPRITES['lane3'].get_height()

car_x =  114    # 33.5 # 114 # 196.5
car_y = 300
car_speed = 84
high_score = 0
score = 0


def display_high_score(screen, high_score):
    font = pygame.font.Font(None, 40)
    high_label_surface = font.render("High Score:", True, (255, 255, 255))  # White text
    high_score_surface = font.render(str(high_score), True, (10, 70, 200))  # Black text
    
    screen.blit(high_label_surface, (WIDTH // 2 - 100, 15))
    screen.blit(high_score_surface, (WIDTH // 2 + 60, 17))
def start_screen():
    global high_score
    
    
    while True:
        if score > high_score:
            high_score = score
        

        screen.blit(GAME_SPRITES['road'],(0, 0))
        screen.blit(GAME_SPRITES['car'],(117, 278))
        screen.blit(GAME_SPRITES['message'],(25, 50))
        
        display_high_score(screen, int(high_score))

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key in [K_ESCAPE, K_q]):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key in [K_SPACE, K_UP] or event.type == MOUSEBUTTONDOWN:
                return game_screen()

def display_score(screen, score):
    """Render and display only the score on the screen (not high score)."""
    font = pygame.font.Font(None, 40)
    label_surface = font.render("Score:", True, (255, 255, 255))  # White text
    score_surface = font.render(str(score), True, (10, 70, 200))  # Black text

    screen.blit(label_surface, (WIDTH // 2 - 50, 15))
    screen.blit(score_surface, (WIDTH // 2 + 40, 17))
    
    
def getrandomenemy():
    choices = [33, 114, 196]
    lane_choices = random.choice(choices)
    return lane_choices
    
def game_screen():
    global score
    global car_x,car_y
    score = 0
    enemyx = getrandomenemy()
    enemyy = -50
    
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key in [K_ESCAPE, K_q]):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and car_x == 114:
                    car_x = 196
                if event.key == K_RIGHT and car_x == 33:
                    car_x = 114
                if event.key == K_LEFT and car_x == 114:
                    car_x = 33
                if event.key == K_LEFT and car_x == 196:
                    car_x = 114
                if car_x <33:
                    car_x = 33
                if car_x > 196:
                    car_x = 196
                
        if collided(enemyx, enemyy, car_x, car_y):
            return start_screen()
            
        
                
                    
        screen.fill((0, 0, 0))
        
        screen.blit(GAME_SPRITES['road'],(0,0))
        screen.blit(GAME_SPRITES['car'],(car_x, car_y))
        screen.blit(GAME_SPRITES['enemy'],(enemyx, enemyy))
        
        enemyy += 2.5
        
        if enemyy > 400:
            enemyy = -50
            enemyx = getrandomenemy()
        
        score += 0.41

        display_score(screen,int(score//1))
    
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
        

def collided(enemyx, enemyy, car_x, car_y):
    enemy_width, enemy_height = GAME_SPRITES['enemy'].get_width(), GAME_SPRITES['enemy'].get_height() 
    car_width, car_height = GAME_SPRITES['car'].get_width(), GAME_SPRITES['car'].get_height()

    enemy_mask = pygame.mask.from_surface(GAME_SPRITES['enemy'])
    car_mask= pygame.mask.from_surface(GAME_SPRITES['car'])
    
    enemyx, enemyy = int(enemyx), int(enemyy)
    car_x, car_y = int(car_x), int(car_y)

    enemy_rect = pygame.Rect(enemyx, enemyy, enemy_width, enemy_height)
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)

    if enemy_rect.colliderect(car_rect):
        offsetx = enemy_rect.x - car_rect.x
        offsety = enemy_rect.y - car_rect.y

        if car_mask.overlap(enemy_mask, (offsetx, offsety)):
            return True
        return False

while True:
    start_screen()
    game_screen()
            