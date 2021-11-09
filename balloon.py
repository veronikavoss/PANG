#%%
from setting import *
from asset import Asset
from level import Level
#%%
class Balloon(pygame.sprite.Sprite,Asset,Level):
    def __init__(self,weapons):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        Level.__init__(self)
        self.weapons=weapons
        self.get_balloons()
        self.balloon_level()
        
        self.image=self.balloon_images[self.color][self.size]
        self.rect=self.image.get_rect(topleft=self.pos)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed_x=3
        self.set_balloon_speed()
        self.gravity=0.18
    
    def set_balloon_speed(self):
        if self.size==0:
            self.speed_y=-12
        elif self.size==1:
            self.speed_y=-9
        elif self.size==2:
            self.speed_y=-6
        elif self.size==3:
            self.speed_y=-3
    
    def set_movement(self):
        self.dx=self.speed_x
        self.rect.x+=self.dx
        self.dy+=self.gravity
        self.rect.y+=self.dy
        
        if self.rect.right>=stage_right:
            self.rect.right=stage_right
            self.speed_x=self.speed_x*-1
        elif self.rect.left<=stage_left:
            self.rect.left=stage_left
            self.speed_x=self.speed_x*-1
        
        if self.rect.bottom>=stage_bottom:
            self.rect.bottom=stage_bottom
            self.dy=self.speed_y
        elif self.rect.top<=stage_top:
            self.rect.top=stage_top
            self.dy=self.dy*-1
    
    def collision(self):
        for weapon in self.weapons:
            if pygame.sprite.collide_mask(self,weapon):
                self.kill()
                weapon.kill()
    
    def update(self):
        self.set_movement()
        self.collision()