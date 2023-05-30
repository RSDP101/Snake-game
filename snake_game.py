import pygame, random
from pygame.locals import *

#initialize pygame
pygame.init()
#create function for randomly creating a position 
def random_pos():
    x = random.randint(1,28)
    y = random.randint(4,28)

    #x = random.randint(1,28)
    #y = random.randint(4,28)
    return (x* 20, y* 20)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
score = 0
#initalize our screen

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

#pygame.Surface creates a surface which can
# overlap the screen via screen.blit
# pygame.Surface takes one parameter which is a pair (width, height)
snake = [(200, 200), (220, 200), (240,200)]
snake_skin = pygame.Surface((20,20))
#snake_skin.fill colors our surface with RGB value specified
snake_skin.fill((255,255,255))

#random apple position
apple_pos = random_pos()
apple = pygame.Surface((20,20))
apple.fill((255,0,0))

#creates border
border = pygame.Surface((20,20))
border.fill((0,0,250))

#initial direction
my_direction = LEFT
running = True

#this is a command for allowing to set FPS later
clock = pygame.time.Clock()

#define function display_score
smallfont = pygame.font.SysFont("comicsansms",30)
def display_score():
    text = smallfont.render("Score: "+str(score), True, (255,0,0))
    screen.blit(text, [0,0])

bigfont = pygame.font.SysFont("comicsansms", 50)

#same as display_score but bigger and centralized 
def final_score():
    text = bigfont.render("Score: "+str(score), True, (255,0,0))
    screen.blit(text, [200,250])

#our main loop
while running == True:
    #set FPS(frames per second) to 10
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False

    #if we notice receive something 
    if event.type == KEYDOWN:
        if event.key == K_UP:
            my_direction = UP
        if event.key == K_DOWN:
            my_direction = DOWN
        if event.key == K_LEFT:
            my_direction = LEFT
        if event.key == K_RIGHT:
            my_direction = RIGHT

    if (snake[0][0]==apple_pos[0]) and (snake[0][1]== apple_pos[1]):
        apple_pos = random_pos()
        snake.append((0,0))
        score =score +1

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 20)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 20)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 20, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] -20, snake[0][1])

    for i in range(len(snake) - 1, 0, -1):
        if snake[0]==snake[i]:
            running = False
        snake[i] = (snake[i-1][0], snake[i-1][1])
    
    if snake[0][0]<20 or snake[0][0]>560 or snake[0][1] >560 or snake[0][1]<70:
        running= False
    
    screen.fill((0,100,0))
    display_score()
    #the blit command overlap your surface in the display. parameters: surface, top left pixel where you want your image
    screen.blit(apple, apple_pos)
    for pos in snake:
        
        screen.blit(snake_skin,pos)
    for i in range( 0, 620, +20):
        screen.blit (border, (i,50))
        screen.blit (border, (i,580))
    for i in range (50, 620, +20):
        screen.blit (border, (0,i))
        screen.blit (border, (580,i))


    pygame.display.update()

running =True
while running == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False 
    final_score()
    pygame.display.update()