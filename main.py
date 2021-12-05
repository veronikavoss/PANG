#%%
from setting import *
from asset import Asset
from start_screen import Start_Screen
from level import Level
from player import Player
from balloon import *
from item_and_food import Item_and_Food
#%%
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen=pygame.display.set_mode(screen_size)
        self.clock=pygame.time.Clock()
        self.running=True
        self.game_over_screen=False
        
        self.asset=Asset()
        self.levels=Level(self.screen,self.asset)
        self.start_screen()
    
    def start_screen(self):
        self.get_start_screen=Start_Screen(self.screen,self.asset)
        running=True
        while running:
            self.clock.tick(FPS)
            
            self.get_start_screen.update()
            self.get_start_screen.balloons.update(self.wave_alpha_value())
            self.get_start_screen.balloons_popped_effect.update()
            
            self.get_start_screen.draw()
            self.get_start_screen.balloons.draw(self.screen)
            self.get_start_screen.balloons_popped_effect.draw(self.screen)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                
                if event.type==pygame.KEYUP and self.get_start_screen.logo:
                    self.asset.credit_sound.play()
                    self.start()
                    running=False
    
    def start(self):
        self.levels.levels()
        self.balloons_popped_effect=pygame.sprite.Group()
        self.player=pygame.sprite.GroupSingle(Player(self.screen,self.asset))
        self.items=pygame.sprite.Group()
        
        self.game_ready=True
        self.game_ready_delay=0
        self.playing_game=False
        self.game_over_screen=False
        self.player_die=False
        self.player_die_delay=0
        
        self.item_dynamite=False
        self.item_dynamite_runtime=0
        self.item_slow=False
        self.item_slow_update_time=0
        self.item_stop=False
        self.item_stop_update_time=0
        
        self.loop()
    
    def loop(self):
        while self.running:
            self.dt=self.clock.tick(FPS)//15
            self.current_time=pygame.time.get_ticks()
            self.events()
            self.update()
            self.draw()
            pygame.display.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.running:
                    self.running=False
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    self.running=False
    
    def set_status(self):
        if self.game_ready:
            self.game_ready_delay+=1*self.dt
        if self.game_ready_delay>=120:
            self.game_ready=False
            self.playing_game=True
        if self.game_ready:
            self.status=2
    
    def collision(self):
        if not self.player_die:
            for weapon in self.player.sprite.weapon_sprite:
                for balloon in self.levels.balloons:
                    if pygame.sprite.collide_mask(weapon,balloon):
                        self.asset.balloon_popped_sound.play()
                        if balloon.size<3:
                            self.balloons_popped_effect.add(Balloons_Popped_Effect(self.asset,balloon.color,balloon.size,balloon.rect.center))
                            item_probability=randint(1,1)
                            if item_probability==1:
                                self.items.add(Item_and_Food(self.asset,balloon.rect.center))
                            balloon.kill()
                            if self.item_stop:
                                self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,(balloon.rect.centerx+(balloon.rect.w//4),balloon.rect.centery),True,True))
                                self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,(balloon.rect.centerx-(balloon.rect.w//4),balloon.rect.centery),False,True))
                            else:
                                self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,balloon.rect.center,True,True))
                                self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,balloon.rect.center,False,True))
                        else:
                            self.balloons_popped_effect.add(Balloons_Popped_Effect(self.asset,balloon.color,balloon.size,balloon.rect.center))
                            balloon.kill()
                            if len(self.levels.balloons)==0:
                                self.next_level()
                        
                        weapon.kill()
        
            for player in self.player:
                for balloon in self.levels.balloons:
                    if pygame.sprite.collide_mask(player,balloon):
                        # if not self.item_stop:
                            if self.player.sprite.shield_status=='shield':
                                self.player.sprite.shield_status='crashed'
                                self.player.sprite.shield=False
                            elif self.player.sprite.shield_status=='normal':
                            # elif self.player.sprite.shield_status=='normal' and not self.player.sprite.shield or self.item_stop:
                                pygame.time.delay(500)
                                if balloon.rect.centerx<player.rect.centerx:
                                    self.player.sprite.hit_pos=True
                                else:
                                    self.player.sprite.hit_pos=False
                                self.asset.dead_sound.play()
                                self.player_die=True
                                self.player.sprite.action='die'
                
                for item in self.items:
                    if pygame.sprite.collide_mask(player,item):
                        if item.item_type=='weapon_items':
                            self.player.sprite.previous_weapon=self.player.sprite.weapon
                            if item.item=='power_wire':
                                if self.player.sprite.previous_weapon=='double_wire':
                                    self.player.sprite.weapon='double_power_wire'
                                else:
                                    self.player.sprite.weapon='power_wire'
                            else:
                                self.player.sprite.weapon=item.item
                        
                        if item.item_type=='clock_items':
                            if item.item=='slow':
                                self.item_slow=True
                                self.item_slow_update_time=pygame.time.get_ticks()
                            else:
                                self.item_slow=False
                            if item.item=='stop':
                                self.item_stop=True
                                self.item_stop_update_time=pygame.time.get_ticks()
                        
                        if item.item_type=='shield_item' and item.item=='shield':
                            if self.player.sprite.shield_status=='normal':
                                self.player.sprite.shield_status='shield'
                                self.player.sprite.shield=True
                            elif self.player.sprite.shield_status=='crashed':
                                self.player.sprite.shield=True
                        
                        if item.item_type=='dynamite_item':
                            if item.item=='dynamite':
                                self.item_dynamite=True
                                self.item_dynamite_runtime=pygame.time.get_ticks()
                        
                        item.kill()
    
    def item_clock(self):
        global FPS
        
        if not self.player_die:
            if self.item_slow:
                if self.current_time-self.item_slow_update_time<=5000:
                    FPS=30
                else:FPS=60
            else:FPS=60
            
            if self.item_stop:
                for balloon in self.levels.balloons.sprites():
                    if self.current_time-self.item_stop_update_time<=5000:
                        balloon.stop=True
                    if self.current_time-self.item_stop_update_time>5000:
                        balloon.Warning_animation=True
                    if self.current_time-self.item_stop_update_time>7000:
                        balloon.Warning_animation=False
                        balloon.stop=False
        
        else:FPS=60
    
    def run_item_dynamite(self,balloon):
        self.balloons_popped_effect.add(Balloons_Popped_Effect(self.asset,balloon.color,balloon.size,balloon.rect.center))
        self.asset.balloon_popped_sound.play()
        item_probability=randint(1,2)
        if item_probability==1:
            self.items.add(Item_and_Food(self.asset,balloon.rect.center))
        balloon.kill()
        if self.item_stop:
            self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,(balloon.rect.centerx+(balloon.rect.w//4),balloon.rect.centery),True,True))
            self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,(balloon.rect.centerx-(balloon.rect.w//4),balloon.rect.centery),False,True))
        else:
            self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,balloon.rect.center,True,True))
            self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,balloon.rect.center,False,True))
        # self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,(balloon.rect.centerx+(balloon.rect.w//4),balloon.rect.centery),True,True))
        # self.levels.balloons.add(Balloon(self.asset,balloon.color,balloon.size+1,(balloon.rect.centerx-(balloon.rect.w//4),balloon.rect.centery),False,True))
    
    def set_item_dynamite(self):
        if self.item_dynamite:
            for balloon in self.levels.balloons:
                if balloon.size==0:
                    self.run_item_dynamite(balloon)
                elif balloon.size==1 and self.current_time-self.item_dynamite_runtime>=300:
                    self.run_item_dynamite(balloon)
                elif balloon.size==2 and self.current_time-self.item_dynamite_runtime>=600:
                    self.run_item_dynamite(balloon)
                    self.item_dynamite=False
    
    def wave_alpha_value(self,value=100):
        current_time=pygame.time.get_ticks()//value # default 0.1s
        if current_time%2==0:
            return 255
        else:
            return 0
    
    def next_level(self):
        self.balloons_popped_effect.empty()
        self.levels.level+=1*self.dt
        self.levels.levels()
        self.player=pygame.sprite.GroupSingle(Player(self.screen,self.asset))
        self.items.empty()
        self.game_ready=True
        self.game_ready_delay=0
        self.playing_game=False
        self.game_over_screen=False
        self.player_die=False
        self.player_die_delay=0
    
    def restart(self):
        if self.player_die:
            self.player_die_delay+=1*self.dt
            if self.player_die_delay>=100:
                self.start()
    
    def update(self):
        self.set_status()
        if self.playing_game:
            self.levels.update(self.playing_game)
            self.player.sprite.weapon_sprite.update(self.dt)
            self.player.sprite.launch_effect.update(self.dt)
            self.levels.balloons.update(self.wave_alpha_value())
            self.balloons_popped_effect.update()
            self.wave_alpha_value()
            self.items.update(self.wave_alpha_value(200),self.dt)
            self.player.update(self.playing_game,self.dt)
            
            self.collision()
            self.item_clock()
            self.set_item_dynamite()
            self.restart()
    
    def draw(self):
        self.levels.draw_background()
        self.player.sprite.weapon_sprite.draw(self.screen)
        self.player.sprite.launch_effect.draw(self.screen)
        self.score_board=pygame.draw.rect(self.screen,'black',score_board_rect)
        self.levels.draw_foreground()
        self.player.sprite.draw_shield(self.dt)
        self.levels.balloons.draw(self.screen)
        self.balloons_popped_effect.draw(self.screen)
        self.player.draw(self.screen)
        self.items.draw(self.screen)
        self.levels.draw_text(self.playing_game,self.game_ready)
        self.levels.draw_status(self.game_ready,self.dt,self.wave_alpha_value())
        if self.game_over_screen:
            pass
        print(self.player.sprite.shield_status)
#%%
game=Game()
pygame.quit()