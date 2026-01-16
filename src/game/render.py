from . import settings
from .state import GameState
import pygame

def draw_snake(screen, state):
    cell_size = settings.CELL_SIZE
    color = settings.SNAKE_COLOR
    for (x, y) in state.snake:
        rect = pygame.Rect(
            x * cell_size,
            y * cell_size,
            cell_size,
            cell_size
        )
        pygame.draw.rect(screen, color, rect)

def draw_food(screen, state):
    cell_size = settings.CELL_SIZE
    color = settings.FOOD_COLOR
    x, y = state.food
    cx = x * cell_size + cell_size // 2
    cy = y * cell_size + cell_size // 2
    radius = cell_size // 2 + settings.FOOD_RADIUS_ADJUSTMENT
    pygame.draw.circle(screen, color, (cx, cy), radius)

def draw_background(screen):
    color = settings.LIGHT_TILE_COLOR
    for y in range(settings.GRID_HEIGHT):
        for x in range(settings.GRID_WIDTH):
            if (x + y) % 2 == 0:
                color = settings.LIGHT_TILE_COLOR
            else:
                color = settings.DARK_TILE_COLOR
            rect = pygame.Rect(x * settings.CELL_SIZE, y * settings.CELL_SIZE, settings.CELL_SIZE, settings.CELL_SIZE)
            pygame.draw.rect(screen, color, rect)


def draw_ui(screen, state):
    pass