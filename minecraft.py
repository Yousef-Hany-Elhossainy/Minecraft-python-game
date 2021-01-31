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
    

def get_user_choice():
    """Prompts the user for its choice and return it."""
    user_input = input('Your choice: ')
    return user_input

    

def listen_for_input():
    waiting_for_input = True
    
    while waiting_for_input:
        print("Welcome to this simple minecraft game.")
        print("1:Start Game")
        print("q: Quit")
        user_choice = get_user_choice()
        if user_choice == '1':   
            global map_size  
            map_size = input("Enter map size(24-42)")
            if int(map_size) > 42 or int(map_size) < 24 :
                print("Invalid input")
                continue
            waiting_for_input = False
            
            
        if user_choice == 'q':
            app.quit()


listen_for_input()

hand = Hand(hand_texture)
person = FirstPersonController(position = (2,2,2))
map = Generate_Map(grass_texture,stone_texture,brick_texture,dirt_texture,sky_texture,int(map_size))
app.run()


