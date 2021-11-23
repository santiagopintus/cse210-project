import arcade
import math
import os

from game import constants
from game.jetFighterSprite import JetFighterSprite
from game.enemiesSprite import EnemiesSprite
from game.bulletSprite import BulletSprite
from game.movePlayers import MovePlayers

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

        arcade.set_background_color(self._constants.BACKGROUND_COLOR)

        self._scene = None
        self._p1_jet_sprite = None
        self._enemy_sprite = None
        self._bullet_sprite = None
        self._move_players = None

        # Sounds
        self._BULLET_SOUND = None
        self._ENEMY_DEAD_SOUND = None
        self._PLAYER_DEAD_SOUND = None

    def setup(self):
        """ Set up the game and initialize the variables. 
        
        Parameters: 
            self (class): An instance of the director class
        """

        self._scene = arcade.Scene()

        # Inizialize the sounds
        self._BULLET_SOUND = arcade.load_sound("../assets/sounds/shoot1.wav")
        self._ENEMY_DEAD_SOUND = arcade.load_sound("../assets/sounds/enemy_boom1.wav")
        self._PLAYER_DEAD_SOUND = arcade.load_sound("../assets/sounds/boom1.wav")
        
        # Create the Sprite lists
        self._scene.add_sprite_list("Player")
        self._scene.add_sprite_list("Bullets")
        self._scene.add_sprite_list("Enemies")

        # Set up the player
        p1_img = self._constants.PLAYER1_IMG
        jet_scale = self._constants.JET_SCALE
        self._p1_jet_sprite = JetFighterSprite(p1_img, jet_scale)
        self._scene.add_sprite("Player", self._p1_jet_sprite)

        # Set up the moving players class
        self._move_players = MovePlayers(self._p1_jet_sprite, self._scene, self._BULLET_SOUND)

        # Set up the enemy
        enem_img = self._constants.ENEMY_IMG
        for _ in range(self._constants.STARTING_ENEMIES_COUNT):
            self._enemy_sprite = EnemiesSprite(enem_img, jet_scale)
            self._scene.add_sprite("Enemies", self._enemy_sprite)

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()

        self._scene.draw()

    def on_key_press(self, symbol, modifiers):
        """ Called whenever a key is pressed. """
        
        # Move players handle the key pressed
        self._move_players.check_button_pressed(symbol)

        self._scene.update()

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        self._move_players.check_button_released(symbol)

    def on_update(self, delta_time):
        """ Move everything """

        self._scene.update()
        
        #Check for collisions if user is not respawning
        # (Later we will use a separate class for handling collisions)
        if not self._p1_jet_sprite.is_respawning():
            enemies = arcade.check_for_collision_with_list(self._p1_jet_sprite, self._scene["Enemies"])
            if len(enemies) > 0:
                for enemy in enemies:
                    self._p1_jet_sprite.respawn()
                    arcade.play_sound(self._PLAYER_DEAD_SOUND)
                    arcade.play_sound(self._ENEMY_DEAD_SOUND)
                    enemy.remove_from_sprite_lists()

            for bullet in self._scene["Bullets"]:
                enemies_shooted = arcade.check_for_collision_with_list(bullet, self._scene["Enemies"])

                if len(enemies_shooted) > 0:
                    for enemy in enemies_shooted:
                        arcade.play_sound(self._ENEMY_DEAD_SOUND)
                        bullet.remove_from_sprite_lists()
                        enemy.remove_from_sprite_lists()
