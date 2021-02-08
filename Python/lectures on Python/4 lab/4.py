"""Draw picture beach."""
import pygame
from pygame.draw import rect, circle

FPS = 30


screen = pygame.display.set_mode((600, 400))


def main():
    """Start the main function."""
    pygame.init()

    height = screen.get_height()
    width = screen.get_width()

    draw_fon(height, width)

    x_cloud = width // 4
    y_cloud = height // 8
    size_cloud = 10
    draw_cloud(x_cloud, y_cloud, size_cloud)

    x_sun = 7/8 * width
    y_sun = height // 7
    size_sun = 30
    draw_sun(x_sun, y_sun, size_sun)

    x_ship = width // 4
    y_ship = height // 8
    width_ship = width // 3
    height_ship = height // 4
    draw_ship(x_ship, y_ship, width_ship, height_ship)

    x_umbrella = width // 4
    y_umbrella = height // 10
    width_umbrella = width // 4
    height_umbrella = height // 3
    draw_umbrella(x_umbrella, y_umbrella, width_umbrella, height_umbrella)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_fon(height, width):
    """Draw sky, water and earth."""
    pass


def draw_cloud(x, y, size):
    """Draw cloud.

    size show radius circle.
    """
    pass


def draw_sun(x, y, size):
    """Draw sun.

    size show radius sun.
    """
    pass


def draw_ship(x, y, width, height):
    """Draw ship."""
    pass


def draw_umbrella(x, y, width, height):
    """Draw umdrella."""
    pass


if __name__ == '__main__':
    main()
