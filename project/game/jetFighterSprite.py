import random
import arcade
import math
from game import constants
from game.explosionSprite import ExplosionSprite

class JetFighterSprite(arcade.Sprite):
    """
    Sprite that represents the jet fighter.

    Inherits from arcade.Sprite class
    """
    def __init__(self, filename, scale, scene, player_number = 1):
        """ Sets up the jet player. 
        
        Parameters:
            filename (str): The filename of the image to use for the jet.
            scale (float): The scale of the jet.
            player_number (int): The player number. (1 by default)
        """
        self._constants = constants

        # Call the parent Sprite constructor
        super().__init__(filename, scale)

        self._sprite_name = "Player"

        # GUI variables
        self._hits = 0
        self._lives = 3
        self._score = 0

        # Info on where we are going.
        # Angle comes in automatically from the parent class.
        self.thrust = 0
        self.speed = 0
        self._max_speed = self._constants.MAX_SPEED
        self.drag = 0.05
        self._respawning = 0
        self._player_number = player_number
        self._scene = scene
        self._explosion_sprite = ExplosionSprite

        # Mark that we are respawning.
        self.respawn()

    def respawn(self):
        """
        Called when we die and need to make a new jet.
        'respawning' is an invulnerability timer.
        """
        self._hits = 0
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
        # When player was damaged 3 times, he dies
        if self._hits == 3:
            self.decrease_lives()

        """ Call the parent class. """
        super().update()

    def get_sprite_name(self):
        """
        Returns the sprite name.
        """
        return self._sprite_name

    def get_player_number(self):
        """
        Returns the player number.
        """
        return self._player_number

    def get_score(self):
        """
        Returns the score.
        """
        return self._score
    
    def get_lives(self):
        """
        Returns the lives.
        """
        return self._lives

    def increase_score(self):
        """
        Increases the score.
        """
        self._score += self._constants.POINTS_PER_KILL
    
    def increase_hit_count(self):
        """
        Increases the hit count.
        """
        self._hits += 1
        arcade.play_sound(self._constants.PLAYER_HIT_SOUND)

    def decrease_lives(self):
        """
        Decreases the lives.
        """
        self._lives -= 1
        player_dead_sound = random.choice(self._constants.PLAYER_DEAD_SOUNDS)
        arcade.play_sound(player_dead_sound)

        # Make explosion
        self._explosion_sprite = ExplosionSprite(
            self._constants.EXPLOSION_IMG_LIST,
            1.5 # Scale (Bigger explosion)
        )
        self._scene.add_sprite(
            self._constants.EXPLOSIONS_LIST_NAME,
            self._explosion_sprite
        )
        self._explosion_sprite.locate_explosion(self)

        if self._lives == 0:
            # Game over (Remove player from screen)
            self.kill()
        else:
            self.respawn()
        
        if self._lives < 0:
            self._lives = 0
            