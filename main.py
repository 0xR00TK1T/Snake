from src.game import *

pygame.init()
fps = pygame.time.Clock()

def main():
    game = Game()
    
    while True:
        game.handle_events()
        game.update()
        fps.tick(15)

if __name__ == '__main__':
    main()