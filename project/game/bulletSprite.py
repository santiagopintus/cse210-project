import arcade
import math

class BulletSprite(arcade.Sprite):

    def __init__(self, filename, scale, player_sprite):
        super().__init__(filename, scale)
        
        self.player_sprite = player_sprite
        self.speed = 0

        self.guid = "Bullet"

        bullet_speed = 13
        self.change_y = \
            math.cos(math.radians(self.player_sprite.angle)) * bullet_speed
        self.change_x = \
            -math.sin(math.radians(self.player_sprite.angle)) \
            * bullet_speed

        self.center_x = self.player_sprite.center_x
        self.center_y = self.player_sprite.center_y