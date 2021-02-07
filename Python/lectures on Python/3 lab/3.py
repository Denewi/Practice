"""Modeling a material point."""
import turtle
from random import uniform
import numpy as np


def main():
    """Start the main function."""
    turtle.shape('circle')
    turtle.speed(0)

    x = 0
    y = 0
    g = 9.8
    corner = np.radians(70)
    V = 50
    Vx = V*np.cos(corner)
    Vy = V*np.sin(corner)
    t = 0.05

    draw_earth()

    print(Vx, np.cos(corner))
    print(Vy, np.sin(corner))
    while Vx > 1:
        x += Vx*t
        y += Vy*t - g*t**2/2
        Vy -= g*t
        if y <= 0:
            y = 0
            Vy = -Vy * uniform(0.7, 0.8)
            Vx *= uniform(0.8, 0.9)
        turtle.goto(x, y)

    input()


def draw_earth():
    """Drawing earth."""
    turtle.goto(500, 0)
    turtle.goto(0, 0)


if __name__ == '__main__':
    main()
