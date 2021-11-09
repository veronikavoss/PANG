#%%
from setting import *
from asset import Asset
#%%
class Balloon(pygame.sprite.Sprite,Asset):
    def __init__(self,level,weapons):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        self.level=level
        self.weapons=weapons
        self.get_balloons()
        self.color='red'
        self.index=0
        self.image=self.balloon_images[self.color][self.index]
        self.rect=self.image.get_rect(topleft=(80,60))
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed_x=3
        self.speed_y=-12
        self.gravity=0.18
    
    def levels(self):
        pass
    
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