import pygame

class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.direction = 'RIGHT'

    def move(self):
        direction_map = {'UP': (0, -10), 'DOWN': (0, 10), 'LEFT': (-10, 0), 'RIGHT': (10, 0)}
        self.position[0] += direction_map[self.direction][0] # x pos
        self.position[1] += direction_map[self.direction][1] # y pos
        self.body.insert(0, list(self.position))

    def check_collision(self, fruit_position = None):
        if fruit_position and self.position == fruit_position: return True
        if self.position in self.body[1:]: return True
        return False

    def change_direction(self, key):
        new_directions = {pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN', pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT'}
        new_direction = new_directions.get(key)

        if new_direction and (self.direction, new_direction) not in [('UP', 'DOWN'), ('DOWN', 'UP'), ('LEFT', 'RIGHT'), ('RIGHT', 'LEFT')]: self.direction = new_direction

    def reset(self):
        self.__init__()