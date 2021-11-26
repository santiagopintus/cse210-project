import arcade
import random

from game import constants
from game.jetFighterSprite import JetFighterSprite
from game.enemiesSprite import EnemiesSprite
from game.movePlayers import MovePlayers
from game.collisionsHandler import CollisionsHandler

class Director(arcade.Window):
    """
    Main application class.
    """
    def __init__(self):
        self._constants = constants

        # Call the parent class and set up the window
        super().__init__(self._constants.SCREEN_WIDTH, self._constants.SCREEN_HEIGHT, self._constants.SCREEN_TITLE)

        arcade.set_background_color(self._constants.BACKGROUND_COLOR)

        self._scene = None
        self._p1_jet_sprite = None
        self._p2_jet_sprite = None
        self._enemy_sprite = None
        self._move_players = None
        self._collisions_handler = None

    def setup(self):
        """ Set up the game and initialize the variables. 
        
        Parameters: 
            self (class): An instance of the director class
        """

        self._scene = arcade.Scene()

        # Create the Sprite lists
        self._scene.add_sprite_list(self._constants.PLAYERS_LIST_NAME)
        self._scene.add_sprite_list(self._constants.ENEMIES_LIST_NAME)
        # Bullets of the players
        self._scene.add_sprite_list(self._constants.P_BULLETS_LIST_NAME)
        # Bullets of the enemies
        self._scene.add_sprite_list(self._constants.E_BULLETS_LIST_NAME)

        #=============== Create the JETS ===============#

        # Set up the player1
        self._p1_jet_sprite = JetFighterSprite(self._constants.PLAYER1_IMG, self._constants.JET_SCALE)
        self._scene.add_sprite(self._constants.PLAYERS_LIST_NAME, self._p1_jet_sprite)
        
        # Set up the player2
        p2_img = self._constants.PLAYER2_IMG
        self._p2_jet_sprite = JetFighterSprite(p2_img, self._constants.JET_SCALE, 2)
        self._scene.add_sprite(self._constants.PLAYERS_LIST_NAME, self._p2_jet_sprite)

        # Set up the enemy
        for _ in range(self._constants.STARTING_ENEMIES_COUNT):
            self._enemy_sprite = EnemiesSprite(
                self._constants.ENEMY_IMG, self._constants.JET_SCALE, 
                self._scene
                )
            self._scene.add_sprite(self._constants.ENEMIES_LIST_NAME, self._enemy_sprite)

        # Set up the moving players class
        self._move_players = MovePlayers(self._scene)
        # Set up the collisions handler class
        self._collisions_handler = CollisionsHandler(self._scene)

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()

        self._scene.draw()

    def on_key_press(self, symbol, modifiers):
        """ Called whenever a key is pressed. """
        
        # Handle the key pressed (Moves or shoots)
        self._move_players.check_button_pressed(symbol)

        self._scene.update()

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        self._move_players.check_button_released(symbol)

    def on_update(self, delta_time):
        """ Move everything """

        self._scene.update()

        # Checks for collisions
        self._collisions_handler.check_collisions()

        # Add new enemies when just one is left
        if len(self._scene.get_sprite_list(self._constants.ENEMIES_LIST_NAME)) < 1:
            # Add STARTING_ENEMIES_COUNT enemies
            # We pass the scene in order to allow the enemies to add bullets to the scene
            for _ in range(self._constants.STARTING_ENEMIES_COUNT):
                self._enemy_sprite = EnemiesSprite(self._constants.ENEMY_IMG, self._constants.JET_SCALE, self._scene)
                self._scene.add_sprite(self._constants.ENEMIES_LIST_NAME, self._enemy_sprite)