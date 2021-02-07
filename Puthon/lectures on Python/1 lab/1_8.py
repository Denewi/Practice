"""
1 лаба.

8 задание
"""
import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy


def main():
    """Show grafics."""
    x, y, z = makeData()

    fig = pylab.figure()
    axes = Axes3D(fig)
    axes.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.jet)
    pylab.show()


def makeData():
    """Определение x, y, z."""
    x = numpy.arange(-10, 10, 0.01)
    y = numpy.arange(-10, 10, 0.01)
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = numpy.sin(xgrid)*numpy.sin(ygrid)/(xgrid*ygrid)
    return xgrid, ygrid, zgrid


if __name__ == '__main__':
    main()
