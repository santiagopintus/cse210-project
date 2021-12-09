import arcade
import math
import random

from game import constants

class BulletSprite(arcade.Sprite):
    """Class of objects that represent the bullet. Extends the arcade.Sprite class

    Attributes:
        jet_sprite (class): An instance of the jetFighterSprite class
        constants: The constants for the game
    Methods:
        setup_bullet: Sets up the bullet for the beginning of the game.
    """
    def __init__(self, filename, scale, jet_sprite):
        """The initializer for the bullet class.

        Parameters:
            self (class): An instance of the bullet class
            filename (str): The filename of the image to use
            scale (float): The scale of the image
        """
        super().__init__(filename, scale)
        
        self._jet_sprite = jet_sprite

        # If the bullet is fired by a player, set the bullet id to 1 or 2
        if self._jet_sprite.get_sprite_name() == "Player":
            self._bullet_id = self._jet_sprite.get_player_number()
        else:
            # If the bullet is fired by an enemy, set the bullet id to 0
            self._bullet_id = 0
        self._constants = constants

        self.setup_bullet()

    def setup_bullet(self):
        """
        Sets up the bullet for the beginning of the game.

        Parameters:
            self (class): An instance of the bullet class
        """
        self._constants = constants
        self.guid = "Bullet"

        # Set bullet speed
        if self.get_bullet_id() != 0:
            b_speed = self._constants.BULLET_SPEED
        else:
            b_speed = self._constants.BULLET_SPEED_ENEMY

        self.change_y = \
            math.cos(math.radians(self._jet_sprite.angle)) * b_speed
        self.change_x = \
            -math.sin(math.radians(self._jet_sprite.angle)) \
            * b_speed

        self.center_x = self._jet_sprite.center_x
        self.center_y = self._jet_sprite.center_y

        # Rotates the bullet to the direction it is moving
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))
        # Plays the bullet sound
        bullet_sound = random.choice(self._constants.BULLET_SOUNDS)
        arcade.play_sound(bullet_sound)

    def get_bullet_id(self):
        """
        Returns the bullet id. Which player fired the bullet.

        Parameters:
            self (class): An instance of the bullet class
        """
        return self._bullet_id

    def update(self):
        """
        Updates the bullet.

        Parameters:
            self (class): An instance of the bullet class
        """
        # Moves the bullet
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If the bullet goes off the screen, remove it
        if self.top > self._constants.TOP_LIMIT or \
            self.bottom < self._constants.BOTTOM_LIMIT or \
            self.right < self._constants.LEFT_LIMIT or \
            self.left > self._constants.RIGHT_LIMIT:
            self.remove_from_sprite_lists()