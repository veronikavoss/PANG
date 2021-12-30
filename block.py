#%%
from setting import *
#%%
class Block(pygame.sprite.Sprite):
    def __init__(self,asset,x,y,color,size):
        super().__init__()
        self.asset=asset
        self.block_images=self.asset.block_images
        self.index=0
        self.image=self.block_images[color][size][self.index]
        self.rect=self.image.get_rect(x=x,y=y)