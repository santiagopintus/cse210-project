import arcade
import random

from game import constants
from game.explosionSprite import ExplosionSprite

class CollisionsHandler():
    """ Class that handles the collisions between players, bullets, and enemies

        Attributes:
    """
    def __init__(self, scene):
        """ Initializes the class """
        self._scene = scene
        self._constants = constants
        self._explosion_sprite = None

    def setup(self):
        """ Sets up the class """
        self._explosion_sprite = ExplosionSprite

    def check_collisions(self):
        #Check for collisions if user is not respawning
        for player in self._scene[self._constants.PLAYERS_LIST_NAME]:
            if not player.is_respawning():
                #Check for collisions with enemies and their bullets
                enemies = arcade.check_for_collision_with_lists(
                    player, 
                    [self._scene[self._constants.ENEMIES_LIST_NAME], self._scene[self._constants.E_BULLETS_LIST_NAME]]
                    )
                if len(enemies) > 0:
                    for enemy in enemies:
                        enemy_dead_sound = random.choice(self._constants.ENEMY_DEAD_SOUNDS)
                        arcade.play_sound(enemy_dead_sound)
                        enemy.remove_from_sprite_lists()
                        # The enemy also explodes
                        self._explosion_sprite = ExplosionSprite(
                            self._constants.EXPLOSION_IMG_LIST,
                            .4
                        )
                        self._scene.add_sprite(
                            self._constants.EXPLOSIONS_LIST_NAME,
                            self._explosion_sprite
                        )
                        self._explosion_sprite.locate_explosion(enemy)
                        # The player get hit
                        player.increase_hit_count()

        #For each bullet, check for enemies shooted by the player
        for bullet in self._scene[self._constants.P_BULLETS_LIST_NAME]:
            enemies_shooted = arcade.check_for_collision_with_list(bullet, self._scene[self._constants.ENEMIES_LIST_NAME])

            # if there are enemies shooted
            if len(enemies_shooted) > 0:
                for enemy in enemies_shooted:
                    # Get the player that shot the bullet
                    players_list = self._scene[self._constants.PLAYERS_LIST_NAME]
                    player_number = bullet.get_bullet_id()
                    if player_number > 0:
                        if len(players_list) == 2:
                            players_list[player_number - 1].increase_score()
                        else:
                            players_list[0].increase_score()

                    # Make explosion
                    self._explosion_sprite = ExplosionSprite(
                        self._constants.EXPLOSION_IMG_LIST
                    )
                    self._scene.add_sprite(
                        self._constants.EXPLOSIONS_LIST_NAME, 
                        self._explosion_sprite
                    )
                    self._explosion_sprite.locate_explosion(enemy)

                    # Play sound of enemy being shooted
                    enemy_shooted_sound = random.choice(self._constants.ENEMY_DEAD_SOUNDS)
                    arcade.play_sound(enemy_shooted_sound)
                    # Remove bullet and enemy
                    bullet.remove_from_sprite_lists()
                    enemy.remove_from_sprite_lists()
