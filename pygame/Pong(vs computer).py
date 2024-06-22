import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('pong')
bar1x=10
bar1y=215
bar2x=620
bar2y=215
circlex=320
circley=240
bar1move=0
bar2move=0
speedx=250
speedy=250
speedcirc=250
bar1score,bar2score=0,0
clock=pygame.time.Clock()
font=pygame.font.SysFont('calibri',40)
run=True
while run:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_a:
                bar1move=-aispeed*2
            elif event.key==K_z:
                bar1move=aispeed*2
        elif event.type==KEYUP:
            if event.key==K_a:
                bar1move=0
            elif event.key==K_z:
                bar1move=0
    if bar1score==10 or bar2score==10:
        run=False
        break
    screen.fill((100,255,100,255))
    score1=font.render(str(bar1score),True,(0,0,0))
    score2=font.render(str(bar2score),True,(0,0,0))
    screen.blit(score1,(250,210))
    screen.blit(score2,(380,210))
    middleline=pygame.draw.aaline(screen,(0,0,0),(320,5),(320,470))
    frame=pygame.draw.rect(screen,(0,0,0),Rect((5,5),(630,470)),2)
    pygame.draw.rect(screen,(255,0,0),(bar1x,bar1y,10,50),0)
    pygame.draw.rect(screen,(0,0,255),(bar2x,bar2y,10,50),0)
    pygame.draw.circle(screen,(255,255,100),(circlex,circley),7.5,0)
    bar1y+=bar1move
    timepassed=clock.tick(30)
    timesec=timepassed/1000
    circlex+=1/2*speedx*timesec
    circley+=1/2*speedy*timesec
    aispeed=speedcirc*timesec
    if circlex>=305:
      if not bar2y==circley:
        if bar2y<circley:
            bar2y+=aispeed
        if bar2y>circley:
            bar2y-=aispeed
      else:
         bar2y=circley+7.5
    if bar2y>=420:
      bar2y=420
    elif bar2y<=10:
      bar2y=10
    if bar1y>=420:
      bar1y=420
    elif bar1y<=10:
      bar1y=10
    if circlex<=bar1x+10:
      if circley>=bar1y-7.5 and circley<=bar1y+62:
        speedx=-speedx
        circlex=20
      
    if circlex>=bar2x-15:
      if circley>=bar2y-7.5 and circley<=bar2y+45:
        speedx=-speedx
        circlex=605

    if circley<=10:
        speedy=-speedy
        circley=10
    elif circley>=457.5:
        speedy=-speedy
        circley=457.5
    if circlex<5:
        bar2score+=1
        circlex,circley=320,232.5
        bar1y,bar2y=215,215
    elif circlex>620:
        bar1score+=1
        circlex,circley=307.5,232.5
        bar1y,bar2y=215,215

    pygame.display.update()

    
                
