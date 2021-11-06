#%%
from setting import *
from asset import Asset
from weapon import *
#%%
class Player(pygame.sprite.Sprite,Asset):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        self.get_player()
        self.get_launch_effect()
        self.screen=screen
        
        self.action='standby'
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
        self.double_wire=False
        self.vulcan_missile=True
        self.launched=False
        
        self.weapon_sprite=pygame.sprite.Group()
    
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
            self.launch_effect()
            self.weapon_launch()
    
    def launch_effect(self):
        self.launch_effect_index+=self.launch_effect_animation_speed
        if self.launch_effect_index>=len(self.launch_effects):
            self.launch_effect_index=0
        self.effect_image=self.launch_effects[int(self.launch_effect_index)]
        self.effect_image_rect=self.effect_image.get_rect(midbottom=self.rect.midtop)
        return self.effect_image
    
    def weapon_launch(self):
        if self.double_wire:
            if len(self.weapon_sprite)<2:
                self.weapon_sprite.add(Weapon(self.rect.midtop))
                if len(self.weapon_sprite)==2:
                    self.launched=True
        elif self.vulcan_missile:
            self.weapon_sprite.add(Weapon(self.rect.midtop))
        else:
            if len(self.weapon_sprite)==0:
                self.weapon_sprite.add(Weapon(self.rect.midtop))
                self.launched=True
    
    def set_action(self):
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
            self.index=0
        self.image=animation[int(self.index)]
        if self.flip:
            self.image=pygame.transform.flip(self.image,True,False)
        else:
            self.image=pygame.transform.flip(self.image,False,False)
    
    def update(self):
        self.key_input()
        self.set_action()
        # self.launch_effect()
        self.animation()
    
    def draw(self):
        self.screen.blit(self.launch_effect(),self.effect_image_rect)