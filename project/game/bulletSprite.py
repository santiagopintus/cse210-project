import arcade
import math

from game import constants

class BulletSprite(arcade.Sprite):
    """Class of objects that represent the bullet. Extends the arcade.Sprite class

    Attributes:
        jet_sprite (class): An instance of the jetFighterSprite class
        bullet_sound (class): A bullet sound loaded with arcade.load_sound()
        constants: The constants for the game
    Methods:
        setup_bullet: Sets up the bullet for the beginning of the game.
    """
    def __init__(self, filename, scale, jet_sprite, bullet_sound):
        """The initializer for the bullet class.

        Parameters:
            self (class): An instance of the bullet class
            filename (str): The filename of the image to use
            scale (float): The scale of the image
            jet_sprite (class): An instance of the jetFighterSprite class
            bullet_sound (class): A bullet sound loaded with arcade.load_sound()
        """
        super().__init__(filename, scale)
        
        self._jet_sprite = jet_sprite
        self._constants = constants
        self._bullet_sound = bullet_sound

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
        arcade.play_sound(self._bullet_sound)