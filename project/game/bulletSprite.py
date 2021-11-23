import arcade
import math

from game import constants

class BulletSprite(arcade.Sprite):

    def __init__(self, filename, scale, player_sprite, bullet_sound):
        super().__init__(filename, scale)
        
        self.player_sprite = player_sprite

        self._constants = constants

        self.guid = "Bullet"

        bullet_speed = self._constants.BULLET_SPEED

        self.change_y = \
            math.cos(math.radians(self.player_sprite.angle)) * bullet_speed
        self.change_x = \
            -math.sin(math.radians(self.player_sprite.angle)) \
            * bullet_speed

        self.center_x = self.player_sprite.center_x
        self.center_y = self.player_sprite.center_y

        # Rotates the bullet to the direction it is moving
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))
        # Plays the bullet sound
        arcade.play_sound(bullet_sound)