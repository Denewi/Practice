"""Modeling of Brownian motion."""
import turtle
from random import randint


def main():
    """Start the main function."""
    turtle.shape('turtle')
    turtle.speed(0)
    while 1:
        turtle.left(randint(0, 360))
        turtle.forward(randint(0, 30))
    input()


if __name__ == '__main__':
    main()
