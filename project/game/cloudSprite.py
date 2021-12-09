import arcade
import random

from game import constants

class CloudSprite(arcade.Sprite):
    """ Cloud sprite """
    
    def __init__(self):
        """ Constructor """
        self._constants = constants
        filename = random.choice(self._constants.CLOUDS_IMG)
        scale = random.randrange(self._constants.CLOUD_SCALE[0], self._constants.CLOUD_SCALE[1])
        super().__init__(filename, scale)

        self.center_x = None
        self.center_y = None
        self.speed = None

        self.setup()

    def setup(self):
        """ Setup cloud """
        
        self.center_x = random.randrange(self._constants.SCREEN_WIDTH)
        self.center_y = 0 - self.height
        self.change_y = random.randint(self._constants.CLOUD_SPEED[0], self._constants.CLOUD_SPEED[1])