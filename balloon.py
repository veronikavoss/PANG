#%%
from setting import *
#%%
class Balloon(pygame.sprite.Sprite):
    def __init__(self,asset,color,size,pos,flip,pop,index=0,speed=3):
        pygame.sprite.Sprite.__init__(self)
        self.balloon_images=asset.balloon_images
        self.color=color
        self.size=size
        self.pos=pos
        self.flip=flip
        self.pop=pop
        self.index=index
        self.speed=speed
        self.stop=False
        self.Warning_animation=False
        
        self.image=self.balloon_images[self.color][self.size]
        self.rect=self.image.get_rect(center=self.pos)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.set_balloon_speed()
        self.gravity=0.18
    
    def set_balloon_speed(self):
        if self.flip:
            self.speed_x=self.speed
        else:
            self.speed_x=-self.speed
        
        if self.pop:
            self.dy=-3
        
        if self.size==0:
            self.speed_y=-12
        elif self.size==1:
            self.speed_y=-10
        elif self.size==2:
            self.speed_y=-8
        elif self.size==3:
            self.speed_y=-6
    
    def set_movement(self):
        if not self.stop:
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
                self.dy=self.speed_y*-1
    
    def stop_animation(self,alpha):
        if self.stop and self.Warning_animation:
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
    
    def update(self,alpha):
        self.set_movement()
        self.stop_animation(alpha)
        print(self.stop)

class Balloons_Popped_Effect(pygame.sprite.Sprite):
    def __init__(self,asset,color,size,center):
        pygame.sprite.Sprite.__init__(self)
        self.balloon_popped_images=asset.balloons_popped_images
        self.color=color
        self.size=size
        self.balloons_popped_effect_index=0
        self.balloons_popped_effect_speed=0.2
        self.get_balloons_popped_effect_image(center)
    
    def get_balloons_popped_effect_image(self,center):
        if self.size==0:
            self.animation=self.balloon_popped_images[self.color]['size1']
        elif self.size==1:
            self.animation=self.balloon_popped_images[self.color]['size2']
        elif self.size==2:
            self.animation=self.balloon_popped_images[self.color]['size3']
        elif self.size==3:
            self.animation=self.balloon_popped_images[self.color]['size4']
        
        self.image=self.animation[int(self.balloons_popped_effect_index)]
        self.rect=self.image.get_rect(center=center)
    
    def balloons_popped_effect(self):
        self.balloons_popped_effect_index+=self.balloons_popped_effect_speed
        if self.balloons_popped_effect_index>=len(self.animation)-1:
            self.kill()
        self.image=self.animation[int(self.balloons_popped_effect_index)]
    
    def update(self):
        self.balloons_popped_effect()