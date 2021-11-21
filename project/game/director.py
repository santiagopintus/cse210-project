import arcade
import random
import math
import os

from game import constants
from game.jet_fighter import JetFighter
from game.enemiesSprite import EnemiesSprite
from game.bulletSprite import BulletSprite

class Director(arcade.Window):
    """
    Main application class.
    """
    def __init__(self):
        self._constants = constants

        # Call the parent class and set up the window
        super().__init__(self._constants.SCREEN_WIDTH, self._constants.SCREEN_HEIGHT, self._constants.SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self._scene = None
        self._jet_sprite = None
        self._enemy_sprite = None
        self._bullet_sprite = None
        self._turning_sprite = None

        # Assets
        self._player_img = "../assets/images/player.png"
        self._enemy_img = "../assets/images/enemy.png"
        self._bullet_img = "../assets/images/bullet.png"

        # Load sounds
        self._shoot_sound = arcade.load_sound("../assets/sounds/shoot1.wav")
        self._enemy_dead_sound = arcade.load_sound("../assets/sounds/enemy_boom1.wav")
        self._player_dead_sound = arcade.load_sound("../assets/sounds/boom1.wav")

    def setup(self):

        self._scene = arcade.Scene()

        # Create the Sprite lists
        self._scene.add_sprite_list("Player")
        self._scene.add_sprite_list("Bullets")
        self._scene.add_sprite_list("Enemies")

        # Set up the player
        self._jet_sprite = JetFighter(self._player_img, self._constants.JET_SCALE)
        self._scene.add_sprite("Player", self._jet_sprite)
        # Set up the enemy
        for _ in range(self._constants.STARTING_ENEMIES_COUNT):
            self._enemy_sprite = EnemiesSprite(self._enemy_img, self._constants.JET_SCALE)
            self._scene.add_sprite("Enemies", self._enemy_sprite)

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()

        self._scene.draw()

    def on_key_press(self, symbol, modifiers):
        """ Called whenever a key is pressed. """

        # SHOOTING
        # Shoot if the player hit the space bar and we aren't respawning.
        if not self._jet_sprite.respawning and symbol == arcade.key.SPACE:
            
            self._bullet_sprite = BulletSprite(
                self._bullet_img, 
                self._constants.SCALE,
                self._jet_sprite
            )

            # Rotates the bullet to the direction it is moving
            self._bullet_sprite.angle = math.degrees(math.atan2(self._bullet_sprite.change_y, self._bullet_sprite.change_x))
            
            self._scene.add_sprite("Bullets", self._bullet_sprite)

            arcade.play_sound(self._shoot_sound)

        # MOVING
            # Rotating left
        if symbol == arcade.key.LEFT:
            self._jet_sprite.change_angle = 3
            # Rotating Right
        elif symbol == arcade.key.RIGHT:
            self._jet_sprite.change_angle = -3
            # Moving Forward
        elif symbol == arcade.key.UP:
            self._jet_sprite.thrust = 0.15
            # Going Reverse
        elif symbol == arcade.key.DOWN:
            self._jet_sprite.thrust = -.2

        self._scene.update()

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            self._jet_sprite.change_angle = 0
        elif symbol == arcade.key.RIGHT:
            self._jet_sprite.change_angle = 0
        elif symbol == arcade.key.UP:
            self._jet_sprite.thrust = 0
        elif symbol == arcade.key.DOWN:
            self._jet_sprite.thrust = 0

    def on_update(self, delta_time):
        """ Move everything """

        self._scene.update()
        
        #Check for collisions if user is not respawning
        # (Later we will use a separate class for handling collisions)
        if not self._jet_sprite.respawning:
            enemies = arcade.check_for_collision_with_list(self._jet_sprite, self._scene["Enemies"])
            if len(enemies) > 0:
                for enemy in enemies:
                    self._jet_sprite.respawn()
                    arcade.play_sound(self._player_dead_sound)
                    arcade.play_sound(self._enemy_dead_sound)
                    enemy.remove_from_sprite_lists()

            for bullet in self._scene["Bullets"]:
                enemies_shooted = arcade.check_for_collision_with_list(bullet, self._scene["Enemies"])

                if len(enemies_shooted) > 0:
                    for enemy in enemies_shooted:
                        arcade.play_sound(self._enemy_dead_sound)
                        enemy.remove_from_sprite_lists()