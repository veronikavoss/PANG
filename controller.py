#%%
from setting import *
from background import *
from player import *
#%%
class Controller:
    def __init__(self,screen):
        self.screen=screen
        self.level=1
        self.background=Background(self.screen,self.level)
        self.foreground=Foreground(self.screen,self.level)
        self.player=pygame.sprite.GroupSingle(Player(self.level))
    
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