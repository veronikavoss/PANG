#%%
from setting import *
from asset import Asset
#%%
class Background(Asset):
    def __init__(self,screen,level):
        Asset.__init__(self)
        self.background()
        self.screen=screen
        self.background_image=self.background_images[level-1]
    
    def draw(self):
        self.screen.blit(self.background_image,(0,0))

class Foreground(Asset):
    def __init__(self,screen,level):
        Asset.__init__(self)
        self.foreground()
        self.screen=screen
        self.foreground_image=self.foreground_images[level-1]
    
    def draw(self):
        self.screen.blit(self.foreground_image,(0,0))