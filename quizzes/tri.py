'''Plot the function $f(x) = x^2$ for integer values of x
ranging from 0 inclusive to 10 exclusive.'''

import pylab as pl
x = [0, 2, 4, 6, 8]
fx = [0, 0, 0, 0, 0]
fy = [0, 1, 2, 3, 4]
fz = [4, 3, 2, 1, 0]
fa = [3, 2, 1, 0, 0]
fb = [0, 0, 1, 2, 3]
fc = [1, 1, 1, 1, 1]
fd = [1.5, 1.5, 1.5, 1.5, 1.5]
pl.plot(x, fx)
pl.plot(x, fy)
pl.plot(x, fz)
pl.plot(x, fa)
pl.plot(x, fb)
pl.plot(x, fc)
pl.plot(x, fd)
pl.show()
