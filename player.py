#%%
from setting import *
from asset import Asset
from level import Level
from weapon import *
from balloon import Balloon
#%%
class Player(pygame.sprite.Sprite,Asset,Level):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        Level.__init__(self)
        self.get_player()
        
        self.action='standby'
        self.weapon='single_wire' # single_wire,double_wire,power_wire,vulcan_missile
        self.weapon_type='' # normal,power_wire,vulcan_missile
        self.index=0
        self.image=self.player_images[self.action][self.index]
        self.rect=self.image.get_rect(midbottom=(screen_width//2,stage_bottom))
        
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed=5
        self.animation_speed=0.1
        
        self.flip=False
        self.Ready_for_Launch=True
        self.vulcan_missile_Ready_for_Launch=True
        self.launched=False
        self.k_space_pressed=False
        
        self.weapon_sprite=pygame.sprite.Group()
        self.launch_effect=pygame.sprite.GroupSingle()
        self.balloons=pygame.sprite.Group(Balloon(self.weapon_sprite))
    
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
        
        if key_input[pygame.K_SPACE]:
            if self.Ready_for_Launch and not self.k_space_pressed:
                self.weapon_launch()
                self.launch_effect.add(Launch_Effect(self.rect.midtop))
                self.k_space_pressed=True
        else:
            self.k_space_pressed=False
        
        if key_input[pygame.K_s]:
            self.weapon='single_wire'
        elif key_input[pygame.K_d]:
            self.weapon='double_wire'
        elif key_input[pygame.K_p]:
            self.weapon='power_wire'
        elif key_input[pygame.K_v]:
            self.weapon='vulcan_missile'
    
    def weapon_launch(self):
            self.weapon_sprite.add(Weapon(self.rect.midtop,self.weapon_type))
            self.launched=True
    
    def collision(self):
        for balloon in self.balloons:
            if pygame.sprite.collide_mask(self,balloon):
                print('c')
    
    def set_action(self):
        if not self.launched:
            if self.dx!=0:
                self.action='move_x'
                self.animation_speed=0.2
            else:
                self.action='standby'
        else:
            self.action='launch'
    
    def set_weapon(self):
        if self.weapon=='single_wire' or self.weapon=='double_wire':
            self.weapon_type='normal'
        elif self.weapon=='power_wire':
            self.weapon_type='power_wire'
        elif self.weapon=='vulcan_missile':
            self.weapon_type='vulcan_missile'
        
        if self.weapon=='single_wire' or self.weapon=='power_wire':
            if len(self.weapon_sprite)==0:
                self.Ready_for_Launch=True
            else:
                self.Ready_for_Launch=False
        elif self.weapon=='double_wire':
            if len(self.weapon_sprite)>=2:
                self.Ready_for_Launch=False
            else:
                self.Ready_for_Launch=True
    
    def animation(self):
        self.index+=self.animation_speed
        animation=self.player_images[self.action]
        if self.index>=len(animation):
            if self.action=='launch':
                self.index=0
                self.action='standby'
                self.launched=False
            else:
                self.index=0
        self.image=animation[int(self.index)]
        if self.flip:
            self.image=pygame.transform.flip(self.image,True,False)
        else:
            self.image=pygame.transform.flip(self.image,False,False)
    
    def update(self):
        self.key_input()
        self.collision()
        self.set_action()
        self.set_weapon()
        self.animation()
        