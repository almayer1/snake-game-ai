import pygame
from game import settings
from game import render
from game.state import GameState
from game.logic import step, reset
from game.input import get_action

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    state = GameState(settings.SNAKE_STARTING, settings.DIRECTION_STARTING, settings.FOOD_STARTING)
    accum = 0
    pending_dir = None

    # Game loop
    running = True
    while running:
        dt = clock.tick(settings.FPS)
        accum += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                d = get_action(event.key)
                if d is not None:
                    pending_dir = d

        #update game state
        while accum >= settings.TICK_RATE and not state.game_over:
            state, done = step(state, pending_dir)
            pending_dir = None
            accum -= settings.TICK_RATE

        #draw 
        render.draw_background(screen)
        render.draw_snake(screen, state)
        render.draw_food(screen, state)

        #show frame
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
