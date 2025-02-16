from src.game import *

# Initializes the pygame module
pygame.init()

# Sets the frames per second clock for the game loop
fps = pygame.time.Clock()

def main():
    """
    Main function that initializes the game and runs it in the loop.

    It creates an instance of the Game class and enters an infinite loop
    where the game is updated, and the FPS is controlled to ensure the
    game runs at a speed of 15 frames per second.
    """
    game = Game()
    
    while True:
        game.update()
        fps.tick(15)

if __name__ == '__main__':
    """
    Entry point of the game, and calls the main function.
    """
    main()