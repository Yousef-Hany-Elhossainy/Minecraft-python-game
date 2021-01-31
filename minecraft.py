from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from map import Generate_Map
from hand import Hand
from voxel import Voxel

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
hand_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound.wav',loop=False, autoplay=False)
block_pick = grass_texture

def update():
        global block_pick
            
        if held_keys['1']:
            block_pick = grass_texture
        if held_keys['2']:
            block_pick = stone_texture
        if held_keys['3']:
            block_pick = brick_texture
        if held_keys['4']:
            block_pick = dirt_texture

map = Generate_Map(grass_texture,stone_texture,brick_texture,dirt_texture,sky_texture)

hand = Hand(hand_texture)

person = FirstPersonController(position = (2,2,2))


app.run()

