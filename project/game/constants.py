import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Window
SCREEN_TITLE = "Jet Fighters - Beta Version"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = arcade.csscolor.CORNFLOWER_BLUE

# Screen limits
OFFSCREEN_SPACE = 80
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE

# JET Players
JET_SCALE = 0.25
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


# Bullet
BULLET_SCALE = 0.5
BULLET_SPEED = 19

# Enemy
ENEMY_SPEED = 1
ENEMY_LIVES = 1
STARTING_ENEMIES_COUNT = 5
MAX_ENEMIES_COUNT = 10
# Amount of fram between enemies shots
ENEMY_SHOOT_TIMER_RANGE = [30, 60]

#==== ASSETS
# Images
PLAYER1_IMG = "../assets/images/player1.png"
PLAYER2_IMG = "../assets/images/player2.png"
ENEMY_IMG = "../assets/images/enemy.png"
BULLET_IMG = "../assets/images/bullet.png"

# Sounds
BULLET_SOUND = arcade.load_sound("../assets/sounds/shoot1.wav")
ENEMY_DEAD_SOUND = arcade.load_sound("../assets/sounds/enemy_boom1.wav")
PLAYER_DEAD_SOUND = arcade.load_sound("../assets/sounds/boom1.wav")