"""4 Упражнение."""
import turtle


def main():
    """Главная функция."""
    turtle.shape('turtle')
    turtle.speed(100)
    draw_a_polygon(100, 10)
    input()


def draw_a_polygon(n, length=80):
    """
    Отрисовка многоугольника.

    На вход дается количество вершин
    """
    if n > 2:
        corner = 360/n
        for i in range(n):
            turtle.forward(length)
            turtle.left(corner)


if __name__ == '__main__':
    main()
