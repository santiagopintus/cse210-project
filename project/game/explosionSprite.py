import arcade

from game import constants


class ExplosionSprite(arcade.Sprite):
    """ This class creates an explosion animation """

    def __init__(self, textures_list, scale = 1):
        self._constants = constants
        super().__init__()
        # Start at the first frame
        self.current_texture = 0
        self.textures = textures_list
        self.scale = scale

    def update(self):

        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()

    def locate_explosion(self, enemy):
        """
        Create an explosion.
        """
        self.position = enemy.position