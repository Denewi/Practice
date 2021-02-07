"""14 Упражнение."""
import turtle
import numpy as np


def main():
    """Главная функция."""
    n = 5
    size = 100
    draw_a_star(n, size)
    input()


def draw_a_star(n, size):
    """
    Отрисовка звезды.

    На вход нается n вершин и размер звезды
    """
    turtle.shape('turtle')
    turtle.speed(1)


    move_turtle(size, corner)

    for side in range(n):
        turtle.forward(length)
        turtle.left(180-corner)


def move_turtle(size, corner):
    """Перемещение черепашки в верхнюю точку."""
    turtle.penup()
    turtle.goto(0, size/2)
    turtle.right(90 + corner/2)
    turtle.pendown()


if __name__ == '__main__':
    main()
