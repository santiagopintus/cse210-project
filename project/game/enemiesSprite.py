import arcade
import random
import math

from game import constants

class EnemiesSprite(arcade.Sprite):
    """ Sprite that represents an enemy jet. """

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self._constants = constants

        # Set position and speed of the jet
        self.setup_enemy()

    def setup_enemy(self):

        self.guid = "Enemy"

        # Here we make enemies spawn outside the screen
        self.center_y = random.choice(
            [
            random.randrange(self._constants.BOTTOM_LIMIT, 0), # Bottom limit to 0
            random.randrange(0, self._constants.TOP_LIMIT) # 0 to top limit
            ]
            )
        self.center_x = random.choice(
            [
            random.randrange(self._constants.LEFT_LIMIT, 0), # Left limit to 0
            random.randrange(self._constants.SCREEN_WIDTH, self._constants.RIGHT_LIMIT) # 0 to right limit
            ]
        )

        self.change_x = random.choice([random.random() * 3, random.random() * -3])
        self.change_y = random.choice([random.random() * 3, random.random() * -3])

        self.angle = math.degrees(math.atan2(self.change_y, self.change_x)) - 90

    def update(self):
        """ Move the enemy around """
        super().update()
        if self.center_x < self._constants.LEFT_LIMIT:
            self.center_x = self._constants.RIGHT_LIMIT
        if self.center_x > self._constants.RIGHT_LIMIT:
            self.center_x = self._constants.LEFT_LIMIT
        if self.center_y > self._constants.TOP_LIMIT:
            self.center_y = self._constants.BOTTOM_LIMIT
        if self.center_y < self._constants.BOTTOM_LIMIT:
            self.center_y = self._constants.TOP_LIMIT