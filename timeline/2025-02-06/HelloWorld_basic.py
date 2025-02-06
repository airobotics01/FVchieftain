from isaacsim.examples.interactive.base_sample import BaseSample #boiler plate of a robotics extension application

class HelloWorld(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        return

    # This function is called to setup the assets in the scene for the first time
    # Class variables should not be assigned here, since this function is not called
    # after a hot-reload, its only called to load the world starting from an EMPTY stage
    def setup_scene(self):
        # A world is defined in the BaseSample, can be accessed everywhere EXCEPT __init__
        world = self.get_world()
        world.scene.add_default_ground_plane() # adds a default ground plane to the scene
        return