"""Draw picture beach."""
import pygame
from pygame.draw import rect, circle
from random import randint

FPS = 30
SKY_BLUE = (117, 210, 253)
DEEP_BLUE = (0, 191, 255)
YELLOW = (255, 215, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((600, 400))


def main():
    """Start the main function."""
    pygame.init()

    height = screen.get_height()
    width = screen.get_width()

    draw_fon(height, width)

    x_cloud = width // 4
    y_cloud = height // 8
    width_cloud = 100
    height_cloud = width_cloud // 3
    draw_cloud(x_cloud, y_cloud, width_cloud, height_cloud)

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
    height_sky = height / 2.5
    rect(screen, SKY_BLUE, (0, 0, width, height_sky))

    y_water = height_sky
    height_water = (height - height_sky) // 2.5
    rect(screen, DEEP_BLUE, (0, y_water, width, height_water))

    y_earht = y_water + height_water
    height_earth = height - height_sky - height_water
    rect(screen, YELLOW, (0, y_earht, width, height_earth))


def draw_cloud(x, y, width_cloud, height_cloud):
    """Draw cloud.

    x, y show up left corner
    size show width cloud.
    """
    for circle_ in range(15):
        circle(screen, WHITE,
            (randint(x + height_cloud//2, x + width_cloud - height_cloud//2),
             randint(y + height_cloud//2, y + height_cloud - height_cloud//2)),
             randint(height_cloud//3, height_cloud//2))


def draw_sun(x, y, size):
    """Draw sun.

    size show radius sun.
    """
    circle(screen, YELLOW, (x, y), size)


def draw_ship(x, y, width, height):
    """Draw ship."""
    pass


def draw_umbrella(x, y, width, height):
    """Draw umdrella."""
    pass


if __name__ == '__main__':
    main()
