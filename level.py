#%%
from setting import *
#%%
class Level:
    def __init__(self):
        self.level=2
    
    def balloon_level(self):
        if self.level==1:
            self.color='red'
            self.size=0
            self.pos=(80,60)
        if self.level==2:
            self.color='green'
            self.size=1
            self.pos=(80,60)