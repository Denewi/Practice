"""7 Упражнение."""
import turtle
import numpy


def main():
    """Главная функция."""
    draw_a_spiral()
    input()


def draw_a_spiral():
    """
    Отрисовка спирали.

    На вход дается количетво витков
    """
    turtle.shape('turtle')
    k = 1
    fi_radian = 0.2
    corner = fi_radian*(180/numpy.pi)
    for i in range(1000):
        r = k*fi_radian
        turtle.forward(r)
        turtle.left(corner)
        fi_radian += 0.2
        r += r


if __name__ == '__main__':
    main()
