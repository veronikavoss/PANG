#%%
from setting import *
from asset import Asset
#%%
class Weapon(pygame.sprite.Sprite,Asset):
    def __init__(self,midtop,weapon_type):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        self.get_weapon()
        self.weapon_type=weapon_type
        self.index=0
        self.image=self.weapon_images[self.weapon_type][self.index]
        self.rect=self.image.get_rect(midtop=midtop)
        self.animation_speed=0.1
        self.flip=False
    
    def animation(self):
        animation=self.weapon_images[self.weapon_type]
        self.rect.y-=8
        self.index+=self.animation_speed
        
        if self.rect.top<=stage_top:
            if self.weapon_type=='normal':
                self.rect.top=stage_top
                self.index=0
                self.kill()
            elif self.weapon_type=='vulcan_missile':
                self.rect.top=stage_top
                if self.index>=len(animation):
                    self.index=0
                    self.kill()
            elif self.weapon_type=='power_wire':
                self.index=2
                self.rect.top=stage_top
        else:
            if self.weapon_type=='vulcan_missile':
                if self.index>=5:
                    self.index=3
            else:
                if self.index>=2:
                    self.index=0
        self.image=animation[int(self.index)]
    
    def update(self):
        self.animation()
        

class Launch_Effect(pygame.sprite.Sprite,Asset):
    def __init__(self,midbottom):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        self.get_launch_effect()
        self.index=0
        self.image=self.launch_effects[self.index]
        self.rect=self.image.get_rect(midbottom=midbottom)
        self.animation_speed=0.2
    
    def animation(self):
        self.index+=self.animation_speed
        animation=self.launch_effects
        if self.index>=len(animation)-1:
            self.kill()
        self.image=animation[int(self.index)]
    
    def update(self):
        self.animation()