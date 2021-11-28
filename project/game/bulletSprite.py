import arcade
import math

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

        if self._jet_sprite.get_sprite_name() == "Player":
            self._bullet_id = self._jet_sprite.get_player_number()
        else:
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

        self.change_y = \
            math.cos(math.radians(self._jet_sprite.angle)) * self._constants.BULLET_SPEED
        self.change_x = \
            -math.sin(math.radians(self._jet_sprite.angle)) \
            * self._constants.BULLET_SPEED

        self.center_x = self._jet_sprite.center_x
        self.center_y = self._jet_sprite.center_y

        # Rotates the bullet to the direction it is moving
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))
        # Plays the bullet sound
        arcade.play_sound(self._constants.BULLET_SOUND)

    def get_bullet_id(self):
        """
        Returns the bullet id. Which player fired the bullet.

        Parameters:
            self (class): An instance of the bullet class
        """
        return self._bullet_id