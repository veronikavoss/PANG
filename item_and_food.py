#%%
from setting import *
from asset import Asset
#%%
class Item_and_Food(pygame.sprite.Sprite,Asset):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
    
#%%
