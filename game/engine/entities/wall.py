import ursina


class Wall(ursina.Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="cube",
            texture="wall.png",
            origin_y=-0.5
        )
        self.texture.filtering = None
        self.collider = ursina.BoxCollider(self, size=ursina.Vec3(1, 2, 1))
