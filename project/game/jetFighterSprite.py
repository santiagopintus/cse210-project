import arcade
import math
from game import constants

class JetFighterSprite(arcade.Sprite):
    """
    Sprite that represents the jet fighter.

    Inherits from arcade.Sprite class
    """
    def __init__(self, filename, scale):
        """ Set up the jet player. """
        self._constants = constants

        # Call the parent Sprite constructor
        super().__init__(filename, scale)

        # Info on where we are going.
        # Angle comes in automatically from the parent class.
        self.thrust = 0
        self.speed = 0
        self.max_speed = self._constants.MAX_SPEED
        self.drag = 0.05
        self.respawning = 0

        # Mark that we are respawning.
        self.respawn()

    def respawn(self):
        """
        Called when we die and need to make a new jet.
        'respawning' is an invulnerability timer.
        """
        # If we are in the middle of respawning, this is non-zero.
        self.respawning = 1
        self.center_x = self._constants.SCREEN_WIDTH / 2
        self.center_y = self._constants.SCREEN_HEIGHT / 2
        self.angle = 0

    def update(self):
        """
        Update our position and other particulars.
        """
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
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
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

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