import pygame, os

from src.settings import *

class Window:

    """
    This class represents the game window.
    It handles window initializationm drawing border, updating display and filling the window with colors.
    """

    def __init__(self, window_x: int, window_y: int):
        """
        Initializes the game window with the specified x and y values, it sets the title and icon for the window.

        Args:
            window_x (int): Window x value represented in integer.
            window_y (int): Window y value represented in integer.
        """

        self.window_x, self.window_y = window_x, window_y
        self.window = pygame.display.set_mode((window_x, window_y))
        pygame.display.set_caption('Snake')
        pygame.display.set_icon(pygame.image.load(os.getcwd() + "/assets/snake_logo.PNG"))

    def draw_border(self):
        """
        Draws a border around the window representing the game's walls.
        """
        pygame.draw.rect(self.window, BLUE, pygame.Rect(0, 20, self.window_x, self.window_y - 20), 10)

    def update(self):
        """
        Updates the display to make changes to the window surface. 
        """
        pygame.display.update()

    def fill(self, color: pygame.Color):
        """
        Fills the entire window with the specified color.

        Args:
            color (pygame.Color): Color object representing the color to fill the window with.
        """
        self.window.fill(color)