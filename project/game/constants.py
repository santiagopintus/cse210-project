import arcade

# JET Player
JET_SCALE = 0.25
MAX_SPEED = 4
LIVES = 3

# Bullet
BULLET_SCALE = 0.5
BULLET_SPEED = 19

# Enemy
ENEMY_SPEED = 1
ENEMY_LIVES = 1
STARTING_ENEMIES_COUNT = 5

# Window
SCREEN_TITLE = "Jet Fighters - Alpha Version"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = arcade.csscolor.CORNFLOWER_BLUE

# Screen limits
OFFSCREEN_SPACE = 300
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE

# Clouds
# CLOUD_SPEED = [1, 5]
# CLOUD_SCALE = [0.25, 1]

#==== ASSETS
# Images
PLAYER1_IMG = "../assets/images/player.png"
ENEMY_IMG = "../assets/images/enemy.png"
BULLET_IMG = "../assets/images/bullet.png"

# Sounds
BULLET_SOUND = arcade.load_sound("../assets/sounds/shoot1.wav")
ENEMY_DEAD_SOUND = arcade.load_sound("../assets/sounds/enemy_boom1.wav")
PLAYER_DEAD_SOUND = arcade.load_sound("../assets/sounds/boom1.wav")
