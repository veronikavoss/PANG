#%%
from setting import *
#%%
class Asset:
    def __init__(self):
        self.background_sheet=pygame.image.load(os.path.join(image_path,'Backgrounds.png')).convert_alpha()
        self.foreground_sheet=pygame.image.load(os.path.join(image_path,'Foreground.png')).convert_alpha()
        self.player_sheet=pygame.image.load(os.path.join(image_path,'player.png')).convert_alpha()
        self.items_weapons_sheet=pygame.image.load(os.path.join(image_path,'Items & Weapons.png')).convert_alpha()
        self.balloons_sheet=pygame.image.load(os.path.join(image_path,'Balloons.png')).convert_alpha()
        self.animals_sheet=pygame.image.load(os.path.join(image_path,'Animals.png')).convert_alpha()
        self.food_sheet=pygame.image.load(os.path.join(image_path,'Food.png')).convert_alpha()
    
    def get_background(self):
        self.background_images=[]
        for i in range(25):
            for j in range(2):
                bg=pygame.Surface((384,208))
                bg.blit(self.background_sheet,(0,0),(8+j*392,8+i*216,384,208))
                bg.set_colorkey((186,254,202))
                bg=pygame.transform.scale(bg,screen_size)
                self.background_images.append(bg)
    
    def get_foreground(self):
        self.foreground_images=[]
        for i in range(25):
            for j in range(2):
                fg=pygame.Surface((384,208))
                fg.blit(self.foreground_sheet,(0,0),(8+j*392,44+i*216,384,208))
                fg.set_colorkey((145,129,137))
                fg=pygame.transform.scale(fg,screen_size)
                self.foreground_images.append(fg)
    
    def get_player(self):
        self.player_images={
            'move_x':[],
            'move_y':[],
            'launch':[],
            'standby':[],
        }
        for column in range(5):
            mx=pygame.Surface((32,32))
            mx.blit(self.player_sheet,(0,0),(10+column*34,2,32,32))
            mx.set_colorkey((0,255,0))
            mx=pygame.transform.scale(mx,(player_width,player_height))
            self.player_images['move_x'].append(mx)
        
        for row in range(2):
            for column in range(4):
                my=pygame.Surface((32,32))
                my.blit(self.player_sheet,(0,0),(10+column*34,36+row*41,32,32))
                my.set_colorkey((0,255,0))
                my=pygame.transform.scale(my,(player_width,player_height))
                self.player_images['move_y'].append(my)
        
        for column in range(2):
            launch=pygame.Surface((32,32))
            launch.blit(self.player_sheet,(0,0),(10+column*34,112,32,32))
            launch.set_colorkey((0,255,0))
            launch=pygame.transform.scale(launch,(player_width,player_height))
            self.player_images['launch'].append(launch)
        
        self.player_images['standby'].append(self.player_images['launch'][0])
    
    def get_weapon(self):
        self.weapon_images={
            'normal':[],
            'power_wire':[],
            'vulcan_missile':[]
        }
        weapon1=pygame.Surface((9,189))
        weapon1.blit(self.items_weapons_sheet,(0,0),(399,1568,9,189))
        weapon1.set_colorkey((103,150,86))
        weapon1=pygame.transform.scale(weapon1,(9*3,189*3))
        weapon1_flip=pygame.Surface.copy(weapon1)
        weapon1_flip=pygame.transform.flip(weapon1_flip,True,False)
        self.weapon_images['normal'].append(weapon1)
        self.weapon_images['normal'].append(weapon1_flip)
        
        weapon2=pygame.Surface((9,191))
        weapon2.blit(self.items_weapons_sheet,(0,0),(382,1101,9,191))
        weapon2.set_colorkey((103,150,86))
        weapon2=pygame.transform.scale(weapon2,(9*3,191*3))
        weapon2_flip=pygame.Surface.copy(weapon2)
        weapon2_flip=pygame.transform.flip(weapon2_flip,True,False)
        weapon2_stop=pygame.Surface((9,191))
        weapon2_stop.blit(self.items_weapons_sheet,(0,0),(399,1101,9,191))
        weapon2_stop.set_colorkey((103,150,86))
        weapon2_stop=pygame.transform.scale(weapon2_stop,(9*3,191*3))
        self.weapon_images['power_wire'].append(weapon2)
        self.weapon_images['power_wire'].append(weapon2_flip)
        self.weapon_images['power_wire'].append(weapon2_stop)
        
        weapon3=[[94,261,16,9],[108,261,16,9],[126,261,16,9],[148,261,16,9],[171,261,16,9],[191,261,16,9],[211,261,16,9]]
        for weapon in weapon3:
            w3=pygame.Surface((16,9))
            w3.blit(self.items_weapons_sheet,(0,0),weapon)
            w3.set_colorkey((103,150,86))
            w3=pygame.transform.scale(w3,(16*3,9*3))
            self.weapon_images['vulcan_missile'].append(w3)
    
    def get_launch_effect(self):
        self.launch_effects=[]
        effect_list=[[3,256,16,14],[17,256,16,14],[36,256,16,14],[60,256,16,14]]
        for effect in effect_list:
            le=pygame.Surface((16,14))
            le.blit(self.items_weapons_sheet,(0,0),effect)
            le.set_colorkey((103,150,86))
            le=pygame.transform.scale(le,(16*3,14*3))
            self.launch_effects.append(le)