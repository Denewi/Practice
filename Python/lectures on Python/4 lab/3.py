"""Draw evil smiley."""
import pygame
from pygame.draw import rect, line, circle


FPS = 30

BACKGROUND = (242, 255, 255)
YELLOW = (255, 211, 0)
RED = (255, 51, 51)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((600, 600))
screen.fill(BACKGROUND)


def main():
    """Start the main function."""
    pygame.init()

    size = 200
    # Point in center screen
    x = screen.get_width() // 2
    y = screen.get_height() // 2

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
    size_body = size // 2
    draw_body(x, y, size_body)

    y_eyes = y - size // 8
    draw_eyes(x, y_eyes, size)

    y_mouth = y + 1/5 * size
    size_mouth_w = 3/4 * size
    size_mouth_h = 1/8 * size
    draw_mouth(x, y_mouth, size_mouth_w, size_mouth_h)


def draw_body(x, y, size):
    """Draw body smiley."""
    circle(screen, YELLOW, (x, y), size)
    circle(screen, BLACK, (x, y), size, 1)


def draw_eyes(x, y, size):
    """Draw eyes and eyebrows smiley.

    x, y show on point between eyes.
    """


def draw_mouth(x, y, width, height):
    """Draw mouth.

    x, y show center mouth.
    width, height show size mouth.
    """
    rect(screen, BLACK, (x, y, width//3, height))
    rect(screen, BLACK, (x-width//3, y, width//3, height))


if __name__ == '__main__':
    main()
