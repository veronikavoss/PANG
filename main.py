#%%
from setting import *
from background import *
from player import *
#%%
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen=pygame.display.set_mode((screen_size),pygame.RESIZABLE)
        self.info=pygame.display.Info()
        self.clock=pygame.time.Clock() 
        self.start_screen=True
        self.playing=True
        self.level=1
        self.start()
    
    def start(self):
        self.background=Background(self.screen,self.level)
        self.foreground=Foreground(self.screen,self.level)
        self.player=pygame.sprite.GroupSingle(Player(self.level))
        self.loop()
    
    def loop(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)
    
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.playing:
                    self.playing=False
                    break
            if event.type==pygame.VIDEORESIZE:
                self.screen=pygame.display.set_mode((self.info.current_w,self.info.current_h),pygame.FULLSCREEN)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    self.playing=False
    
    def update(self):
        self.player.sprite.weapon_sprite.update()
        self.player.sprite.launch_effect.update()
        self.player.sprite.balloons.update()
        self.player.update()
    
    def draw(self):
        self.background.draw()
        self.player.sprite.weapon_sprite.draw(self.screen)
        self.player.sprite.launch_effect.draw(self.screen)
        self.player.sprite.balloons.draw(self.screen)
        self.foreground.draw()
        self.player.draw(self.screen)
#%%
game=Game()
pygame.quit()