import arcade
import random
import math

from game.bulletSprite import BulletSprite
from game import constants

class EnemiesSprite(arcade.Sprite):
    """ Sprite that represents an enemy jet. """

    def __init__(self, image_file_name, scale, scene):
        super().__init__(image_file_name, scale=scale)

        self._sprite_name = "Enemy"

        self._constants = constants
        self._bullet_sprite = BulletSprite
        self._scene = scene
        self._enemy_shoot_timer = 0
        self._shooting_speed = random.randint(
            self._constants.ENEMY_SHOOT_TIMER_RANGE[0], self._constants.ENEMY_SHOOT_TIMER_RANGE[1]
        )
        
        # Set position and speed of the jet
        self.setup_enemy()

    def setup_enemy(self):
        """ Set up the enemy. """
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
        # Here we make enemies move in a random direction
        self.change_x = random.choice([random.random() * 3, random.random() * -3])
        self.change_y = random.choice([random.random() * 3, random.random() * -3])
        # Here we make enemies' angle match their direction
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

        self._enemy_shoot_timer += 1
        if self._enemy_shoot_timer > self._shooting_speed:
            self.shoot_bullet()
            self._enemy_shoot_timer = 0

    def shoot_bullet(self):
        """ Create a bullet and add it to the list of bullets. """
        bullet = self._bullet_sprite(self._constants.BULLET_IMG, self._constants.BULLET_SCALE, self)
        self._scene.add_sprite(self._constants.E_BULLETS_LIST_NAME, bullet)

    def get_sprite_name(self):
        """ Returns the sprite name. """
        return self._sprite_name