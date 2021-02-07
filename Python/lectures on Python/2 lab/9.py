"""9 Упражнение."""
import turtle
import numpy as np


def main():
    """Главная функция."""
    for i in range(3, 13):
        draw_a_polygon(i, i*7)
    input()


def draw_a_polygon(n, length=100):
    """
    Отрисовка многоугольника.

    На вход дается количество вершин и длина грани
    """
    move_a_turtle(n, length)
    turtle.shape('turtle')
    turtle.speed(100)
    corner = 360/n
    turtle.left((180 - corner)/2)
    for i in range(n):
        turtle.left(corner)
        turtle.forward(length)
    turtle.right((180 - corner)/2)


def move_a_turtle(n, length):
    """Перемещение черепашки."""
    turtle.penup()
    turtle.goto(length/(2*np.sin(np.pi/n)), 0)
    turtle.pendown()


if __name__ == '__main__':
    main()
