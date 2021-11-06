#%%
from setting import *
from asset import Asset
#%%
class Weapon(pygame.sprite.Sprite,Asset):
    def __init__(self,midtop):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        self.get_weapon()
        self.weapon_type='weapon3'
        self.index=0
        self.image=self.weapon_images[self.weapon_type][self.index]
        self.rect=self.image.get_rect(midtop=midtop)
        self.animation_speed=0.1
        self.flip=False
        self.launched=True
    
    def animation(self):
        animation=self.weapon_images[self.weapon_type]
        self.rect.y-=8
        self.index+=self.animation_speed
        if self.index>=2:
            self.index=0
        if self.rect.top<=stage_top:
            if self.weapon_type=='weapon1':
                self.kill()
                self.launched=False
            elif self.weapon_type=='weapon2':
                self.index=2
                self.rect.top=stage_top
        self.image=animation[int(self.index)]
    
    def update(self):
        self.animation()