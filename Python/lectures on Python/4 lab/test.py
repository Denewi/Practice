"""Test create file on Pygame."""
import pygame
from pygame.draw import *


def main():
    """Start the main function."""
    pygame.init()  # init pygame

    # Create screen
    screen = pygame.display.set_mode((300, 200))

    # Create delay for event
    clock = pygame.time.Clock()

    # Graw figure

    pygame.display.update()  # update screen

    # Main cycle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                clock.tick(30)


if __name__ == '__main__':
    main()
