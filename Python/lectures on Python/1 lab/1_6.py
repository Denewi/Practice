"""
1 лаба.

6 задание
"""
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Show grafics."""
    ax = axes3d.Axes3D(plt.figure())
    i = np.arange(-1, 1, 0.01)
    X, Y = np.meshgrid(i, i)
    Z = X**2 - Y**2
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    plt.show()


if __name__ == '__main__':
    main()
