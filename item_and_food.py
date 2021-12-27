#%%
from setting import *
#%%
class Item_and_Food(pygame.sprite.Sprite):
    def __init__(self,asset,center):
        pygame.sprite.Sprite.__init__(self)
        self.asset=asset
        self.animation_index=0
        self.item_type=''
        self.item=''
        self.get_item_images()
        self.set_items()
        self.image=self.item_image
        self.rect=self.image.get_rect(center=center)
        self.update_timer=pygame.time.get_ticks()
    
    def get_item_images(self):
        self.items_images=self.asset.items_images
        self.weapon_power_wire_item=self.items_images['weapon_items']['power_wire']
        self.weapon_double_wire_item=self.items_images['weapon_items']['double_wire']
        self.weapon_vulcan_missile_item=self.items_images['weapon_items']['vulcan_missile']
        self.clock_stop_item=self.items_images['clock_items']['stop']
        self.clock_slow_item=self.items_images['clock_items']['slow']
        self.dynamite_item=self.items_images['dynamite_item'][self.animation_index]
        self.shield_item=self.items_images['shield_item'][self.animation_index]
        self.bonus_item=self.items_images['bonus_items']['bonus']
    
    def set_items(self):
        self.items=[
            self.weapon_power_wire_item,
            self.weapon_double_wire_item,
            self.weapon_vulcan_missile_item,
            self.clock_stop_item,
            self.clock_slow_item,
            self.dynamite_item,
            self.shield_item,
            # self.bonus_items
            ]
        self.item_image=choice(self.items)
        if self.item_image==self.weapon_power_wire_item:
            self.item_type='weapon_items'
            self.item='power_wire'
        elif self.item_image==self.weapon_double_wire_item:
            self.item_type='weapon_items'
            self.item='double_wire'
        elif self.item_image==self.weapon_vulcan_missile_item:
            self.item_type='weapon_items'
            self.item='vulcan_missile'
        elif self.item_image==self.clock_stop_item:
            self.item_type='clock_items'
            self.item='stop'
        elif self.item_image==self.clock_slow_item:
            self.item_type='clock_items'
            self.item='slow'
        elif self.item_image==self.dynamite_item:
            self.item_type='dynamite_item'
            self.item='dynamite'
        elif self.item_image==self.shield_item:
            self.item_type='shield_item'
            self.item='shield'
        elif self.item_image==self.bonus_item:
            self.item_type='bonus_items'
            self.item='bonus'
    
    def animation(self,current_time,ms,dt):
        self.rect.y+=5*dt
        
        if self.item_image==self.dynamite_item or self.item_image==self.shield_item:
            if self.item_image==self.dynamite_item:
                self.animation_index+=0.1*dt
                item=self.items_images['dynamite_item']
                if self.animation_index>=len(item):
                    self.animation_index=0
            elif self.item_image==self.shield_item:
                self.animation_index+=0.1*dt
                item=self.items_images['shield_item']
                if self.animation_index>=len(item):
                    self.animation_index=0
            self.image=item[int(self.animation_index)]
        else:
            self.image=self.item_image
        
        if self.rect.bottom>=stage_bottom:
            self.rect.bottom=stage_bottom
            if current_time-self.update_timer>=5000:
                self.image.set_alpha(ms)
            if current_time-self.update_timer>=7000:
                self.image.set_alpha(255)
                self.kill()
        
        print(current_time-self.update_timer)
    
    def update(self,current_time,ms,dt):
        self.animation(current_time,ms,dt)
#%%
