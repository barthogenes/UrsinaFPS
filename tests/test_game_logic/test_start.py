import unittest
from unittest.mock import MagicMock

from game.logic.game_logic import Game


class test_start(unittest.TestCase):
    def test_connects_to_server_then_loads_world_then_spawns_player(self):
        # arrange
        server_mock = MagicMock()
        world_manager_mock = MagicMock()
        player_manager_mock = MagicMock()
        game = Game(server=server_mock, world_manager=world_manager_mock,
                    player_manager=player_manager_mock)

        # act
        game.start()

        # assert
        server_mock.connect.assert_called_with('localhost', 8000, 'bart')
        world_manager_mock.load_world.assert_called()
        player_manager_mock.spawn_player.assert_called()
