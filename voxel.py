from ursina import *

block_pick = None

class Voxel(Button):
    

    def __init__(self,position = (0,0,0), texture = None ,destroys = True):
        self.destroyable = destroys
        self.punch_sound = Audio('assets/punch_sound.wav',loop=False, autoplay=False)        
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
                self.punch_sound.play()
                boxel = Voxel(((self.position)+ mouse.normal), texture = block_pick)
            if key == 'right mouse down':
                self.punch_sound.play()
                if self.destroyable == True:
                    destroy(self)
                
