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
        self.info=pygame.display.Info()
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
            self.get_start_screen.balloons.update()
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
        self.player=pygame.sprite.GroupSingle(Player(self.asset))
        self.items=pygame.sprite.Group()
        
        self.game_ready=True
        self.game_ready_delay=0
        self.playing_game=False
        self.game_over_screen=False
        self.player_die=False
        self.player_die_delay=0
        self.loop()
    
    def loop(self):
        while self.running:
            self.clock.tick(FPS)
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
            self.game_ready_delay+=1
        if self.game_ready_delay>=120:
            self.game_ready=False
            self.playing_game=True
        if self.game_ready:
            self.status=2
    
    def collision(self):
        for weapon in self.player.sprite.weapon_sprite:
            for balloon in self.levels.balloons:
                if pygame.sprite.collide_mask(weapon,balloon) and not self.player_die:
                    self.asset.balloon_popped_sound.play()
                    if balloon.size<3:
                        self.balloons_popped_effect.add(Balloons_Popped_Effect(self.asset,balloon.color,balloon.size,balloon.rect.center))
                        self.items.add(Item_and_Food(self.asset,balloon.rect.center))
                        balloon.kill()
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
                    if not self.player_die:
                        pygame.time.delay(500)
                        if balloon.rect.centerx<player.rect.centerx:
                            self.player.sprite.hit_pos=True
                        else:
                            self.player.sprite.hit_pos=False
                        self.asset.dead_sound.play()
                    self.player_die=True
                    self.player.sprite.action='die'
    
    def next_level(self):
        self.levels.level+=1
        self.levels.levels()
        self.player=pygame.sprite.GroupSingle(Player(self.asset))  
        self.game_ready=True
        self.game_ready_delay=0
        self.playing_game=False
        self.game_over_screen=False
        self.player_die=False
        self.player_die_delay=0
    
    def restart(self):
        if self.player_die:
            self.player_die_delay+=1
            if self.player_die_delay>=100:
                self.start()
    
    def update(self):
        self.set_status()
        if self.playing_game:
            self.levels.update(self.playing_game)
            self.player.sprite.weapon_sprite.update()
            self.player.sprite.launch_effect.update()
            self.levels.balloons.update()
            self.balloons_popped_effect.update()
            self.items.update()
            self.player.update(self.playing_game)
            
            self.collision()
            self.restart()
    
    def draw(self):
        self.levels.draw_background()
        self.player.sprite.weapon_sprite.draw(self.screen)
        self.player.sprite.launch_effect.draw(self.screen)
        self.score_board=pygame.draw.rect(self.screen,'black',score_board_rect)
        self.levels.balloons.draw(self.screen)
        self.balloons_popped_effect.draw(self.screen)
        self.levels.draw_foreground()
        self.player.draw(self.screen)
        self.items.draw(self.screen)
        self.levels.draw_text(self.playing_game,self.game_ready)
        self.levels.draw_status(self.game_ready)
        
        print(self.game_ready_delay)
        if self.game_over_screen:
            pass
            # for r in range(26):
            #     for c in range(48):
            #         pygame.draw.rect(self.screen,('blue'),(c*24,r*24,24,24),2)
            #         # self.items.add(Item_and_Food(c*24,r*24))
#%%
game=Game()
pygame.quit()