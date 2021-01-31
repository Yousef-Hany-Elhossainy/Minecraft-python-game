from ursina import *
from voxel import Voxel


class Sky(Entity):
    def __init__(self,sky_texture):
        
        super().__init__(
            parent = scene,
            model ='sphere',
            texture = sky_texture,
            scale = 250,
            double_sided = True
        )


class Generate_Map():
    
    
    def __init__(self,grass_texture,stone_texture,brick_texture,dirt_texture,sky_texture,map_size):
        block_pick = grass_texture
        map_size = map_size
        map_wall_height = int(map_size/4)
        house_size = int(map_wall_height/3)
        sky = Sky(sky_texture)
        for z in range(map_size):
            for x in range(map_size):
                if (z == 0) or (z == map_size-1) or(x == 0) or (x == map_size-1):
                    for h in range(map_wall_height):
                        voxel = Voxel((x,h,z),texture = stone_texture,destroys = False)
                else:
                    voxel = Voxel((x,0,z),texture = grass_texture, destroys = False)

        for z in range(int((map_size/2)-house_size),int((map_size/2)+house_size)):
            for x in range(int((map_size/2)-house_size),(int(map_size/2)+house_size)):
                if (z == int((map_size/2)-house_size)) or (z == int((map_size/2)+house_size-1)) or(x == int((map_size/2)-house_size)) or (x == int((map_size/2)+house_size-1)):
                    for h in range(map_wall_height):
                        voxel = Voxel((x,h,z),texture = brick_texture)
                else:
                    pass



