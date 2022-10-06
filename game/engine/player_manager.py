import ursina
from game.engine.entities.player import Player
from game.logic.player_interface import PlayerInterface
from game.logic.player_manager_interface import PlayerManagerInterface


class PlayerManager(PlayerManagerInterface):
    def spawn_player(self):
        self.player = Player(ursina.Vec3(0, 1, 0))

    def get_player(self) -> PlayerInterface:
        return self.player

