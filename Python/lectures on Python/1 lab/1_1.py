"""
1 лаба.

1 задание
"""
import numpy as np


def main():
    """Главная функция."""
    print(foo(1))
    print(foo(10))
    print(foo(100))


def foo(x):
    """Эта функция берет x и возвращает резульат выраженя."""
    return np.log((1/(np.e**(np.sin(x+1))))/(5/4 + 1/x**15)) / np.log(1 + x**2)


if __name__ == '__main__':
    main()
