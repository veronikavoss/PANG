#%%
from setting import *
#%%
class Item_and_Food(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((24,24),pygame.SRCALPHA)
        self.image.fill((250,250,250,10))
        self.rect=self.image.get_rect(x=x,y=y)
    
#%%
