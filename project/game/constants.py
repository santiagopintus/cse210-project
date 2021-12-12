import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Window
SCREEN_TITLE = "Jet Fighters - Beta Version"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#RGB bg color 
# BACKGROUND_COLOR = (6, 123, 194)
BACKGROUND_COLOR = (0, 100, 171)

# Screen limits
OFFSCREEN_SPACE = 80
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE
# Game
WIN_LEVEL = 11
GAME_WIN = 1 # The number indicates if the player won
GAME_OVER = 2 # The number indicates if the player loose


# Coordinates for GUI elements
SCORE_HEIGHT = SCREEN_HEIGHT - 28
LIVES_HEIGHT = SCREEN_HEIGHT - 52
RESPAWNING_HEIGHT = SCREEN_HEIGHT - 76
CURRENT_LEVEL_HEIGHT = SCREEN_HEIGHT - 180
P1_GUI_X = 10
P2_GUI_X = SCREEN_WIDTH - P1_GUI_X - 400

# JET Players
JET_SCALE = 0.25
LIVES_SCALE = 0.1
MAX_SPEED = 4
LIVES = 3
P1_X_POS = SCREEN_WIDTH / 3 * 2
P_Y_POS = SCREEN_HEIGHT / 2
P2_X_POS = SCREEN_WIDTH / 3

#===== PLAYERS CONTROLS
# Player 1
P1_UP = arcade.key.UP
P1_DOWN = arcade.key.DOWN
P1_LEFT = arcade.key.LEFT
P1_RIGHT = arcade.key.RIGHT
P1_SHOOT = arcade.key.RCTRL
P1_CONTROLS = [P1_UP, P1_DOWN, P1_LEFT, P1_RIGHT]
# Player 2
P2_UP = arcade.key.W
P2_DOWN = arcade.key.S
P2_LEFT = arcade.key.A
P2_RIGHT = arcade.key.D
P2_SHOOT = arcade.key.SPACE
P2_CONTROLS = [P2_UP, P2_DOWN, P2_LEFT, P2_RIGHT]

# Sprite lists names
PLAYERS_LIST_NAME = "Players"
P_BULLETS_LIST_NAME = "PlayerBullets"
ENEMIES_LIST_NAME = "Enemies"
E_BULLETS_LIST_NAME = "EnemyBullets"
EXPLOSIONS_LIST_NAME = "Explosions"
CLOUDS_LIST_NAME = "Clouds"

# Bullet
BULLET_SCALE = 0.5
BULLET_SPEED = 19
BULLET_SPEED_ENEMY = 4
# Amount of frames between enemies shots (The higher, the slower)
ENEMY_SHOOT_TIMER_RANGE = [60, 100]

# Enemy
ENEMY_SPEED = 1
ENEMY_LIVES = 1
POINTS_PER_KILL = 50
STARTING_ENEMIES_COUNT = 2
MAX_ENEMIES_COUNT = 8

#==== ASSETS
# Images
PLAYER1_IMG = "../assets/images/player1.png"
PLAYER2_IMG = "../assets/images/player2.png"
ENEMY_IMG = "../assets/images/enemy.png"
BULLET_IMG = "../assets/images/bullet.png"
# Adding 7 different clouds
CLOUDS_IMG = ["../assets/images/clouds/cloud1.png", "../assets/images/clouds/cloud2.png", "../assets/images/clouds/cloud3.png", "../assets/images/clouds/cloud4.png", "../assets/images/clouds/cloud5.png", "../assets/images/clouds/cloud6.png", "../assets/images/clouds/cloud7.png"]

# Clouds
CLOUDS_COUNT = 3
CLOUD_SCALE = [1, 2]
CLOUD_SPEED = [1, 2]

# Explosion images
EXPLOSION_IMG_LIST = []

columns = 16
count = 60
sprite_width = 256
sprite_height = 256
file_name = ":resources:images/spritesheets/explosion.png"

# Load the explosions from a sprite sheet
EXPLOSION_IMG_LIST = arcade.load_spritesheet(
    file_name, sprite_width, sprite_height, columns, count)

# Sounds
BULLET_SOUNDS = [arcade.load_sound("../assets/sounds/shoot1.wav"), arcade.load_sound("../assets/sounds/shoot2.wav"), arcade.load_sound("../assets/sounds/shoot3.wav"), arcade.load_sound("../assets/sounds/shoot4.wav")]
ENEMY_DEAD_SOUNDS = [arcade.load_sound("../assets/sounds/enemy_boom1.wav"), arcade.load_sound("../assets/sounds/enemy_boom2.wav")]
PLAYER_HIT_SOUND = arcade.load_sound("../assets/sounds/enemy_boom2.wav")
PLAYER_DEAD_SOUNDS = [arcade.load_sound("../assets/sounds/boom1.wav"), arcade.load_sound("../assets/sounds/boom2.wav")]

# Background music
BACKGROUND_SOUNDS = [
    arcade.load_sound("../assets/background_music/b_music.mp3", True), 
    arcade.load_sound("../assets/background_music/war_fx.mp3", True)
]

