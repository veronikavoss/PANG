#%%
from setting import *
#%%
class Weapon(pygame.sprite.Sprite):
    def __init__(self,asset,midtop,weapon_type):
        pygame.sprite.Sprite.__init__(self)
        self.asset=asset
        self.weapon_images=self.asset.weapon_images
        self.weapon_type=weapon_type
        
        self.index=0
        self.image=self.weapon_images[self.weapon_type][self.index]
        self.rect=self.image.get_rect(midtop=midtop)
        self.animation_speed=0.1
        self.power_wire_countdown=0
        self.flip=False
        self.vulcan_missile_ceiling=False
    
    def animation(self):
        self.rect.y-=8
        animation=self.weapon_images[self.weapon_type]
        self.index+=self.animation_speed
        
        if self.rect.top<=stage_top:
            if self.weapon_type=='normal':
                self.rect.top=stage_top
                self.index=0
                self.kill()
            elif self.weapon_type=='vulcan_missile':
                self.rect.top=stage_top
                if not self.vulcan_missile_ceiling:
                    self.asset.vulcan_missile_ceiling_sound.play()
                    self.vulcan_missile_ceiling=True
                if self.index>=len(animation):
                    self.index=0
                    self.kill()
                    self.vulcan_missile_ceiling=False
            elif self.weapon_type=='power_wire':
                self.animation_speed=0
                self.rect.top=stage_top
                self.power_wire_countdown+=1
                if self.power_wire_countdown<=180:
                    self.index=2
                elif self.power_wire_countdown<=240:
                    self.index=3
                elif self.power_wire_countdown<=300:
                    self.index=4
                elif self.power_wire_countdown>=360:
                    self.kill()
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

class Launch_Effect(pygame.sprite.Sprite):
    def __init__(self,asset,midbottom):
        pygame.sprite.Sprite.__init__(self)
        self.asset=asset
        self.launch_effects=self.asset.launch_effects
        
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