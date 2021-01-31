from ursina import *


class Hand(Entity):
    def __init__(self,hand_texture):
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

    def update(self):
        if held_keys['left mouse'] or held_keys['right mouse']:
            self.active()
        else:
            self.normal()