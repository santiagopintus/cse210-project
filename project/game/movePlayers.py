from game.bulletSprite import BulletSprite
from game import constants

class MovePlayers():
    """ Acording to the key pressed or released, moves the different players
    
    Attributes:
        player1 (JetFighterSprite): The first player (Instance of JetFighterSprite class)
        player2 (JetFighterSprite): The second player (Instance of JetFighterSprite class)
        scene (Scene): The scene where the players are moving
        BulletSprite (BulletSprite): The bullet sprite class
        constants (Constants): The constants for the game
    """

    def __init__(self, scene):
        """ Initializes the class """
        self._scene = scene
        self._player1 = self._scene["Players"][0]
        self._player2 = self._scene["Players"][1]
        self._bullet_sprite = BulletSprite
        self._constants = constants

        self._up = [self._constants.P1_UP, self._constants.P2_UP]
        self._down = [self._constants.P1_DOWN, self._constants.P2_DOWN]
        self._left = [self._constants.P1_LEFT, self._constants.P2_LEFT]
        self._right = [self._constants.P1_RIGHT, self._constants.P2_RIGHT]

    def check_button_pressed(self, key_pressed):
        """ Depending on the key pressed, moves the player
        
        Parameters:
            key_pressed (int): The key pressed
        """
        # Move player1
        if key_pressed in self._constants.P1_CONTROLS:
            self.move_player(self._player1, key_pressed)
        # Move player2
        elif key_pressed in self._constants.P2_CONTROLS:
            self.move_player(self._player2, key_pressed)
        # Shoots player1
        elif key_pressed == self._constants.P1_SHOOT:
            self.player_shoot(self._player1)
        # Shoots player2
        elif key_pressed == self._constants.P2_SHOOT:
            self.player_shoot(self._player2)

    def check_button_released(self, key_released):
        """ Depending on the key released, stops a player from moving
        """

        # stops player1
        if key_released in self._constants.P1_CONTROLS:
            self.stop_player(self._player1, key_released)
        # stops player2
        elif key_released in self._constants.P2_CONTROLS:
            self.stop_player(self._player2, key_released)

    
    def move_player(self, player, key_pressed):
        """ Depending on the key pressed, moves the player1
        
        Parameters:
            player (Player): The player to move (Instance of jetFighterSprite class)
            key_pressed (int): The key pressed
        """

        # Moving Forward
        if key_pressed in self._up:
            player.thrust = 0.15
        # Going Reverse
        elif key_pressed in self._down:
            player.thrust = -.2
        # Rotating left
        elif key_pressed in self._left:
            player.change_angle = 3
        # Rotating Right
        elif key_pressed in self._right:
            player.change_angle = -3

    def player_shoot(self, player):
        """ Depending on the key pressed, shoots the bullet
        
        Parameters:
            player (Player): The player to shoot (Instance of jetFighterSprite class)
        """
        # Shoot if the player hit the space bar and we aren't respawning.
        # Create a bullet
        if not player.is_respawning():
            self._bullet_sprite = BulletSprite(
                self._constants.BULLET_IMG, 
                self._constants.BULLET_SCALE,
                player
            )
            self._scene.add_sprite(
                self._constants.P_BULLETS_LIST_NAME, self._bullet_sprite)

    def stop_player(self, player, key_pressed):
        """ Depending on the key released, stops the jet.
        """
        if key_pressed in self._up:
            player.thrust = 0
        elif key_pressed in self._down:
            player.thrust = 0
        elif key_pressed in self._left:
            player.change_angle = 0
        elif key_pressed in self._right:
            player.change_angle = 0