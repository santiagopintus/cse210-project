import arcade
import math
from game import constants

class JetFighterSprite(arcade.Sprite):
    """
    Sprite that represents the jet fighter.

    Inherits from arcade.Sprite class
    """
    def __init__(self, filename, scale, player_number = 1):
        """ Sets up the jet player. 
        
        Parameters:
            filename (str): The filename of the image to use for the jet.
            scale (float): The scale of the jet.
            player_number (int): The player number. (1 by default)
        """
        self._constants = constants

        # Call the parent Sprite constructor
        super().__init__(filename, scale)

        # Info on where we are going.
        # Angle comes in automatically from the parent class.
        self.thrust = 0
        self.speed = 0
        self._max_speed = self._constants.MAX_SPEED
        self.drag = 0.05
        self._respawning = 0
        self._player_number = player_number

        # Mark that we are respawning.
        self.respawn()

    def respawn(self):
        """
        Called when we die and need to make a new jet.
        'respawning' is an invulnerability timer.
        """
        # If we are in the middle of respawning, this is non-zero.
        self._respawning = 1
        
        # Depending on the player number, we might start in a different x position.
        if self._player_number == 1:
            self.center_x = self._constants.P1_X_POS
        else:
            self.center_x = self._constants.P2_X_POS

        self.center_y = self._constants.SCREEN_HEIGHT / 2
        self.angle = 0

    def is_respawning(self):
        """
        Returns the respawning status.
        """
        return self._respawning

    def update(self):
        """
        Update our position and other particulars.
        """
        if self._respawning:
            self._respawning += 1
            self.alpha = self._respawning
            if self._respawning > 250:
                self._respawning = 0
                self.alpha = 255

        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self._max_speed:
            self.speed = self._max_speed
        if self.speed < -self._max_speed:
            self.speed = -self._max_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If the ship goes off-screen, move it to the other side of the window
        if self.right < 0:
            self.left = self._constants.SCREEN_WIDTH

        if self.left > self._constants.SCREEN_WIDTH:
            self.right = 0

        if self.top < 0:
            self.bottom = self._constants.SCREEN_HEIGHT

        if self.bottom > self._constants.SCREEN_HEIGHT:
            self.top = 0

        """ Call the parent class. """
        super().update()