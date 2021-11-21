import arcade

#Game classes
from game.director import Director


def main():
    """ Start the game """
    
    Director().setup()
    arcade.run()


if __name__ == "__main__":
    main()
