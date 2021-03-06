"""Draw picture beach."""
import pygame
from pygame.draw import rect, circle, polygon, line
from random import randint

FPS = 30
SKY_BLUE = (117, 210, 253)
DEEP_BLUE = (0, 191, 255)
YELLOW = (255, 215, 0)
WHITE = (255, 255, 255)
BLACK = (90, 90, 90)
LIGHT_BROWN = (166, 64, 0)
BROWN = (65, 25, 0)
GREY = (230, 230, 200)
RED = (230, 76, 0)


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

    x_ship = width // 1.5
    y_ship = height // 2
    width_ship = 250
    height_ship = width_ship // 1.75
    draw_ship(x_ship, y_ship, width_ship, height_ship)

    x_umbrella = width // 6
    y_umbrella = height // 2
    height_umbrella = 150
    width_umbrella = height_umbrella // 1.05
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
    """Draw ship.

    x, y show position center up body ship
    """
    height_body_ship = height // 5
    draw_body_ship(x, y, width, height_body_ship)

    width_mast_ship = width // 3
    height_mast_ship = height - height_body_ship
    x_mast_ship = x - width // 5
    draw_mast_ship(x_mast_ship, y, width_mast_ship, height_mast_ship)


def draw_body_ship(x, y, width, height):
    """Draw body ship.

    x, y show position center up body ship
    """
    # Draw end ship
    radius_end = height
    x_end = x - width // 2 + radius_end
    circle(screen, LIGHT_BROWN, (x_end, y), radius_end, draw_bottom_left=True)
    circle(screen, BROWN, (x_end, y), radius_end, 1, draw_bottom_left=True)

    # Draw center ship
    width_center = (width - radius_end) // 1.4
    rect(screen, LIGHT_BROWN, (x_end, y, width_center, height))
    rect(screen, BROWN, (x_end, y, width_center, height), 1)

    # Draw start ship
    x_start = x_end + width_center
    y_start = y + height
    x_width_start = x_start + width - width_center - radius_end
    polygon(screen, LIGHT_BROWN, ([x_start, y], [x_width_start, y],
                                  [x_start, y_start]))
    polygon(screen, BROWN, ([x_start, y], [x_width_start, y],
                            [x_start, y_start]), 1)
    # Draw circle in start body
    radius_start = height // 4
    indent = radius_start // 1.5
    x_start_circle = x_start + indent + radius_start
    y_start_circle = y + indent + radius_start
    circle(screen, WHITE, (x_start_circle, y_start_circle), radius_start)
    indent_inside = int(radius_start // 3)
    circle(screen, BLACK, (x_start_circle, y_start_circle),
           radius_start, indent_inside)


def draw_mast_ship(x, y, width, height):
    """Draw mast ship.

    x, y show down point mast
    width show size pillar and sail
    """
    y_mast = y - height
    # Draw pillar
    width_pillar = width // 10
    line(screen, BLACK, [x, y],
                        [x, y_mast], width_pillar)

    # Draw sail
    x_sail_start = x + width_pillar // 2
    y_sail_start = y - height
    x_sail_mid = x_sail_start + width // 4
    y_sail_mid = y - height // 2
    x_sail_end = x_sail_start + width - width_pillar
    polygon(screen, GREY, ([x_sail_start, y_sail_start],
                           [x_sail_mid, y_sail_mid],
                           [x_sail_end, y_sail_mid]))
    polygon(screen, BLACK, ([x_sail_start, y_sail_start],
                            [x_sail_mid, y_sail_mid],
                            [x_sail_end, y_sail_mid]), 1)

    polygon(screen, GREY, ([x_sail_start, y],
                           [x_sail_mid, y_sail_mid],
                           [x_sail_end, y_sail_mid]))
    polygon(screen, BLACK, ([x_sail_start, y],
                            [x_sail_mid, y_sail_mid],
                            [x_sail_end, y_sail_mid]), 1)


def draw_umbrella(x, y, width, height):
    """Draw umdrella.

    x, y show point center up stick
    """
    # Draw canopy
    x_canopy_left = x - width // 2
    x_canopy_right = x + width // 2
    height_canopy = height // 5
    y_canopy = y + height_canopy
    polygon(screen, RED, ([x, y], [x_canopy_left, y_canopy],
                          [x_canopy_right, y_canopy]))

    # Draw line
    step = int(width // 7)
    for triangle in range(step, int(width), step):
        polygon(screen, BLACK, ([x, y], [x_canopy_left, y_canopy],
                                [x_canopy_left + triangle, y_canopy]), 1)

    # Draw stick
    width_stick = width // 15
    x_stick = x - width_stick // 2
    rect(screen, LIGHT_BROWN, (x_stick, y_canopy, width_stick, height))


if __name__ == '__main__':
    main()
