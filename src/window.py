import pygame

from src.settings import *

class Window:
    def __init__(self, window_x: int, window_y: int):
        self.window_x, self.window_y = window_x, window_y
        self.window = pygame.display.set_mode((window_x, window_y))
        pygame.display.set_caption('Snake')

    def draw_border(self):
        pygame.draw.rect(self.window, BLUE, pygame.Rect(0, 20, self.window_x, self.window_y - 20), 10)

    def update(self):
        pygame.display.update()

    def fill(self, color):
        self.window.fill(color)