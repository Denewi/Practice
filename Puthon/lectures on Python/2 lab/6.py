"""6 Упражнение."""
import turtle


def main():
    """Главная функция."""
    n = 12
    draw_a_paw(n)
    input()


def draw_a_paw(n, length=100):
    """
    Отрисовка паука.

    На вход дается количетво лапок и их длина
    """
    turtle.shape('turtle')
    corner = 360/n
    for i in range(n):
        turtle.right(corner)
        turtle.forward(length)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(length)
        turtle.left(180)


if __name__ == '__main__':
    main()
