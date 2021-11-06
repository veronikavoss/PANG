#%%
import pygame,os
#%%
title='PANG'
# screen_size=screen_width,screen_height=1280,960
screen_size=screen_width,screen_height=384*3,208*3
wall_size=8*3
stage_left=wall_size
stage_right=screen_width-wall_size
stage_top=wall_size
stage_bottom=screen_height-wall_size
player_size=player_width,player_height=32*3,32*3
FPS=60
#%%
current_path=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_path,'image')
sound_path=os.path.join(current_path,'sound')