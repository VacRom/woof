'''Plot the function $f(x) = x^2$ for integer values of x
ranging from 0 inclusive to 10 exclusive.'''

import pylab as pl
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
fx = [0, -1, 4, -9, 16, -25, 36, -49, 64, -81, 100, -121, 144, -169]
fy = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
fz = [0, -1, -4, -9, -16, -25, -36, -49, -64, -81, -100, -121, -144, -169]
pl.plot(x, fx)
pl.plot(x, fy)
pl.plot(x, fz)
pl.show()
