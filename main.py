"""
Let's make rock paper scissor game.
Language:python,
game engine:pygame 
"""
#import all classes,variable,function from pygame.
from pygame import *
#import randint function from random for the random choice of computer.
from random import randint
#import sleep from time for delay.
from time import sleep
#initialization the variables,pygame.
init()
"""important variables"""
#set the screen with FULLSCREEN.
window=display.set_mode((1200,400))
#clock for fps
clock=time.Clock()
#the value of fps
FPS=60
#white color rgb.
white=(255,255,255)
#black color rgb.
black=(0, 0, 0)
#photos of rock paper scissor.
paper=image.load('paper.png')
scissor=image.load('scissor.png')
rock=image.load('rock.png')
p=image.load('p.png')
c=image.load('c.png')
score=image.load('score.png')
#user choice.
user=None
clicked=False
cc=False
#resize the images.
paper=transform.scale(paper,(250,200))
scissor=transform.scale(scissor,(200,200))
rock=transform.scale(rock,(250,200))
p=transform.scale(p,(350,600))
co=transform.scale(c,(350,600))
score=transform.scale(score,(500,200))
x=0
y=0
comp=None
tie='0'
win='0'
lose='0'
compc=None
restart=False
#text.
font = font.Font('freesansbold.ttf', 64)
wintext = font.render(win, True, white, (0,255,0))  
losetext = font.render(lose, True, white, (0,255,0))  
tietext = font.render(tie, True, white, (0,255,0))  
#computer class make the random.
class computer:
    def choices(self):
        i=randint(0,2)
        return i
#result class have result.
class result:
    def get_result(self,user,comp):
        if user==comp:
            return 0
        elif user=='r' and comp=='p':
            return -1
        elif user=='r' and comp=='s':
            return 1
        elif user=='p' and comp=='r':
            return 1
        elif user=='p' and comp=='s':
            return -1
        elif user=='s' and comp=='r':
            return -1
        elif user=='s' and comp=='p':
            return 1
        else:
            self.result=-1
        return self.result  
#main class that only run in this file.    
class main(computer,result):
    #main method.
    def main(self):
        #game loop.
        while True:
            #lets global sum variables.
            global window,x,clicked,user,y,cc,comp,tie,win,lose,compc,restart,wintext,losetext,tietext
            if restart==True:
                sleep(2)
            #iterate the event on even.
            for even in event.get():
                #if user want to quit it quit with the of pygame or python.
                if even.type==QUIT:
                    quit()
                if even.type==MOUSEMOTION and clicked==False:
                        pos=mouse.get_pos()
                        x=pos[0]
                        y=pos[1]
                        if x>0 and x<270 and y>1100:
                            user='r'
                            clicked=True
                        elif x>=270 and x<490 and y>=1100:
                            user='p'
                            clicked=True
                        elif x>=490 and x<=900 and y>=1100:
                            user='s'
                            clicked=True                                            
            #set the caption.
            display.set_caption('Rock Paper Scissor')
            #fill the window with black the.
            window.fill(black)
            c=computer()
            if clicked==True:
                if user=='r':
                    window.blit(rock,(250,1000))
                elif user=='p':
                    window.blit(paper,(250,1000))
                elif user=='s':
                    window.blit(scissor,(250,1000))
            else:        
                window.blit(rock,(0,1100))
                window.blit(paper,(270,1100))
                window.blit(scissor,(500,1100))
            window.blit(p,(200,1050))
            window.blit(co,(200,0))
            window.blit(score,(120,400))
            window.blit(tietext,(380,500))
            window.blit(losetext,(550,500))
            window.blit(wintext,(180,500))
            if cc==False and clicked==True:
                    if c.choices()==0:
                        comp=rock
                        compc='r'
                        cc=True
                    elif c.choices()==1:
                        comp=paper
                        compc='p'
                        cc=True
                    elif c.choices()==2:
                        comp=scissor
                        compc='s'
                        cc=True
            if comp!=None:
                window.blit(comp,(250,150))
            if cc==True and clicked==True:
                self.result=result()
                if self.result.get_result(user,compc)==0:
                    tie=str(int(tie)+1)
                    tietext = font.render(tie, True, white, (0,255,0)) 
                elif self.result.get_result(user,compc)==1:
                    win=str(int(win)+1)
                    wintext = font.render(win, True, white, (0,255,0)) 
                elif self.result.get_result(user,compc)==-1:
                    lose=str(int(lose)+1)
                    losetext = font.render(lose, True, white, (0,255,0)) 
                cc=False
                clicked=False
                comp=None
                user=None 
                restart=True
            else:
                restart=False
            #update the screen.
            display.update()
            #set the fps on pygame.
            clock.tick(FPS)
#if the the file isn't run in this file main.py.
if __name__=='__main__':
   #rps=rock paper scissor run with main class
   rps=main()
   #and run the main method of this game.
   rps.main()
"""
footer:
thanks for read my code.
©redoansaleh1
origamimaster366@gmail.com 
"""