"""11 Упражнение."""
import turtle


def main():
    """Главная функция."""
    draw_a_butterfly()
    input()


def draw_a_butterfly():
    """Отрисовка бабочки."""
    turtle.shape('turtle')
    turtle.speed(0)
    n = 5
    for i in range(5, n+5):
        draw_a_polygon(length=i, direction=0)
        draw_a_polygon(length=i, direction=1)


def draw_a_polygon(n=100, length=5, direction=0):
    """
    Отрисовка окружности.

    На вход дается количество вершин, длина грани и направление
    """
    corner = 360/n
    for i in range(n):
        turtle.forward(length)
        if direction == 0:
            turtle.left(corner)
        else:
            turtle.right(corner)


if __name__ == '__main__':
    main()
