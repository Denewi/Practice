"""10 Упражнение."""
import turtle


def main():
    """Главная функция."""
    draw_a_flower()
    input()


def draw_a_flower():
    """Отрисовка цветка."""
    turtle.shape('turtle')
    turtle.speed(0)
    n = 5
    corner = 180/n
    for i in range(n):
        draw_a_polygon(direction=0)
        draw_a_polygon(direction=1)
        turtle.left(corner)


def draw_a_polygon(n=100, length=5, direction=0):
    """
    Отрисовка окружности.

    На вход дается количество вершин и длина грани
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
