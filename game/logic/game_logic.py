from game.logic.input_handler_interface import InputHandlerInterface
from game.logic.player_manager_interface import PlayerManagerInterface
from game.logic.world_manager_interface import WorldManagerInterface


class Game:
    def __init__(self, world_manager: WorldManagerInterface, player_manager: PlayerManagerInterface):
        self.world_manager = world_manager
        self.player_manager = player_manager

    def start(self):
        self.world_manager.load_world()
        self.player_manager.spawn_player()
