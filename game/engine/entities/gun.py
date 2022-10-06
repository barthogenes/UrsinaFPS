import ursina
from game.engine.entities.bullet import Bullet
from game.logic.gun_interface import GunInterface
from ursina.entity import Entity


class Gun(GunInterface, Entity):
    def __init__(self):
        super().__init__(
            parent=ursina.camera.ui,
            position=ursina.Vec2(0.6, -0.45),
            scale=ursina.Vec3(0.1, 0.2, 0.65),
            rotation=ursina.Vec3(-20, -20, -5),
            model="cube",
            texture="white_cube",
            color=ursina.color.color(0, 0, 0.4)
        )

    def shoot(self, position, rotation_y, rotation_x):
        b_pos = position + ursina.Vec3(0, 2, 0)
        bullet = Bullet(b_pos, rotation_y, rotation_x)
        ursina.destroy(bullet, delay=2)
