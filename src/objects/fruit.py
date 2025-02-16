import random

class Fruit:
    """
    This class represents the fruit in the game, it manages the fruit's
    position and spawning.
    """

    def __init__(self, window_x: int, window_y: int):
        """
        Initializes the Fruit object with a random position whitin the game area.

        Args:
            window_x (int): Window x value represented in integer.
            window_y (int): Window y value represented in integer.
        """
        self.window_x, self.window_y = window_x, window_y
        self.position = [random.randrange(1, (self.window_x//10) - 1) * 10, random.randrange(3, (self.window_y//10) - 1) * 10]
        self.spawned = True

    def spawn(self):
        """
        Spawns the fruit at a new random position within the game window.
        """
        self.position = [random.randrange(1, (self.window_x // 10) - 1) * 10, random.randrange(3, (self.window_y // 10) - 2) * 10]
        self.spawned = True