"""Test create file on Pygame."""
import pygame


def main():
    """Start the main function."""
    pygame.init()  # init pygame

    # create screen
    screen = pygame.display.set_mode((300, 200))

    # Graw figure

    pygame.display.update()  # update screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == '__main__':
    main()
