#%%
from random import *
import pygame,os,sys,time
#%%
title='PANG'
# screen_size=screen_width,screen_height=1280,960
screen_size=screen_width,screen_height=384*3,(208*3)+(24*4) # 1152,720 8:5
stage_size=stage_width,stage_height=384*3,208*3 # 1152,624
score_board_rect=\
    score_board_x,score_board_y,score_board_w,score_board_h=\
        int(0),stage_height,screen_width,screen_height-stage_height
wall_size=8*3
stage_left=wall_size
stage_right=stage_width-wall_size
stage_top=wall_size
stage_bottom=stage_height-wall_size
player_size=player_width,player_height=32*3,32*3
FPS=60
VOLUME_SFX=0.3
#%%
current_path=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_path,'image')
weapon_path=os.path.join(image_path,'weapon')
sound_path=os.path.join(current_path,'sound')
font_path=os.path.join(current_path,'font')