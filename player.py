#%%
from setting import *
from weapon import *
#%%
class Player(pygame.sprite.Sprite):
    def __init__(self,screen,asset,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.asset=asset
        self.weapon_images=self.asset.weapon_images
        self.launch_effects=self.asset.launch_effects
        self.player_images=self.asset.player_images
        
        self.action='standby'
        self.weapon='single_wire' # single_wire,double_wire,double_power_wire,power_wire,vulcan_missile
        self.previous_weapon=''
        self.weapon_type='normal' # normal,power_wire,vulcan_missile
        self.index=0
        self.animation_speed=0.1
        self.image=self.player_images[self.action][self.index]
        # self.rect=self.image.get_rect(midbottom=(screen_width//2,stage_bottom))
        self.rect=self.image.get_rect(x=x,y=y)
        
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed_x=5
        self.speed_y=-15
        self.gravity=0.8
        
        self.flip=False
        self.launched=False
        self.launch_key_pressed=False
        self.die_jump=False
        self.hit_pos=True
        self.playing_game=False
        
        self.shield=False
        self.shield_index=0
        self.shield_crash=False
        self.shield_animation_index=0
        self.shield_status='normal'
        
        self.weapon_sprite=pygame.sprite.Group()
        self.launch_effect=pygame.sprite.GroupSingle()
    
    def key_input(self,playing_game,dt):
        self.rect.x+=self.dx*dt
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
                if not self.launch_key_pressed:
                    self.weapon_launch()
                    self.launch_key_pressed=True
            else:
                self.launch_key_pressed=False
            
            if key_input[pygame.K_s]:
                if self.shield_status=='normal':
                    self.shield_status='shield'
                elif self.shield_status=='crashed':
                    self.shield=True
            elif key_input[pygame.K_d]:
                self.weapon='double_wire'
            elif key_input[pygame.K_p]:
                self.previous_weapon=self.weapon
                if self.previous_weapon=='double_wire':
                    self.weapon='double_power_wire'
                else:
                    self.weapon='power_wire'
            elif key_input[pygame.K_v]:
                self.weapon='vulcan_missile'
            elif key_input[pygame.K_1]:
                FPS=30
            elif key_input[pygame.K_2]:
                FPS=60
            
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
    
    def set_gravity(self,dt):
        self.dy+=self.gravity
        self.rect.y+=self.dy*dt
        
        if self.rect.bottom>=stage_bottom:
            self.rect.bottom=stage_bottom
    
    def set_weapon_type(self):
        if self.weapon=='single_wire' or self.weapon=='double_wire':
            self.weapon_type='normal'
        elif self.weapon=='power_wire' or self.weapon=='double_power_wire':
            self.weapon_type='power_wire'
        elif self.weapon=='vulcan_missile':
            self.weapon_type='vulcan_missile'
    
    def weapon_launch(self):
        if self.weapon=='single_wire' or self.weapon=='power_wire':
            if len(self.weapon_sprite)==0:
                self.weapon_sprite.add(Weapon(self.asset,self.rect.midtop,self.weapon_type))
                self.launch_effect.add(Launch_Effect(self.asset,self.rect.midtop))
                self.asset.normal_launch_sound.play()
                self.launched=True
        elif self.weapon=='double_wire' or self.weapon=='double_power_wire':
            if len(self.weapon_sprite)<2:
                self.weapon_sprite.add(Weapon(self.asset,self.rect.midtop,self.weapon_type))
                self.launch_effect.add(Launch_Effect(self.asset,self.rect.midtop))
                self.asset.normal_launch_sound.play()
                self.launched=True
        else:
            self.weapon_sprite.add(Weapon(self.asset,self.rect.midtop,self.weapon_type))
            self.launch_effect.add(Launch_Effect(self.asset,self.rect.midtop))
            self.asset.vulcan_missile_launch_sound.play()
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
    
    def animation(self,dt):
        self.index+=self.animation_speed*dt
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
    
    def draw_shield(self,dt):
        shield_image=self.player_images['shield']
        
        if self.shield_status=='shield':
            self.shield_image=shield_image[int(self.shield_index)]
            
            self.shield_index+=0.1*dt
            if self.shield_index>=len(shield_image)-2:
                self.shield_index=0
            
            if not self.flip:
                self.shield_image=pygame.transform.flip(self.shield_image,False,False)
                self.shield_rect=self.shield_image.get_rect(center=(self.rect.centerx-5,self.rect.centery))
            else:
                self.shield_image=pygame.transform.flip(self.shield_image,True,False)
                self.shield_rect=self.shield_image.get_rect(center=(self.rect.centerx+5,self.rect.centery))
            
            self.screen.blit(self.shield_image,self.shield_rect)
        
        elif self.shield_status=='crashed':
            self.shield_image=shield_image[2]
            self.shield_animation_index+=0.1*dt
            self.current_time=int(self.shield_animation_index)
            if not self.flip:
                self.shield_image=pygame.transform.flip(self.shield_image,False,False)
                self.shield_rect=self.shield_image.get_rect(center=(self.rect.centerx-5,self.rect.centery))
            else:
                self.shield_image=pygame.transform.flip(self.shield_image,True,False)
                self.shield_rect=self.shield_image.get_rect(center=(self.rect.centerx+5,self.rect.centery))
                
            if self.current_time<=1:
                self.screen.blit(self.shield_image,self.shield_rect)
            
            if self.shield:
                self.shield_image=shield_image[0]
                self.screen.blit(self.shield_image,self.shield_rect)
            
            if self.current_time%2==0:
                self.image.set_alpha(255)
                self.shield_image.set_alpha(255)
            else:
                self.image.set_alpha(0)
                self.shield_image.set_alpha(0)
                
            if self.current_time>=20:
                if self.shield:
                    self.shield_status='shield'
                    self.shield_animation_index=0
                else:
                    self.shield_status='normal'
                    self.shield=False
        else:
            self.shield_status='normal'
            self.shield_animation_index=0
    
    def update(self,playing_game,dt):
        self.key_input(playing_game,dt)
        self.set_gravity(dt)
        self.set_action()
        self.set_weapon_type()
        self.animation(dt)