#%%
from setting import *
from weapon import *
#%%
class Player(pygame.sprite.Sprite):
    def __init__(self,asset):
        pygame.sprite.Sprite.__init__(self)
        self.asset=asset
        self.weapon_images=self.asset.weapon_images
        self.launch_effects=self.asset.launch_effects
        self.player_images=self.asset.player_images
        
        self.action='standby'
        self.weapon='single_wire' # single_wire,double_wire,power_wire,vulcan_missile
        self.weapon_type='normal' # normal,power_wire,vulcan_missile
        self.index=0
        self.animation_speed=0.1
        self.image=self.player_images[self.action][self.index]
        self.rect=self.image.get_rect(midbottom=(screen_width//2,stage_bottom))
        
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed_x=5
        self.speed_y=-15
        self.gravity=0.8
        
        self.flip=False
        self.Ready_for_Launch=True
        self.vulcan_missile_Ready_for_Launch=True
        self.launched=False
        self.launch_key_pressed=False
        self.die_jump=False
        self.hit_pos=True
        self.playing_game=False
        
        self.weapon_sprite=pygame.sprite.Group()
        self.launch_effect=pygame.sprite.GroupSingle()
    
    def key_input(self,playing_game):
        self.rect.x+=self.dx
        key_input=pygame.key.get_pressed()
        if playing_game and not self.action=='die':
            if key_input[pygame.K_LEFT]:
                if self.rect.left>=stage_left:
                    self.dx=-self.speed_x
                    self.flip=True
                else:
                    self.rect.left=stage_left
            elif key_input[pygame.K_RIGHT]:
                if self.rect.right<=stage_right:
                    self.dx=self.speed_x
                    self.flip=False
                else:
                    self.rect.right=stage_right
            else:
                self.dx=0
            
            if key_input[pygame.K_SPACE]:
                if self.Ready_for_Launch and not self.launch_key_pressed:
                    self.weapon_launch()
                    self.launch_effect.add(Launch_Effect(self.asset,self.rect.midtop))
                    self.launch_key_pressed=True
                    if self.weapon_type=='normal' or self.weapon_type=='power_wire':
                        self.asset.normal_launch_sound.play()
                    elif self.weapon_type=='vulcan_missile':
                        self.asset.vulcan_missile_launch_sound.play()
            else:
                self.launch_key_pressed=False
            
            if key_input[pygame.K_s]:
                self.weapon='single_wire'
            elif key_input[pygame.K_d]:
                self.weapon='double_wire'
            elif key_input[pygame.K_p]:
                self.weapon='power_wire'
            elif key_input[pygame.K_v]:
                self.weapon='vulcan_missile'
    
    def die(self):
        if self.hit_pos:
            self.dx=5
        else:
            self.dx=-5
        self.gravity=0.5
        if not self.die_jump:
            self.dy=-15
            self.die_jump=True
        elif self.rect.bottom>=stage_bottom:
            self.die_jump=False
            self.dy=-10
            self.die_jump=True
    
    def set_gravity(self):
        self.dy+=self.gravity
        self.rect.y+=self.dy
        
        if self.rect.bottom>=stage_bottom:
            self.rect.bottom=stage_bottom
    
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
    
    def weapon_launch(self):
            self.weapon_sprite.add(Weapon(self.asset,self.rect.midtop,self.weapon_type))
            self.launched=True
    
    def set_action(self):
        if not self.action=='die':
            if not self.launched:
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
            if self.action=='launch':
                self.index=0
                self.action='standby'
                self.launched=False
            elif self.action=='die':
                self.index=1
                self.die()
            else:
                self.index=0
        self.image=animation[int(self.index)]
        if self.flip:
            self.image=pygame.transform.flip(self.image,True,False)
        else:
            self.image=pygame.transform.flip(self.image,False,False)
    
    def update(self,playing_game):
        self.key_input(playing_game)
        self.set_gravity()
        self.set_action()
        self.set_weapon()
        self.animation()
        print(self.playing_game)
#%%
