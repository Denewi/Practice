"""
1 лаба.

2 задание
"""
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Главная функция."""
    x = np.arange(-10, 10.01, 0.01)
    plt.figure(figsize=(10, 5))
    plt.plot(x, foo(x))
    plt.grid(True)
    plt.show()


def foo(x):
    """Эта функция берет x и возвращает резульат выраженя."""
    return x**2 - x - 6


if __name__ == '__main__':
    main()
