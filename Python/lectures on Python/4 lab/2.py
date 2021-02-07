"""Streaks with the help cycle."""
import pygame
from pygame.draw import rect, line


def main():
    """Start the main function."""
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((400, 400))

    x1 = 100
    y1 = 100
    x2 = 300
    y2 = 200
    N = 10
    color = (255, 255, 255)
    rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
    h = (x2 - x1) // (N + 1)
    x = x1 + h
    for i in range(N):
        line(screen, color, (x1, y1), (x2, y2))
        x += h

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


if __name__ == '__main__':
    main()
