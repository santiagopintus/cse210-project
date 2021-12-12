import arcade

from game import constants

class GuiInterface():
    """ Draws the GUI, which is the score and the lives
    """
    def __init__(self):
        """ Initializes the GUI class
        """
        self._constants = constants

    def drawGUIS(self, player):
        """ Draws the GUI for the player
        """
        self._draw_player_GUI(player)

    def _draw_player_GUI(self, player):
        """ Draws the player's score, lives, and if it's respawning """
        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {player.get_score()}"
        lives_text = f"Lives: {player.get_lives()}"
        respawning_text = f"Respawning..."

        if player.get_player_number() == 1:
            gui_x = self._constants.P1_GUI_X
        else:
            gui_x = self._constants.P2_GUI_X

        arcade.draw_text(
            score_text,
            gui_x,
            self._constants.SCORE_HEIGHT,
            arcade.csscolor.WHITE,
            18
        )
        arcade.draw_text(
            lives_text,
            gui_x,
            self._constants.LIVES_HEIGHT,
            arcade.csscolor.WHITE,
            18
        )
        # Print if the user is respawning
        if player.is_respawning():
            arcade.draw_text(
                respawning_text,
                gui_x,
                self._constants.RESPAWNING_HEIGHT,
                arcade.csscolor.GREENYELLOW,
                18
            )

    def draw_current_level(self, level_num):
        """ Draws the current level on the screen
        """
        level_text = f"Level: {level_num}"
        arcade.draw_text(
            level_text,
            self._constants.SCREEN_WIDTH / 2 - 50,
            self._constants.CURRENT_LEVEL_HEIGHT,
            arcade.csscolor.WHITE,
            24
        )
    
    def draw_game_over(self, final_text):
        """ Draws the win screen
        """
        arcade.draw_text(
            final_text,
            self._constants.SCREEN_WIDTH / 2 - 90,
            self._constants.SCORE_HEIGHT / 2 + 20,
            arcade.csscolor.BLACK,
            40
        )
