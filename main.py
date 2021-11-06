#%%
from setting import *
from controller import *
#%%
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen=pygame.display.set_mode((screen_size),pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.clock=pygame.time.Clock() 
        self.start_screen=True
        self.playing=True
        self.start()
    
    def start(self):
        self.controller=Controller(self.screen)
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
    
    def update(self):
        self.controller.update()
    
    def draw(self):
        self.screen.fill('white')
        self.controller.draw()
    
    # print()
#%%
game=Game()
pygame.quit()