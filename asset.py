#%%
from setting import *
#%%
class Asset:
    def __init__(self):
        self.background_sheet=pygame.image.load(os.path.join(image_path,'Backgrounds.png')).convert_alpha()
        self.foreground_sheet=pygame.image.load(os.path.join(image_path,'Foreground.png')).convert_alpha()
        self.player_sheet=pygame.image.load(os.path.join(image_path,'player.png')).convert_alpha()
        self.crash_shield_sheet=pygame.image.load(os.path.join(image_path,'shield_crash.png')).convert_alpha()
        self.items_weapons_sheet=pygame.image.load(os.path.join(image_path,'Items & Weapons.png')).convert_alpha()
        self.balloons_sheet=pygame.image.load(os.path.join(image_path,'Balloons.png')).convert_alpha()
        self.balloon_popped_red_sheet=pygame.image.load(os.path.join(image_path,'balloon_popped_red.png')).convert_alpha()
        self.balloon_popped_blue_sheet=pygame.image.load(os.path.join(image_path,'balloon_popped_blue.png')).convert_alpha()
        self.balloon_popped_green_sheet=pygame.image.load(os.path.join(image_path,'balloon_popped_green.png')).convert_alpha()
        self.animals_sheet=pygame.image.load(os.path.join(image_path,'Animals.png')).convert_alpha()
        self.food_sheet=pygame.image.load(os.path.join(image_path,'Food.png')).convert_alpha()
        self.game_status_signal_sheet=pygame.image.load(os.path.join(image_path,'blueText.png')).convert_alpha()
        self.ui()
        self.get_background()
        self.get_foreground()
        self.get_weapons()
        self.get_launch_effect()
        self.get_player()
        self.get_balloons()
        self.get_balloons_popped()
        self.get_items()
        self.get_sound()
        self.get_font()
    
    def ui(self):
        # title
        self.PANG=[]
        for i in range(1,5):
            pang=pygame.image.load(os.path.join(image_path,f'ui/PANG_{i}.png')).convert_alpha()
            pang.set_colorkey((17,17,17))
            pang=pygame.transform.scale(pang,(screen_width,screen_height))
            self.PANG.append(pang)
        
        self.pang_logo=pygame.image.load(os.path.join(image_path,'ui/PangTitleCard.png')).convert_alpha()
        self.pang_logo=pygame.transform.scale(self.pang_logo,(screen_width,screen_height))
        
        # game_status_signal
        game_status_signal=[]
        game_status_signal_pos=[[5,5,533,59],[5,69,533,59],[5,132,204,68]]
        for status in game_status_signal_pos:
            surface=pygame.Surface((status[2],status[3]))
            surface.blit(self.game_status_signal_sheet,(0,0),status)
            surface.set_colorkey((0,0,0))
            game_status_signal.append(surface)
        
        self.game_status_signal={
            'ready':game_status_signal[2],
            'time_over':game_status_signal[1],
            'game_over':game_status_signal[0]
        }
    
    def get_background(self):
        self.background_images=[]
        for i in range(25):
            for j in range(2):
                bg=pygame.Surface((384,208))
                bg.blit(self.background_sheet,(0,0),(8+j*392,8+i*216,384,208))
                bg.set_colorkey((186,254,202))
                bg=pygame.transform.scale(bg,stage_size)
                self.background_images.append(bg)
    
    def get_foreground(self):
        self.foreground_images=[]
        for i in range(25):
            for j in range(2):
                fg=pygame.Surface((384,208))
                fg.blit(self.foreground_sheet,(0,0),(8+j*392,44+i*216,384,208))
                fg.set_colorkey((145,129,137))
                fg=pygame.transform.scale(fg,stage_size)
                self.foreground_images.append(fg)
    
    def get_weapons(self):
        self.weapon_images={
        'normal':[],
        'power_wire':[],
        'vulcan_missile':[]
        }
        
        # normal
        weapon1=pygame.Surface((9,189))
        weapon1.blit(self.items_weapons_sheet,(0,0),(399,1568,9,189))
        weapon1.set_colorkey((103,150,86))
        weapon1=pygame.transform.scale(weapon1,(9*scale,189*scale))
        weapon1_flip=pygame.Surface.copy(weapon1)
        weapon1_flip=pygame.transform.flip(weapon1_flip,True,False)
        self.weapon_images['normal'].append(weapon1)
        self.weapon_images['normal'].append(weapon1_flip)
        
        # power_wire
        weapon2=pygame.Surface((9,191))
        weapon2.blit(self.items_weapons_sheet,(0,0),(382,1101,9,191))
        weapon2.set_colorkey((103,150,86))
        weapon2=pygame.transform.scale(weapon2,(9*scale,191*scale))
        weapon2_flip=pygame.Surface.copy(weapon2)
        weapon2_flip=pygame.transform.flip(weapon2_flip,True,False)
        self.weapon_images['power_wire'].append(weapon2)
        self.weapon_images['power_wire'].append(weapon2_flip)
        weapon2_stop_list=[[365,308,9,191],[382,308,9,191],[399,308,9,191]]
        for weapon in weapon2_stop_list:
            weapon2_stop=pygame.Surface((9,191))
            weapon2_stop.blit(self.items_weapons_sheet,(0,0),weapon)
            weapon2_stop.set_colorkey((103,150,86))
            weapon2_stop=pygame.transform.scale(weapon2_stop,(9*scale,191*scale))
            self.weapon_images['power_wire'].append(weapon2_stop)
        
        # vulcan_missile
        weapon3=[[94,261,16,9],[108,261,16,9],[126,261,16,9],[148,261,16,9],[171,261,16,9],[191,261,16,9],[211,261,16,9]]
        for weapon in weapon3:
            w3=pygame.Surface((16,9))
            w3.blit(self.items_weapons_sheet,(0,0),weapon)
            w3.set_colorkey((103,150,86))
            w3=pygame.transform.scale(w3,(16*scale,9*scale))
            self.weapon_images['vulcan_missile'].append(w3)
    
    def get_launch_effect(self):
        self.launch_effects=[]
        effect_list=[[3,256,16,14],[17,256,16,14],[36,256,16,14],[60,256,16,14]]
        for effect in effect_list:
            le=pygame.Surface((16,14))
            le.blit(self.items_weapons_sheet,(0,0),effect)
            le.set_colorkey((103,150,86))
            le=pygame.transform.scale(le,(16*scale,14*scale))
            self.launch_effects.append(le)
    
    def get_player(self):
        self.player_images={
            'move_x':[],
            'move_y':[],
            'launch':[],
            'standby':[],
            'die':[],
            'shield':[]
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
        
        die_list=[[147,80,32,30],[81,112,41,30]]
        for die in die_list:
            surface=pygame.Surface((die[2],die[3]))
            surface.blit(self.player_sheet,(0,0),die)
            surface.set_colorkey((0,255,0))
            surface=pygame.transform.scale(surface,(die[2]*scale,die[3]*scale))
            self.player_images['die'].append(surface)
        
        shield_list=[[64,404,32,39],[104,404,32,39]]
        for shield in shield_list:
            surface=pygame.Surface((shield[2],shield[3]))
            surface.blit(self.items_weapons_sheet,(0,0),shield)
            surface.set_colorkey((103,150,86))
            surface=pygame.transform.scale(surface,(shield[2]*scale,shield[3]*scale))
            self.player_images['shield'].append(surface)
        for i in range(2):
            surface=pygame.Surface((32,39))
            surface.blit(self.crash_shield_sheet,(0,0),(i*40,0,32,39))
            surface.set_colorkey((0,0,0))
            surface=pygame.transform.scale(surface,(32*scale,39*scale))
            self.player_images['shield'].append(surface)
    
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
            r=pygame.transform.scale(r,(br[2]*scale,br[3]*scale))
            self.balloon_images['red'].append(r)
        for bb in bb_pos:
            b=pygame.Surface((bb[2],bb[3]))
            b.blit(self.balloons_sheet,(0,0),bb)
            b.set_colorkey((128,64,0))
            b=pygame.transform.scale(b,(bb[2]*scale,bb[3]*scale))
            self.balloon_images['blue'].append(b)
        for bg in bg_pos:
            g=pygame.Surface((bg[2],bg[3]))
            g.blit(self.balloons_sheet,(0,0),bg)
            g.set_colorkey((128,64,0))
            g=pygame.transform.scale(g,(bg[2]*scale,bg[3]*scale))
            self.balloon_images['green'].append(g)
    
    def get_balloons_popped(self):
        self.balloons_popped_images={
            'red':{
                'size1':[],
                'size2':[],
                'size3':[],
                'size4':[]},
            'blue':{
                'size1':[],
                'size2':[],
                'size3':[],
                'size4':[]},
            'green':{
                'size1':[],
                'size2':[],
                'size3':[],
                'size4':[]}
        }
        size_1=[[8,143,48,39],[64,149,28,25],[100,144,41,37],[149,138,48,46]]
        size_2=[[8,86,32,26],[48,89,20,15],[76,86,27,26],[111,84,32,30]]
        size_3=[[8,45,16,14],[32,48,9,8],[49,44,15,15],[72,44,16,16]]
        size_4=[[8,13,5,5],[21,13,7,6],[36,12,10,8]]
        
        for effect in size_1:
            bpr=pygame.Surface((effect[2],effect[3]))
            bpr.blit(self.balloon_popped_red_sheet,(0,0),effect)
            bpr.set_colorkey((0,0,0))
            bpr=pygame.transform.scale(bpr,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['red']['size1'].append(bpr)
            
            bpb=pygame.Surface((effect[2],effect[3]))
            bpb.blit(self.balloon_popped_blue_sheet,(0,0),effect)
            bpb.set_colorkey((0,0,0))
            bpb=pygame.transform.scale(bpb,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['blue']['size1'].append(bpb)
            
            bpg=pygame.Surface((effect[2],effect[3]))
            bpg.blit(self.balloon_popped_green_sheet,(0,0),effect)
            bpg.set_colorkey((0,0,0))
            bpg=pygame.transform.scale(bpg,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['green']['size1'].append(bpg)
        
        for effect in size_2:
            bpr=pygame.Surface((effect[2],effect[3]))
            bpr.blit(self.balloon_popped_red_sheet,(0,0),effect)
            bpr.set_colorkey((0,0,0))
            bpr=pygame.transform.scale(bpr,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['red']['size2'].append(bpr)
            
            bpb=pygame.Surface((effect[2],effect[3]))
            bpb.blit(self.balloon_popped_blue_sheet,(0,0),effect)
            bpb.set_colorkey((0,0,0))
            bpb=pygame.transform.scale(bpb,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['blue']['size2'].append(bpb)
            
            bpg=pygame.Surface((effect[2],effect[3]))
            bpg.blit(self.balloon_popped_green_sheet,(0,0),effect)
            bpg.set_colorkey((0,0,0))
            bpg=pygame.transform.scale(bpg,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['green']['size2'].append(bpg)
        
        for effect in size_3:
            bpr=pygame.Surface((effect[2],effect[3]))
            bpr.blit(self.balloon_popped_red_sheet,(0,0),effect)
            bpr.set_colorkey((0,0,0))
            bpr=pygame.transform.scale(bpr,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['red']['size3'].append(bpr)
            
            bpb=pygame.Surface((effect[2],effect[3]))
            bpb.blit(self.balloon_popped_blue_sheet,(0,0),effect)
            bpb.set_colorkey((0,0,0))
            bpb=pygame.transform.scale(bpb,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['blue']['size3'].append(bpb)
            
            bpg=pygame.Surface((effect[2],effect[3]))
            bpg.blit(self.balloon_popped_green_sheet,(0,0),effect)
            bpg.set_colorkey((0,0,0))
            bpg=pygame.transform.scale(bpg,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['green']['size3'].append(bpg)
        
        for effect in size_4:
            bpr=pygame.Surface((effect[2],effect[3]))
            bpr.blit(self.balloon_popped_red_sheet,(0,0),effect)
            bpr.set_colorkey((0,0,0))
            bpr=pygame.transform.scale(bpr,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['red']['size4'].append(bpr)
            
            bpb=pygame.Surface((effect[2],effect[3]))
            bpb.blit(self.balloon_popped_blue_sheet,(0,0),effect)
            bpb.set_colorkey((0,0,0))
            bpb=pygame.transform.scale(bpb,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['blue']['size4'].append(bpb)
            
            bpg=pygame.Surface((effect[2],effect[3]))
            bpg.blit(self.balloon_popped_green_sheet,(0,0),effect)
            bpg.set_colorkey((0,0,0))
            bpg=pygame.transform.scale(bpg,(effect[2]*scale,effect[3]*scale))
            self.balloons_popped_images['green']['size4'].append(bpg)
    
    def get_items(self):
        weapon_items_pos=[[8,62,15,16],[47,62,15,16],[86,65,16,13]]
        clock_items_pos=[[8,102,16,16],[48,102,16,16]]
        dynamite_items_pos=[[88,102,16,16],[111,102,16,16],[135,102,16,16]]
        bonus_items_pos=[[8,142,16,16],[48,142,16,16],[72,142,16,16],[96,142,16,16],[120,142,16,16]]
        shield_items_pos=[[5,366,16,14],[25,366,16,14],[48,366,16,14],[72,366,16,14],[96,366,16,14],[120,366,16,14],[144,366,16,14],[167,366,16,14]]
        items_pos_list=[weapon_items_pos,clock_items_pos,dynamite_items_pos,bonus_items_pos,shield_items_pos]
        item_surface_temp=[]
        for i in range(5):
            for item in items_pos_list[i]:
                surface=pygame.Surface((item[2],item[3]))
                surface.blit(self.items_weapons_sheet,(0,0),item)
                surface.set_colorkey((103,150,86))
                surface=pygame.transform.scale(surface,(item[2]*scale,item[3]*scale))
                item_surface_temp.append(surface)
        
        self.items_images={
            'weapon_items':{'power_wire':item_surface_temp[0],'double_wire':item_surface_temp[1],'vulcan_missile':item_surface_temp[2]},
            # 'weapon_items':item_surface_temp[0:3],
            'clock_items':{'stop':item_surface_temp[3],'slow':item_surface_temp[4]},
            'dynamite_item':item_surface_temp[5:7],
            'bonus_items':{'bonus':item_surface_temp[8],'robot':item_surface_temp[9:12]},
            'shield_item':item_surface_temp[13:20]
        }
    
    def get_sound(self):
        self.start_screen_balloon_popped_sound=pygame.mixer.Sound(os.path.join(sound_path,'SFX/titleScreenAnimationSound_fix.wav'))
        self.start_screen_balloon_popped_sound.set_volume(VOLUME_SFX)
        self.credit_sound=pygame.mixer.Sound(os.path.join(sound_path,'SFX/credit.wav'))
        self.credit_sound.set_volume(VOLUME_SFX)
        self.normal_launch_sound=pygame.mixer.Sound(os.path.join(sound_path,'SFX/shotClaw.wav'))
        self.normal_launch_sound.set_volume(VOLUME_SFX)
        self.vulcan_missile_launch_sound=pygame.mixer.Sound(os.path.join(sound_path,'SFX/shotgun.wav'))
        self.vulcan_missile_launch_sound.set_volume(VOLUME_SFX)
        self.vulcan_missile_ceiling_sound=pygame.mixer.Sound(os.path.join(sound_path,'SFX/shotgunCeiling.wav'))
        self.vulcan_missile_ceiling_sound.set_volume(VOLUME_SFX)
        self.balloon_popped_sound=pygame.mixer.Sound(os.path.join(sound_path,'SFX/balloonPopped.wav'))
        self.balloon_popped_sound.set_volume(VOLUME_SFX)
        self.dead_sound=pygame.mixer.Sound(os.path.join(sound_path,'SFX/dead.wav'))
        self.dead_sound.set_volume(VOLUME_SFX)
    
    def get_font(self):
        self.font_30=pygame.font.Font(os.path.join(font_path,'pang.ttf'),30)
        self.font_40=pygame.font.Font(os.path.join(font_path,'pang.ttf'),40)
        self.font_50=pygame.font.Font(os.path.join(font_path,'pang.ttf'),50)
        self.font_60=pygame.font.Font(os.path.join(font_path,'pang.ttf'),60)
        self.time_font=pygame.font.Font(os.path.join(font_path,'Coiny-Regular.ttf'),50)