#%%
from setting import *
#%%
class Weapon(pygame.sprite.Sprite):
    def __init__(self,midtop,weapon_type):
        pygame.sprite.Sprite.__init__(self)
        self.weapon_type=weapon_type
        self.get_weapons()
        self.index=0
        self.image=self.weapon_images[self.weapon_type][self.index]
        self.init_weapon_position()
        self.image.set_colorkey((103,150,86))
        self.rect=self.image.get_rect(midtop=midtop)
        self.animation_speed=0.1
        self.flip=False
    
    def init_weapon_position(self):
        if self.weapon_type=='normal':
            self.image=pygame.transform.scale(self.image,(9*3,189*3))
        elif self.weapon_type=='power_wire':
            self.image=pygame.transform.scale(self.image,(9*3,191*3))
        elif self.weapon_type=='vulcan_missile':
            self.image=pygame.transform.scale(self.image,(16*3,9*3))
    
    def get_weapons(self):
        self.weapon_images={
            'normal':[],
            'power_wire':[],
            'vulcan_missile':[]
        }
        for i in range(1,3):
            self.weapon_images['normal'].append(pygame.image.load(os.path.join(weapon_path,f'normal_{i}.png')).convert_alpha())
        for i in range(1,4):
            self.weapon_images['power_wire'].append(pygame.image.load(os.path.join(weapon_path,f'power_wire_{i}.png')).convert_alpha())
        for i in range(1,8):
            self.weapon_images['vulcan_missile'].append(pygame.image.load(os.path.join(weapon_path,f'vulcan_missile_{i}.png')).convert_alpha())
    
    def collision(self):
        self.rect.y-=8
    
    def animation(self):
        animation=self.weapon_images[self.weapon_type]
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
        if self.weapon_type=='normal':
            self.image=pygame.transform.scale(self.image,(9*3,189*3))
        elif self.weapon_type=='power_wire':
            self.image=pygame.transform.scale(self.image,(9*3,191*3))
        elif self.weapon_type=='vulcan_missile':
            self.image=pygame.transform.scale(self.image,(16*3,9*3))
        self.image.set_colorkey((103,150,86))
    
    def update(self):
        self.collision()
        self.animation()

class Launch_Effect(pygame.sprite.Sprite):
    def __init__(self,midbottom):
        pygame.sprite.Sprite.__init__(self)
        self.launch_effects=[]
        for i in range(1,5):
            self.launch_effects.append(pygame.image.load(os.path.join(weapon_path,f'launch_effect_{i}.png')).convert_alpha())
        self.index=0
        self.image=self.launch_effects[self.index]
        self.image=pygame.transform.scale(self.image,(16*3,14*3))
        self.image.set_colorkey((103,150,86))
        self.rect=self.image.get_rect(midbottom=midbottom)
        self.animation_speed=0.2
    
    def animation(self):
        self.index+=self.animation_speed
        animation=self.launch_effects
        if self.index>=len(animation)-1:
            self.kill()
        self.image=animation[int(self.index)]
        self.image=pygame.transform.scale(self.image,(16*3,14*3))
        self.image.set_colorkey((103,150,86))
    
    def update(self):
        self.animation()