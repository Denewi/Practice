"""Draw evil smiley."""
import pygame
from pygame.draw import rect, line, circle


FPS = 30

YELLOW = (255, 211, 0)
RED = (255, 51, 51)
BLACK = (255, 255, 255)

screen = pygame.display.set_mode((600, 600))


def main():
    """Start the main function."""
    pygame.init()

    size = 200
    x = 300
    y = 300

    draw_smiley(x, y, size)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_smiley(x, y, size):
    """Draw smile.

    Location smile x, y in senter with diameter size.
    """
    draw_body(x, y, size)


def draw_body(x, y, size):
    """Draw body smiley."""
    circle(screen, YELLOW, (x, y), size)


if __name__ == '__main__':
    main()
