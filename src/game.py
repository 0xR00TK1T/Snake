import pygame

from src.window import *
from src.objects.snake import *
from src.objects.fruit import *
from src.settings import *

class Game:
    def __init__(self):
        self.snake, self.fruit, self.score = Snake(), Fruit(window_x, window_y), 0
        self.window = Window(window_x, window_y)

    def show_score(self):
        font = pygame.font.SysFont('Comic Sans', 20)
        score_surface = font.render(f'Score : {self.score}', True, WHITE)
        self.window.window.blit(score_surface, score_surface.get_rect(center=(window_x // 2, 10)))

    def game_over(self):
        font = pygame.font.SysFont('Comic Sans', 50)
        self.window.fill(BLACK)

        #game_over_surface = font.render('Game Over!', True, RED)
        score_text = font.render(f'Your Score is : {self.score}', True, WHITE)
        
        self.window.window.blit(score_text, score_text.get_rect(midtop=(window_x / 2, window_y / 4)))
        self.window.update()
        
        pygame.time.delay(3000)
        
        self.snake.reset()
        self.score = 0

        #pygame.quit()
        #quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == pygame.KEYDOWN: self.snake.change_direction(event.key)

    def update(self):
        self.snake.move()

        if self.snake.check_collision(self.fruit.position):
            self.score += 1
            self.fruit.spawned = False
        else:
            self.snake.body.pop()

        if not self.fruit.spawned: self.fruit.spawn()

        if self.snake.position[0] < 10 or self.snake.position[0] >= window_x - 10 or self.snake.position[1] < 30 or self.snake.position[1] >= window_y - 10 or self.snake.check_collision(): self.game_over()

        self.window.fill(BLACK)
        self.window.draw_border()

        for pos in self.snake.body: pygame.draw.rect(self.window.window, GREEN, pygame.Rect(pos[0], pos[1], 12, 12))

        pygame.draw.rect(self.window.window, WHITE, pygame.Rect(self.fruit.position[0], self.fruit.position[1], 12, 12))

        self.show_score()
        self.window.update()