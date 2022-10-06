import os
import threading

import ursina

from game.engine.player_manager import PlayerManager
from game.engine.world_manager import WorldManager
from game.logic.game_logic import Game

app = ursina.Ursina()
ursina.window.borderless = False
ursina.window.title = "Ursina FPS"
ursina.window.exit_button.visible = False

game = Game(world_manager=WorldManager(),
            player_manager=PlayerManager())


def main():
    game.start()
    app.run()


if __name__ == "__main__":
    main()
