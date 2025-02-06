from isaacsim.examples.interactive.base_sample import BaseSample
from isaacsim.core.api import World

class HelloWorld(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        return

    def setup_scene(self):
        world = World.instance()
        world.scene.add_default_ground_plane()
        return