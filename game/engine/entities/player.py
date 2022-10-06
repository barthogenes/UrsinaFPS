import ursina
from game.engine.entities.gun import Gun
from game.logic.player_interface import PlayerInterface
from ursina import camera, curve
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.sequence import Func


class Player(FirstPersonController, PlayerInterface):
    def __init__(self, position: ursina.Vec3):
        super().__init__(
            position=position,
            model="cube",
            jump_height=2.5,
            jump_duration=0.4,
            origin_y=-2,
            collider="box",
            speed=7
        )
        self.cursor.color = ursina.color.rgb(255, 0, 0, 122)

        self.gun = Gun()

        self.healthbar_pos = ursina.Vec2(0, 0.45)
        self.healthbar_size = ursina.Vec2(0.8, 0.04)
        self.healthbar_bg = ursina.Entity(
            parent=ursina.camera.ui,
            model="quad",
            color=ursina.color.rgb(255, 0, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )
        self.healthbar = ursina.Entity(
            parent=ursina.camera.ui,
            model="quad",
            color=ursina.color.rgb(0, 255, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )

        self._health = 100
        self.death_message_shown = False

    def set_health(self, amount: int):
        self._health = amount

    def get_health(self) -> int:
        return self._health

    def death(self):
        self.death_message_shown = True

        ursina.destroy(self.gun)
        self.rotation = 0
        self.camera_pivot.world_rotation_x = 0
        self.world_position = ursina.Vec3(0, 7, -35)
        self.cursor.color = ursina.color.rgb(0, 0, 0, a=0)
        self.gravity = 0

        ursina.Text(
            text="You are dead!",
            origin=ursina.Vec2(0, 0),
            scale=3
        )

    def shoot_gun(self):
        self.gun.shoot(self.position, self.world_rotation_y, -
                       self.camera_pivot.world_rotation_x)

    def input(self, key: str):
        if key == 'space':
            self.jump()

        if key == "left mouse down":
            self.shoot_gun()

        if key == "right mouse down":
            camera.animate('fov', 60, duration=.2, curve=curve.in_sine)

        if key == "right mouse up":
            camera.animate('fov', 90, duration=.2, curve=curve.in_sine)

        if key == "shift":
            self.animate('speed', 14, duration=.2, curve=curve.in_sine)

        if key == "shift up":
            self.animate('speed', 7, duration=.2, curve=curve.in_sine)

        if key == "p":
            self.death()

    def update(self):
        self.healthbar.scale_x = self._health / 100 * self.healthbar_size.x

        if self._health <= 0:
            if not self.death_message_shown:
                self.death()
        else:
            super().update()
