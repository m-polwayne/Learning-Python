import time
import pygame
import random



pygame.init()
i = 1

# coordinate

x_0 = 200
y_0 = 200

x = random.randint(10, 750)
y = random.randint(10, 750)

# object size
width = 10
height = 10
# speed
speed = 0.2
#score
score=0

#functions
def speedIncrease():
    global score,speed
    if score>=50:
        speed=0.4
    if score>=80:
        speed=0.6
    if score>=100:
        speed=0.8
    if score>=130:
        speed=1.5

def food():
    global score,x,y,x_0,y_0
    xx = round(x, -1)
    xe = round(x_0, -1)
    yy = round(y, -1)
    ye = round(y_0, -1)
    if xx == xe and yy == ye:
        x = random.randint(10, 750)
        y = random.randint(10, 750)
        score+=10 

def moving():
    global direction,x_0,y_0

    if direction == 'right' :
        x_0 += speed
    if direction == 'left' :
        x_0 -= speed
    if direction == 'up' :
        y_0 -= speed
    if direction == 'down' :
        y_0 += speed

#default direction
direction = 'right'
  

while i < 2:
    windo = pygame.display.set_mode((800, 800))
    #windo.fill((255, 255, 255)) 
    #pygame.draw.rect(windo, (0, 0, 0), (700, 700))
    pygame.draw.rect(windo, (200, 100, 100), (x_0, y_0, width, height))
    pygame.draw.rect(windo, (255, 200, 0), (x, y, width, height))

    pygame.display.update()
    if x_0 >= 800 or y_0 >= 800 or x_0 <= 0 or y_0 <= 0:
        i = 3
    if pygame.key.get_pressed()[pygame.K_RIGHT] and direction != 'left':
        direction = 'right'
    if pygame.key.get_pressed()[pygame.K_LEFT] and direction != 'right':
        direction = 'left'
    if pygame.key.get_pressed()[pygame.K_UP] and direction != 'down':
        direction = 'up'
    if pygame.key.get_pressed()[pygame.K_DOWN] and direction != 'up':
       direction = 'down'


    speedIncrease()
    food()
    moving()
   
