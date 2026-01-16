import pygame
from .logic import UP, DOWN, LEFT, RIGHT

def get_action(key:int):
    if key == pygame.K_UP:
        return UP
    if key == pygame.K_RIGHT:
        return RIGHT
    if key == pygame.K_DOWN:
        return DOWN
    if key == pygame.K_LEFT:
        return LEFT
    return None