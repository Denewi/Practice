"""
1 лаба.

2 задание
"""
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Show grafics."""
    x = np.arange(-10, 10.01, 0.01)
    plt.figure(figsize=(10, 5))
    plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
    plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
    plt.plot(x, -x, label=r'$f_3(x)=-x$')
    plt.xlabel(r'$x$', fontsize=14)
    plt.xlabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.savefig('figure_with_legend.png')
    plt.show()


if __name__ == '__main__':
    main()
