import pygame
from game import settings

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)).convert()
    pygame.display.set_caption("Hello Pygame")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    


    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
