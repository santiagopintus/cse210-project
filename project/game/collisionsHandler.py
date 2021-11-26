import arcade

from game import constants

class CollisionsHandler():
    """ Class that handles the collisions between players, bullets, and enemies

        Attributes:
    """
    def __init__(self, scene):
        """ Initializes the class """
        self._scene = scene
        self._constants = constants

    def check_collisions(self):
        #Check for collisions if user is not respawning
        for player in self._scene["Players"]:
            if not player.is_respawning():
                #Check for collisions with enemies and their bullets
                enemies = arcade.check_for_collision_with_lists(
                    player, 
                    [self._scene[self._constants.ENEMIES_LIST_NAME], self._scene[self._constants.E_BULLETS_LIST_NAME]]
                    )
                if len(enemies) > 0:
                    for enemy in enemies:
                        player.respawn()
                        arcade.play_sound(self._constants.PLAYER_DEAD_SOUND)
                        arcade.play_sound(self._constants.ENEMY_DEAD_SOUND)
                        enemy.remove_from_sprite_lists()

        for bullet in self._scene["PlayerBullets"]:
            enemies_shooted = arcade.check_for_collision_with_list(bullet, self._scene["Enemies"])

            if len(enemies_shooted) > 0:
                for enemy in enemies_shooted:
                    arcade.play_sound(self._constants.ENEMY_DEAD_SOUND)
                    bullet.remove_from_sprite_lists()
                    enemy.remove_from_sprite_lists()