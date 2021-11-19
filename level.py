#%%
from setting import *
from balloon import Balloon
#%%
class Level:
    def __init__(self,screen,asset):
        self.screen=screen
        self.asset=asset
        self.background_images=self.asset.background_images
        self.foreground_images=self.asset.foreground_images
        self.game_status_signal=self.asset.game_status_signal
        
        self.level=1
        self.background_image=self.background_images[self.level-1]
        self.foreground_image=self.foreground_images[self.level-1]
        
        self.timer=0
        
        self.status='ready'
        self.game_status_signal=self.game_status_signal[self.status]
        self.game_status_signal_rect=self.game_status_signal.get_rect(center=(stage_width//2,stage_height//2))
        self.status_animation=0
    
    def levels(self):
        self.balloons=pygame.sprite.Group()
        self.update_time=pygame.time.get_ticks()
        if self.level==1:
            self.time=110
            self.background_image=self.background_images[self.level-1]
            self.balloons.add(Balloon(self.asset,'red',0,(120,100),True,False))
        elif self.level==2:
            self.time=110
            self.background_image=self.background_images[self.level-1]
            self.foreground_image=self.foreground_images[self.level-1]
            self.balloons.add(Balloon(self.asset,'blue',0,(120,100),True,False))
    
    def set_game_timer(self,playing_game):
        if playing_game:
            current_time=pygame.time.get_ticks()
            self.timer=str(self.time-((current_time-self.update_time)//1000))
    
    def update(self,playing_game):
        self.set_game_timer(playing_game)
    
    def draw_text(self,playing_game,game_ready):
        if game_ready:
            self.time_text=self.asset.time_font.render(f'TIME : {self.time}',True,'white')
            self.time_text_rect=self.time_text.get_rect(right=stage_right,top=stage_top)
            self.screen.blit(self.time_text,self.time_text_rect)
        elif playing_game:
            self.time_text=self.asset.time_font.render(f'TIME : {self.timer}',True,'white')
            self.time_text_rect=self.time_text.get_rect(right=stage_right,top=stage_top)
            self.screen.blit(self.time_text,self.time_text_rect)
    
    def draw_background(self):
        self.screen.blit(self.background_image,(0,0))
    
    def draw_foreground(self):
        self.screen.blit(self.foreground_image,(0,0))
    
    def draw_status(self,game_ready):
        if game_ready:
            self.status_animation+=1
            if self.status_animation<60 or self.status_animation>70:
                self.screen.blit(self.game_status_signal,self.game_status_signal_rect)
            elif self.status_animation>60:
                pass
            if self.status_animation>=80:
                self.status_animation=60