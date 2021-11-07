#%%
from setting import *
from asset import Asset
from weapon import *
#%%
class Player(pygame.sprite.Sprite,Asset):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        self.get_player()
        self.get_launch_effect()
        
        self.action='standby'
        self.weapon_type='normal'
        self.index=0
        self.image=self.player_images[self.action][self.index]
        self.rect=self.image.get_rect(midbottom=(screen_width//2,stage_bottom))
        
        self.launch_effect_index=0
        self.launch_effect_animation_speed=0.1
        
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed=5
        self.animation_speed=0.1
        
        self.flip=False
        self.pressed=False
        self.launched=False
        
        self.weapon_sprite=pygame.sprite.Group()
        self.launch_effect=pygame.sprite.GroupSingle()
    
    def key_input(self):
        self.rect.x+=self.dx
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            if self.rect.left>=stage_left:
                self.dx=-self.speed
                self.flip=True
            else:
                self.rect.left=stage_left
        elif key_input[pygame.K_RIGHT]:
            if self.rect.right<=stage_right:
                self.dx=self.speed
                self.flip=False
            else:
                self.rect.right=stage_right
        else:
            self.dx=0
        
        if key_input[pygame.K_SPACE] and not self.pressed:
            self.pressed=True
            self.launch_effect.add(Launch_Effect(self.rect.midtop))
            self.weapon_launch()
            self.pressed=False
    
    def weapon_launch(self):
        if self.weapon_type=='double_wire':
            if len(self.weapon_sprite)<2:
                self.weapon_sprite.add(Weapon(self.rect.midtop,self.weapon_type))
                if len(self.weapon_sprite)==2:
                    self.launched=True
        elif self.weapon_type=='vulcan_missile':
            self.weapon_sprite.add(Weapon(self.rect.midtop,self.weapon_type))
        else:
            if len(self.weapon_sprite)==0:
                self.weapon_sprite.add(Weapon(self.rect.midtop,self.weapon_type))
                self.launched=True
    
    def set_action(self):
        if not self.pressed:
            if self.dx!=0:
                self.action='move_x'
                self.animation_speed=0.2
            else:
                self.action='standby'
        else:
            self.action='launch'
    
    def animation(self):
        self.index+=self.animation_speed
        animation=self.player_images[self.action]
        if self.index>=len(animation):
            self.index=0
        self.image=animation[int(self.index)]
        if self.flip:
            self.image=pygame.transform.flip(self.image,True,False)
        else:
            self.image=pygame.transform.flip(self.image,False,False)
    
    def update(self):
        self.key_input()
        self.set_action()
        self.animation()