from ursina import *



class Voxel(Button):
    
    def __init__(self,position = (0,0,0), texture = None ,destroys = True):
        self.destroyable = destroys
        self.punch_sound = Audio('assets/punch_sound.wav',loop=False, autoplay=False)   
        self.grass_texture = load_texture('assets/grass_block.png')
        self.stone_texture = load_texture('assets/stone_block.png')
        self.brick_texture = load_texture('assets/brick_block.png')
        self.dirt_texture = load_texture('assets/dirt_block.png')     
        self.block_pick = texture
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
    
    def update(self):      
        
        if held_keys['1']:
            self.block_pick = self.grass_texture
        if held_keys['2']:
            self.block_pick = self.stone_texture
        if held_keys['3']:
            self.block_pick = self.brick_texture
        if held_keys['4']:
            self.block_pick = self.dirt_texture

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                self.punch_sound.play()
                boxel = Voxel(((self.position)+ mouse.normal), texture = self.block_pick)
            if key == 'right mouse down':
                self.punch_sound.play()
                if self.destroyable == True:
                    destroy(self)
                
