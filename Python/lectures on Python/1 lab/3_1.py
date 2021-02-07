"""
1 лаба.

3 задание
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
    return np.log((x**2 + 1) * np.exp(-np.abs(x)/10)) / np.log(1 + np.tan(1/(1 + np.sin(x)**2)))


if __name__ == '__main__':
    main()
