"""5 Упражнение."""
import turtle


def main():
    """Главная функция."""
    turtle.shape('turtle')
    length = 10
    step = 5
    n = 10
    draw_a_square_spiral(n, length, step)
    input()


def draw_a_square_spiral(n, length, step):
    """
    Отрисовка квадратной спирали.

    На вход дается количество квадратов, начальная длина и прирост
    """
    for i in range(n*4):
        turtle.forward(length)
        turtle.left(90)
        length += step


if __name__ == '__main__':
    main()
