import pygame

def main():
    x = 400
    y = 300
    pygame.init()
    screen = pygame.display.set_mode((x, y)).convert()
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
