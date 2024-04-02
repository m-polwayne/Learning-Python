import pygame 
import random


pygame.init()
i=1
#coordinate
x_0=200
y_0=200

x=random.randint(10,750)
y=random.randint(10,750)

#object size
width=10
height=10
#speed
icrement=1



while i<2:
    windo=pygame.display.set_mode((800,800))
    pygame.draw.rect(windo, (255, 200, 0), (x_0, y_0, width, height)) 
    pygame.draw.rect(windo, (255, 255, 255), (x, y, width, height)) 
   
    pygame.display.update() 
    if x_0>=800 or y_0>=800 or x_0<=0 or y_0<=0:
        i=3
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x_0+=icrement
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x_0-=icrement
    if pygame.key.get_pressed()[pygame.K_UP]:
        y_0-=icrement
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        y_0+=icrement
    
    xx=round(x,-1)
    xe=round(x_0,-1)
    yy=round(y,-1)
    ye=round(y_0,-1)
    if xx==xe and yy==ye:
        x=random.randint(10,750)
        y=random.randint(10,750)
