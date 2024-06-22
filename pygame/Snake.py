
from cmath import rect
from dis import dis
from multiprocessing.sharedctypes import Value
from pyexpat.errors import messages
import random,time
from tkinter import font
import pygame
import numpy as np
a=600
b=400
pygame.init()
font_style=pygame.font.SysFont(None,40)
close=False
dis=pygame.display.set_mode((a,b))
def yourscore(score):
  value=pygame.font.SysFont(None,28).render('your score: '+str(score),True,(0,0,0))
  dis.blit(value,(0,0))
def message(msg,xm,ym):
  mesg=font_style.render(msg,True,(0,0,0))
  dis.blit(mesg,(xm,ym))
def oursnake(snakelist,s):
  for x in snakelist:
     pygame.draw.circle(dis,(255,110,100),(x[0],x[1]),s,5)
     pygame.draw.circle(dis,(255,0,50),(x[0],x[1]),5,5)

def game_loop():
  x=300
  y=200 
  xch=0
  ych=0
  s=7
  f=5
  bx1=round(random.randrange(5,a-50))
  by1=round(random.randrange(5,y-50))
  bx2=round(random.randrange(5,a-50))
  by2=round(random.randrange(5,y-50))
  if bx1<=bx2+200 and bx1>=bx2-100 and by1<=by2+200 and by1>=by2-100:
    bx1=bx2
    by1=by2

  foodx=round(random.randrange(0,a-10))
  foody=round(random.randrange(0,b-10))
  if foodx>=bx1-5 and foodx<=bx1+105 and foody>=by1-5 and foody<=by1+105:
    foodx=0
    foody=0
  if foodx>=bx2-5 and foodx<=bx2+105 and foody>=by2-5 and foody<=by2+105:
    foodx=0
    foody=0
  color=round(random.randrange(20,255))
  clock=pygame.time.Clock()
  pygame.display.set_caption('snake')
  game_over=False
  close=False
  snakelist=[]
  lsnake=1
 
  while not game_over:  
      
      while close==True:
        message('GAME OVER',a/6,b/2)
        message('press c to play again',a/6,300)
        yourscore(lsnake-1)
        pygame.display.update()
        
        print(yourscore)
        for event in pygame.event.get(): 
           if event.type==pygame.QUIT:
               game_over=True
               close=False
           if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_c:   
                   game_loop() 
               if event.key==pygame.K_q:
                 game_over=True
                 close=False
        
              

      for event in pygame.event.get(): 
           if event.type==pygame.QUIT:
               game_over=True
               close=False
           if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_c:   
                   game_loop() 
               if event.key==pygame.K_q:
                 game_over=True
                 close=False
               if event.key==pygame.K_LEFT:
                 xch=-7
                 ych=0
               if event.key==pygame.K_RIGHT:
                 xch=7
                 ych=0 
               if event.key==pygame.K_UP:
                 ych=-7
                 xch=0
               if event.key==pygame.K_DOWN:
                   xch=0
                   ych=7   
               
      
      if x>=a or x<=0 or y<=0 or y>=b:
           close=True
      if x>=bx1-8 and x<=bx1+108 and y>=by1-8 and y<=by1+108:
           close=True
      if x>=bx2-8 and x<=bx2+108 and y>=by2-8 and y<=by2+108:
           close=True     
      x=x+xch
      y=y+ych           
      dis.fill((255,155,225)) 
        
      pygame.draw.circle(dis,(color,100,color),(foodx,foody),f,0) 
      pygame.draw.rect(dis,(150,100,151),(bx1,by1,100,100),5) 
      pygame.draw.rect(dis,(150,100,151),(bx2,by2,100,100),5) 
      #print(color)

        
         
      snakehead=[]
      snakehead.append(x)
      snakehead.append(y)
      snakelist.append(snakehead)
      if len(snakelist)>lsnake:
        del snakelist[0]
      for x in snakehead[:-1]:
        if x==snakehead:
          game_over=True
      for i in snakelist[:-1]:
        if i==[x,y]:    
           close=True
      oursnake(snakelist,s)
      yourscore(lsnake-1)
      #print(snakelist)
      d=np.sqrt((x-foodx)**2+(y-foody)**2)
      n=s+f
      if d<=n :
        lsnake+=1
        foodx=round(random.randrange(10,a-10))
        foody=round(random.randrange(10,b-10))
        if foodx>=bx1-5 and foodx<=bx1+105 and foody>=by1-5 and foody<=by1+105:
          foodx=300
          foody=200
          if foodx>=bx1-5 and foodx<=bx1+105 and foody>=by1-5 and foody<=by1+105:
            foodx=100
            foody=100
        if foodx>=bx2-5 and foodx<=bx2+105 and foody>=by2-5 and foody<=by2+105:
             foodx=300
             foody=200
             if foodx>=bx1-5 and foodx<=bx1+105 and foody>=by1-5 and foody<=by1+105:
                 foodx=400
                 foody=300
        color=round(random.randrange(30,240))  



      pygame.display.update()
      clock.tick(18)    #18 fram per secend if not use ,too many in secend=move so fast  
    
game_loop()            
