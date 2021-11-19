#%%
from setting import *
from random import *
#%%
class Item_and_Food(pygame.sprite.Sprite):
    def __init__(self,asset,center):
        pygame.sprite.Sprite.__init__(self)
        self.asset=asset
        self.items_images=self.asset.items_images
        self.weapon_power_wire_items=self.items_images['weapon_items']['power_wire']
        self.weapon_double_wire_items=self.items_images['weapon_items']['double_wire']
        self.weapon_vulcan_missile_items=self.items_images['weapon_items']['vulcan_missile']
        self.clock_stop_items=self.items_images['clock_items']['stop']
        self.clock_slow_items=self.items_images['clock_items']['slow']
        self.dynamite_items=self.items_images['dynamite_items'][0]
        self.bonus_items=self.items_images['bonus_items']['bonus']
        self.shield_items=self.items_images['shield_items'][0]
        self.items=[
            self.weapon_power_wire_items,
            self.weapon_double_wire_items,
            self.weapon_vulcan_missile_items,
            self.clock_stop_items,
            self.clock_slow_items,
            self.dynamite_items,
            self.bonus_items,
            self.shield_items
            ]
        self.item=choice(self.items)
        self.animation_index=0
        self.image=self.item
        self.rect=self.image.get_rect(center=center)
        
    
    def animation(self):
        if self.item==self.dynamite_items or self.item==self.shield_items:
            if self.item==self.dynamite_items:
                self.animation_index+=0.1
                item=self.items_images['dynamite_items']
                if self.animation_index>=len(item):
                    self.animation_index=0
            elif self.item==self.shield_items:
                self.animation_index+=0.1
                item=self.items_images['shield_items']
                if self.animation_index>=len(item):
                    self.animation_index=0
            self.image=item[int(self.animation_index)]
        else:
            self.image=self.item
    
    def update(self):
        self.rect.y+=5
        if self.rect.bottom>=stage_bottom:
            self.rect.bottom=stage_bottom
        self.animation()
        print(self.rect.centery)
#%%
# import pygame
# weapon_items_pos=[[8,62,15,16],[47,62,15,16],[86,65,16,13]]
# clock_items_pos=[[8,102,16,16],[48,102,16,16]]
# dynamite_items_pos=[[88,105,15,13],[111,102,16,16],[135,102,16,16]]
# bonus_items_pos=[[8,142,16,16],[48,142,16,16],[72,142,16,16],[96,142,16,16],[120,142,16,16]]
# shield_items_pos=[[8,372,10,8],[26,368,14,12],[48,366,16,14],[72,366,16,14],[96,366,16,14],[120,366,16,14],[144,366,16,14],[168,368,14,12]]
# items_pos_list=[weapon_items_pos,clock_items_pos,dynamite_items_pos,bonus_items_pos,shield_items_pos]
# item_surface_temp=[]
# for i in range(5):
#     for item in items_pos_list[i]:
#         surface=pygame.Surface((item[2],item[3]))
#         item_surface_temp.append(surface)
# #%%
# print(item_surface_temp[0])
# #%%
