from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
hand_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound.wav',loop=False, autoplay=False)
block_pick = grass_texture
map_size = 36
map_wall_height = 12
house_size = 4

class Voxel(Button):
    def __init__(self,position = (0,0,0), texture = grass_texture,destroyable = True):
        super().__init__(
            parent= scene,
            model = 'assets/block',
            texture = texture,
            color = color.color(0,0.2,random.uniform(0.9,1)),
            position = position,
            origin_y = 0.5,
            scale =0.5,
            highlight_color = color.color(0,0,0.9)          
        )
    
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                boxel = Voxel(((self.position)+ mouse.normal), texture = block_pick)
            if key == 'right mouse down':
                punch_sound.play()
                if destroyable:
                    destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model ='sphere',
            texture = sky_texture,
            scale = 200,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent =camera.ui,
            model ='assets/arm',
            texture = hand_texture,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.5,-0.5),
            scale = 0.2
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)
    def normal(self):
        self.rotation = Vec3(150,-10,0),
        self.position = Vec2(0.4,-0.6)


def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.normal()

    if held_keys['1']:
        block_pick = grass_texture
    if held_keys['2']:
        block_pick = stone_texture
    if held_keys['3']:
        block_pick = brick_texture
    if held_keys['4']:
        block_pick = dirt_texture




for z in range(map_size):
    for x in range(map_size):
        if (z == 0) or (z == map_size-1) or(x == 0) or (x == map_size-1):
            for h in range(map_wall_height):
                voxel = Voxel((x,h,z),texture = stone_texture)
        else:
            voxel = Voxel((x,0,z))

for z in range(int((map_size/2)-house_size),int((map_size/2)+house_size)):
    for x in range(int((map_size/2)-house_size),(int(map_size/2)+house_size)):
        if (z == int((map_size/2)-house_size)) or (z == int((map_size/2)+house_size-1)) or(x == int((map_size/2)-house_size)) or (x == int((map_size/2)+house_size-1)):
            for h in range(map_wall_height):
                voxel = Voxel((x,h,z),texture = brick_texture)
        else:
            pass

sky = Sky()

hand = Hand()

person = FirstPersonController(position = (2,2,2))


app.run()

