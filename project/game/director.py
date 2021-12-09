import arcade
from time import sleep
import random

from game import constants
from game.jetFighterSprite import JetFighterSprite
from game.enemiesSprite import EnemiesSprite
from game.movePlayers import MovePlayers
from game.collisionsHandler import CollisionsHandler
from game.guiInterface import GuiInterface
from game.cloudSprite import CloudSprite

# Start of Director class
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
        self._gui_interface = None
        self._cloud_sprite = None
        self._enemies_count = 0
        self._current_level = 1
        self._game_over = 0

    def setup(self):
        """ Set up the game and initialize the variables. 
        
        Parameters: 
            self (class): An instance of the director class
        """

        self._scene = arcade.Scene()
        self._gui_interface = GuiInterface()
        self._cloud_sprite = CloudSprite
        #--------------- Create the Sprite lists
        self._scene.add_sprite_list(self._constants.PLAYERS_LIST_NAME)
        self._scene.add_sprite_list(self._constants.ENEMIES_LIST_NAME)
        # Bullets of the players
        self._scene.add_sprite_list(self._constants.P_BULLETS_LIST_NAME)
        # Bullets of the enemies
        self._scene.add_sprite_list(self._constants.E_BULLETS_LIST_NAME)
        # Explosion of the enemies
        self._scene.add_sprite_list(self._constants.EXPLOSIONS_LIST_NAME)
        # Clouds
        self._scene.add_sprite_list(self._constants.CLOUDS_LIST_NAME)

        # The following number will increase as the player kills enemies
        self._enemies_count = self._constants.STARTING_ENEMIES_COUNT

        #=============== Create the JETS ===============#

        # Set up the player1
        self._p1_jet_sprite = JetFighterSprite(self._constants.PLAYER1_IMG, self._constants.JET_SCALE, self._scene)
        self._scene.add_sprite(self._constants.PLAYERS_LIST_NAME, self._p1_jet_sprite)
        
        # Set up the player2
        p2_img = self._constants.PLAYER2_IMG
        self._p2_jet_sprite = JetFighterSprite(p2_img, self._constants.JET_SCALE, self._scene, 2)
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
        # Plays the backgroun music
        for sound in self._constants.BACKGROUND_SOUNDS:
            arcade.play_sound(sound)
        # Plays the game music

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()

        self._scene.draw()

        self._gui_interface.drawGUIS(self._p1_jet_sprite)
        self._gui_interface.drawGUIS(self._p2_jet_sprite)
        self._gui_interface.draw_current_level(self._current_level)
        if self._game_over == 1:
            self._gui_interface.draw_game_over('You won!')
        elif self._game_over == 2:
            self._gui_interface.draw_game_over('Game Over')

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

        if self._game_over == 0:
            
            # Checks for collisions
            self._collisions_handler.check_collisions()
            self._scene.update()

            # Keeping track of the enemies count
            current_enemy_count = len(self._scene.get_sprite_list(self._constants.ENEMIES_LIST_NAME))
            # Add new enemies when the last is killed
            if  current_enemy_count < 1:
                self._current_level += 1
                # We pass the scene in order to allow the enemies to add bullets to the scene
                for _ in range(self._enemies_count):
                    self._enemy_sprite = EnemiesSprite(self._constants.ENEMY_IMG, self._constants.JET_SCALE, self._scene)
                    self._scene.add_sprite(self._constants.ENEMIES_LIST_NAME, self._enemy_sprite)
                if self._enemies_count < self._constants.MAX_ENEMIES_COUNT:
                    self._enemies_count += 1
            
            # Spawns clouds
            if len(self._scene[self._constants.CLOUDS_LIST_NAME]) < self._constants.CLOUDS_COUNT:
                cloud = self._cloud_sprite()
                self._scene.add_sprite(self._constants.CLOUDS_LIST_NAME, cloud)
            for cloud in self._scene[self._constants.CLOUDS_LIST_NAME]:
                if cloud.center_y > self._constants.SCREEN_HEIGHT:
                    cloud.kill()

            # Checking for end of loop
            if self._current_level == self._constants.WIN_LEVEL:
                # Player/s won the game
                self._game_over = 1
            elif len(self._scene[self._constants.PLAYERS_LIST_NAME]) < 1:
                # Players lost the game
                self._game_over = 2
            
        else:
            sleep(3)
            self.close()