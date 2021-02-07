"""5 Упражнение."""
import turtle


def main():
    """Главная функция."""
    turtle.shape('turtle')
    length = 20
    indent = length/2
    for i in range(10):
        draw_a_square(length, indent)
        length += 2*indent
    input()


def draw_a_square(length, indent):
    """
    Отрисовка квадрта.

    На вход дается длина грани
    """
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.penup()
    turtle.goto(-length/2, -length/2)
    turtle.pendown()


if __name__ == '__main__':
    main()
