import ursina
from game.engine.entities.floor import Floor
from game.engine.map import Map
from game.logic.world_manager_interface import WorldManagerInterface


class WorldManager(WorldManagerInterface):
    def load_world(self):
        self.floor = Floor()
        self.map = Map()
        self.sky = ursina.Entity(
            model="sphere",
            texture="sky.png",
            scale=9999,
            double_sided=True
        )
