"""
1 лаба.

5 задание
"""
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Show grafics."""
    t = np.arange(0, 2*np.pi, 0.01)
    r = 4
    plt.plot(r*np.sin(t), r*np.cos(t), lw=3)
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    main()
