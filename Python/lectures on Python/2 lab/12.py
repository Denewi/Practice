"""12 Упражнение."""
import turtle


def main():
    """Главная функция."""
    draw_a_spring()
    input()


def draw_a_spring():
    """Отрисовка пружины."""
    turtle.shape('turtle')
    turtle.speed(0)
    n = 3
    turtle.left(90)
    for i in range(n):
        draw_a_polygon(curvature=0)
        draw_a_polygon(length=1, curvature=1)


def draw_a_polygon(n=100, length=5, curvature=0):
    """
    Отрисовка полуогружности.

    На вход дается количество вершин, длина грани и направление
    """
    corner = 360/n
    for i in range(n//2):
        turtle.forward(length)
        if curvature == 0:
            turtle.right(corner)
        else:
            turtle.right(corner)


if __name__ == '__main__':
    main()
