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
    
    def get_balloons(self):
        self.balloon_images={
            'red':[],
            'blue':[],
            'green':[]
        }
        br_pos=[[1,6,48,40],[52,13,32,26],[86,19,16,14],[106,23,8,7]]
        bb_pos=[[1,56,48,40],[52,63,32,26],[86,69,16,14],[106,73,8,7]]
        bg_pos=[[1,105,48,40],[52,112,32,26],[86,118,16,14],[106,112,8,7]]
        for br in br_pos:
            r=pygame.Surface((br[2],br[3]))
            r.blit(self.balloons_sheet,(0,0),br)
            r.set_colorkey((128,64,0))
            r=pygame.transform.scale(r,(br[2]*3,br[3]*3))
            self.balloon_images['red'].append(r)