import random

class Fruit:
    def __init__(self, window_x: int, window_y: int):
        self.window_x, self.window_y = window_x, window_y
        self.position = [random.randrange(1, (self.window_x//10) - 3) * 10, random.randrange(2, (self.window_y//10) - 1) * 10]
        self.spawned = True

    def spawn(self):
        self.position = [random.randrange(1, (self.window_x // 10) - 3) * 10, random.randrange(2, (self.window_y // 10) - 2) * 10]
        self.spawned = True