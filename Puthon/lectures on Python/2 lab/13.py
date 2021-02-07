"""13 Упражнение."""
import turtle
import numpy as np


def main():
    """Главная функция."""
    radius = 100
    draw_a_spring(radius)
    input()


def draw_a_spring(radius):
    """
    Отрисовка смайлика.

    На вход дается радиус смайла
    """
    turtle.shape('turtle')
    turtle.speed(0)

    move_turtle(radius, 0, 90)
    draw_a_face(radius)

    move_turtle(radius/2.5, radius/3, 270)
    draw_eyes(radius)

    move_turtle(0, radius/10, 270)
    draw_a_nose(radius)

    move_turtle(-radius/2, -radius/4)
    draw_a_mouth(radius)

    move_turtle()


def move_turtle(x=0, y=0, corner=0):
    """Функция пермещения черепашки."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.left(corner)
    turtle.pendown()


def draw_a_face(radius):
    """Отрисовка лица."""
    turtle.begin_fill()
    draw_a_circle(radius)
    turtle.fillcolor("Yellow")
    turtle.end_fill()
    turtle.fillcolor("black")


def draw_eyes(radius):
    """Отрисовка глаз."""
    radius_eyes = radius/7

    turtle.begin_fill()
    draw_a_circle(radius_eyes)
    move_turtle(-radius/2.5, radius/3)
    draw_a_circle(radius_eyes)
    turtle.fillcolor("blue")
    turtle.end_fill()
    turtle.fillcolor("black")


def draw_a_nose(radius):
    """Отрисовка носа."""
    turtle.pensize(radius/10)
    turtle.forward(radius/4)
    turtle.pensize(1)


def draw_a_mouth(radius):
    """Отрисовка рта."""
    turtle.pensize(radius/10)
    turtle.color("red")
    draw_arc(radius/2)
    turtle.color("black")
    turtle.pensize(1)


def draw_a_circle(radius):
    """
    Отрисовка окружности.

    На вход дается радиус окружности
    """
    circumference = 2*np.pi*radius  # Расчет длины окружности
    n = 100  # Количество вершин
    length = circumference/n  # Длина ребра
    corner = 360/n  # Угол поворота
    for i in range(n):
        turtle.left(corner)
        turtle.forward(length)


def draw_arc(radius):
    """
    Отрисовка полуокружности.

    На вход дается радиус окружности
    """
    circumference = 2*np.pi*radius  # Расчет длины окружности
    n = 100  # Количество вершин
    length = circumference/n  # Длина ребра
    corner = 360/n  # Угол поворота
    for i in range(n//2):
        turtle.left(corner)
        turtle.forward(length)


if __name__ == '__main__':
    main()
