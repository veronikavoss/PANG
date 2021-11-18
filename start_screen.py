#%%
from setting import *
from balloon import Balloon,Balloons_Popped_Effect
#%%
class Start_Screen:
    def __init__(self,screen,asset):
        self.screen=screen
        self.asset=asset
        self.timer=0
        self.balloon_popped={'p':False,'a':False,'n':False,'g':False}
        self.logo=False
        
        self.balloons=pygame.sprite.Group()
        self.balloons_popped_effect=pygame.sprite.Group()
    
    def set_balloons(self):
        self.timer+=1
        if not self.logo:
            if self.timer==20:
                self.balloons.add(Balloon(self.asset,'red',0,(screen_width,0),True,False,index=1,speed=9))
            elif self.timer==40:
                self.balloons.add(Balloon(self.asset,'red',0,(0,0),False,False,index=2,speed=6))
            elif self.timer==50:
                self.balloons.add(Balloon(self.asset,'red',0,(screen_width,0),True,False,index=3,speed=6))
            elif self.timer==60:
                self.balloons.add(Balloon(self.asset,'red',0,(0,0),False,False,index=4,speed=10))
            
            for balloon in self.balloons:
                if self.timer>=100 and balloon.index==1:
                    self.balloons_popped_effect.add(Balloons_Popped_Effect(self.asset,'red',0,balloon.rect.center))
                    balloon.kill()
                    self.asset.start_screen_balloon_popped_sound.play()
                    self.balloon_popped['p']=True
                elif self.timer>=110 and balloon.index==2:
                    self.balloons_popped_effect.add(Balloons_Popped_Effect(self.asset,'red',0,balloon.rect.center))
                    balloon.kill()
                    self.balloon_popped['a']=True
                elif self.timer>=120 and balloon.index==3:
                    self.balloons_popped_effect.add(Balloons_Popped_Effect(self.asset,'red',0,balloon.rect.center))
                    balloon.kill()
                    self.balloon_popped['n']=True
                elif self.timer>=130 and balloon.index==4:
                    self.balloons_popped_effect.add(Balloons_Popped_Effect(self.asset,'red',0,balloon.rect.center))
                    balloon.kill()
                    self.balloon_popped['g']=True
        if self.timer>=200:
            self.logo=True
    
    def animation(self):
        if self.balloon_popped['p']==True:
            self.screen.blit(self.asset.PANG[0],(0,0))
        if self.balloon_popped['a']==True:
            self.screen.blit(self.asset.PANG[1],(0,0))
        if self.balloon_popped['n']==True:
            self.screen.blit(self.asset.PANG[2],(0,0))
        if self.balloon_popped['g']==True:
            self.screen.blit(self.asset.PANG[3],(0,0))
    
    def text(self):
        self.start=self.asset.font_40.render('PRESS ANY KEY',True,'white')
        self.start_rect=self.start.get_rect(center=(screen_width//2,screen_height-70))
        if self.timer>=40:
            self.screen.blit(self.start,self.start_rect)
        if self.timer>=80:
            self.timer=0
    
    def update(self):
        self.set_balloons()
    
    def draw(self):
        self.screen.fill('black')
        if not self.logo:
            self.animation()
        else:
            self.asset.pang_logo.set_colorkey((17,17,17))
            self.screen.blit(self.asset.pang_logo,(0,0))
            self.text()
        print(self.timer)