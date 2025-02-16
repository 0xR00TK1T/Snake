import pygame

class Snake:

    """
    This class represents the snake in the game.
    It manages the snake's position, movement, direction, body and collision detection.
    """

    def __init__(self):
        """
        Initializes the snake's position, body, and direction.

        Snake's initial position is at (100, 50) which is the x and y position on the screen,
        further the body consists of a list of segments. The snake starts by moving to the right.
        """
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.direction = 'RIGHT'

    def move(self):
        """
        Moves the snake in the current direction by updating its position and body.
        """
        direction_map = {'UP': (0, -10), 'DOWN': (0, 10), 'LEFT': (-10, 0), 'RIGHT': (10, 0)}
        self.position[0] += direction_map[self.direction][0] # x pos
        self.position[1] += direction_map[self.direction][1] # y pos
        self.body.insert(0, list(self.position))

    def check_collision(self, fruit_position = None):
        """
        Checks if the snake collides with itself or the fruit.

        Args:
            fruit_position (list or None): The position of the fruit to check for collision, default is None.

        Returns:
            bool: True if the snake collides with the fruit or itself, false otherwise. 
        """
        if fruit_position and self.position == fruit_position: return True
        if self.position in self.body[1:]: return True
        return False

    def change_direction(self, key: int):
        """
        Changes the direction of the snake based on a keypress only if it's a new direction.

        Args:
            key (int): The key event that indicates the new direction.
        """
        new_directions = {pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN', pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT'}
        new_direction = new_directions.get(key)

        if new_direction and (self.direction, new_direction) not in [('UP', 'DOWN'), ('DOWN', 'UP'), ('LEFT', 'RIGHT'), ('RIGHT', 'LEFT')]: self.direction = new_direction

    def reset(self):
        """
        Resets the snake to its initial state with the default position, body, and direction.

        This method is only used when it's time to reset the game.
        """
        self.__init__()