from .state import GameState
from . import settings
import random

#Directions
UP = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)
DOWN = (0, 1)


def reset() -> GameState:
    snake = settings.SNAKE_STARTING
    direction = settings.DIRECTION_STARTING
    food = settings.FOOD_STARTING
    return GameState(
        snake = snake,
        direct = direction,
        food = food,
        score = 0,
        game_over = False
    )

def step(state, action) -> tuple[GameState, bool]:
    #check if game_over
    if (state.game_over):
        return state, True
    #find out new direction
    state.direction = set_direction(state.direction, action)
    #calculate new position based on direction
    head_x, head_y = state.snake[0]
    dx, dy = state.direction
    new_head = (head_x + dx, head_y + dy)
    #check if collision
    if hit_self(new_head, state.snake) or hit_wall(new_head):
        return state, True
    #move
    state.snake.insert(0, new_head)
    #update food
    if (new_head == state.food):
        state.score += 1
        state.food = spawn_food(state.snake)
    else:
        state.snake.pop()
    return state, False

#takes current direction and finds new direction based on action
def set_direction(current, new):
    if new is None:
        return current
    if current[0] == -new[0] and current[1] == -new[1]:
        return current
    return new

def hit_self(new_head, snake) -> bool:
    return new_head in snake

def hit_wall(new_head) -> bool:
    x, y = new_head
    if x < 0 or x >= settings.GRID_WIDTH or y < 0 or y >= settings.GRID_HEIGHT:
        return True
    return False

def spawn_food(snake):
    empty = [
        (x, y)
        for y in range(settings.GRID_HEIGHT)
        for x in range(settings.GRID_WIDTH)
        if (x, y) not in snake
    ]
    return random.choice(empty)