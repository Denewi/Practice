"""
1 лаба.

3 задание
"""
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Show grafics."""
    x = np.arange(-10, 10.01, 0.01)
    t = np.arange(-10, 11, 1)

    subplot_1(x)  # subplot 1
    subplot_2(x)  # subplot 2
    subplot_3(x, t)  # subplot 3
    subplot_4(x)  # subplot 4

    plt.show()


def subplot_1(x):
    """Отрисовка 1 графика."""
    plt.subplot(221)
    plt.plot(x, np.sin(x))
    plt.title(r'$\sin(x)$')
    plt.grid(True)


def subplot_2(x):
    """Отрисовка 2 графика."""
    plt.subplot(222)
    plt.plot(x, np.cos(x), 'g')
    plt.axis('equal')
    plt.title(r'$\cos(x)$')


def subplot_3(x, t):
    """Отрисовка 3 графика."""
    plt.subplot(223)
    plt.plot(x, x**2, t, t**2, 'ro')
    plt.title(r'$x^2$')


def subplot_4(x):
    """Отрисовка 4 графика."""
    sp = plt.subplot(224)
    plt.plot(x, x)
    sp.spines['left'].set_position('center')
    sp.spines['bottom'].set_position('center')
    plt.title(r'$x$')


if __name__ == '__main__':
    main()
