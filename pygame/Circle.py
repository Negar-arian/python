import pygame
import numpy as np
import random
pygame.init()
a=1300
b=600
screen=pygame.display.set_mode((a,b))
pygame.display.set_caption('ball 2')
run=True
x=750
y=450
x1=50
x2=150
x3=200
y1=20
y2=20
y3=20
x4=a
x5=0
y4=150
y5=300
speedcirc=170
move=0
move1=0
S=50
c4=4
c5=2
c1=3
c2=4
c3=6
r1=3
r2=4
r3=6
while run:
    d1=np.sqrt((x-x1)**2+(y-y1)**2)
    d2=np.sqrt((x-x2)**2+(y-y2)**2)
    d3=np.sqrt((x-x3)**2+(y-y3)**2)
    d4=np.sqrt((x-x4)**2+(y-y4)**2)
    d5=np.sqrt((x-x5)**2+(y-y5)**2)
    f=S+10
    if d1<=f or d2<=f or d3<=f or d4<=f or d5<=f:
        S=S-5
    if (S<=10):
        font=pygame.font.SysFont('calibri',70)
        over=font.render(('GAME OVER'),True,(255,0,0))
        screen.blit(over,(200,100))
        pygame.display.update()
        run=False
        break
    y1=y1+c1
    y2=y2+c2
    y3=y3+c3
    x1=x1+r1
    x2=x2+r2
    x3=x3+r3
    x4=x4-c4
    x5=x5+c5
    if y1>=b or y1<=0:
        c1=-c1
    if x1>=a or x1<=0:
        r1=-r1
    if x2>=a or x2<=0:
        r2=-r2    
    if x4<=0 or x4>=a:
        c4=-c4
    if x3>=a or x3<=0:
        r3=-r3    
    if x5<=0 or x5>=a:     
        c5=-c5
    if y2>=b or y2<=0:
        c2=-c2
    if y3>=b or y3<=0:
        c3=-c3
        
    clock=pygame.time.Clock()
    timepassed=clock.tick(30)
    timesec=timepassed/1000
    aispeed=speedcirc*timesec
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                move=-aispeed
                #if y<=0:
                    #y=b-25
            if event.key==pygame.K_DOWN:
                move=aispeed
                #if y>=b:
                    #y=25
            if event.key==pygame.K_LEFT:
                move1=-aispeed
                #if y<=0:
                    #x=a-25
            if event.key==pygame.K_RIGHT:
                move1=aispeed
                #if x>=a:
                #x=25
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                move1=0
            if event.key==pygame.K_RIGHT:
                move1=0
            if event.key==pygame.K_UP:
                move=0
            elif event.key==pygame.K_DOWN:
                move=0
    y+=move
    x+=move1
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(200,0,100),(x,y),S,0)
    pygame.draw.circle(screen,(20,100,0),(x1,y1),10,0)
    pygame.draw.circle(screen,(250,100,0),(x2,y2),10,0)
    pygame.draw.circle(screen,(100,100,0),(x3,y3),10,0)
    pygame.draw.circle(screen,(250,200,0),(x4,y4),10,0)
    pygame.draw.circle(screen,(250,200,0),(x5,y5),10,0)
    pygame.draw.rect(screen,(0,0,0),(0,0,100,100),3)
    if x<=100 and y<=100:
        font=pygame.font.SysFont('calibri',70)
        won=font.render(('YOU WON'),True,(0,255,0))
        screen.blit(won,(200,100))
        pygame.display.update()
        run=False
        
    pygame.display.update()
  
    
