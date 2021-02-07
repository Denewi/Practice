"""Drawing an Index."""
import turtle


def main():
    """Start the main function."""
    turtle.shape('turtle')
    turtle.speed(0)
    turtle.color('blue')
    turtle.pensize(4)

    t1 = (0, 100)
    t2 = (50, 100)
    t3 = (0, 50)
    t4 = (50, 50)
    t5 = (0, 0)
    t6 = (50, 0)

    n = -300

    numbers = [
        (t6, t2, t1, t5, t6),                      # 0
        (t6, t2, t3, t2, t6),                      # 1
        (t6, t5, t4, t2, t1, t2, t4, t5),          # 2
        (t5, t4, t3, t2, t1, t2, t3, t4, t5),      # 3
        (t6, t2, t4, t3, t1, t3, t4, t6),          # 4
        (t5, t6, t4, t3, t1, t2, t1, t3, t4, t6),  # 5
        (t5, t6, t4, t3, t2, t3, t5),              # 6
        (t5, t3, t2, t1, t2, t3, t5),              # 7
        (t5, t6, t2, t1, t3, t4, t3, t5),          # 8
        (t5, t6, t2, t1, t3, t4, t6),              # 9
    ]
    index = '1234567890'
    for i, num in enumerate(index):
        print(i)
        num = int(num)
        for move in numbers[num]:
            turtle.goto(move[0] + i*70 + n, move[1])

    input()


if __name__ == '__main__':
    main()
