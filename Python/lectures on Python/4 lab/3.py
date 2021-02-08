"""Draw evil smiley."""
import pygame
from pygame.draw import rect


FPS = 30

YELLOW = (255, 211, 0)
RED = (255, 51, 51)
BLACK = (255, 255, 255)


def main():
    """Start the main function."""
    pygame.init()

    screen = pygame.display.set_mode((600, 600))

    size = 200
    x = 0
    y = 0

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        draw_smiley(x, y, size)

    pygame.quit()


def draw_smiley(x, y, size):
    """Draw smile.

    Location smile x, y in senter with diameter size.
    """
    draw_body(x, y, size)


def draw_body(x, y, size):
    """Draw body smiley."""


if __name__ == '__main__':
    main()
