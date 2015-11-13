# Credit to FB36 for base code.
# Written by VacRom

# Random, for determining an initial condition.
import random

# Our imaging tool.
from PIL import Image
# Dimensions of the image.
imgx = 800
imgy = 600
image = Image.new("RGB", (imgx, imgy))

# The number of iterations on our function.
maxIt = 60000
# Create an image after this many iterations.
frame = 500
# The size of our axis. We are plotting the projection of the system
# onto the x-y coordinate plane.
size = 30
xa = -size
xb = size
ya = -size
yb = size

# Initial conditions.
x = random.random() * size * 2 - 1
y = random.random() * size * 2 - 1
z = random.random() * size * 2 - 1

x2 = x+0.00002
y2 = y
z2 = z

x3 = x
y3 = y
z3 = z+0.00002

# The Lorenz equations:
# dx/dt = delta * (y - x)
# dy/dt = r * x - y - x * z
# dz/dt = x * y - b * z
delta = float(10)
r = float(28)
b = float(8) / 3
# Step size for our derivative.
h = 1e-3

def Lorenz(x, y, z):
    dx_dt = delta * (y - x)
    dy_dt = r * x - y - x * z
    dz_dt = x * y - b * z
    x += dx_dt * h
    y += dy_dt * h
    z += dz_dt * h
    return (x, y, z)

def Lorenz2(x2, y2, z2):
    dx_dt2 = delta * (y2 - x2)
    dy_dt2 = r * x2 - y2 - x2 * z2
    dz_dt2 = x2 * y2 - b * z2
    x2 += dx_dt2 * h
    y2 += dy_dt2 * h
    z2 += dz_dt2 * h
    return (x2, y2, z2)

def Lorenz3(x3, y3, z3):
    dx_dt3 = delta * (y3 - x3)
    dy_dt3 = r * x3 - y3 - x3 * z3
    dz_dt3 = x3 * y3 - b * z3
    x3 += dx_dt3 * h
    y3 += dy_dt3 * h
    z3 += dz_dt3 * h
    return (x3, y3, z3)

for i in range(maxIt):

    n = i/frame

    print(i, x, x2, x3)

    (x, y, z) = Lorenz(x, y, z)
    xi = int((imgx - 1) * (x - xa) / (xb - xa))
    yi = int((imgy - 1) * (y - ya) / (yb - ya))
    if xi >= 0 and xi < imgx and yi >= 0 and yi < imgy:
        image.putpixel((xi, yi), (255, 0, 0))

    (x2, y2, z2) = Lorenz2(x2, y2, z2)
    xj = int((imgx - 1) * (x2 - xa) / (xb - xa))
    yj = int((imgy - 1) * (y2 - ya) / (yb - ya))
    if xj >= 0 and xj < imgx and yj >= 0 and yj < imgy:
        image.putpixel((xj, yj), (0, 255, 0))

    (x3, y3, z3) = Lorenz3(x3, y3, z3)
    xk = int((imgx - 1) * (x3 - xa) / (xb - xa))
    yk = int((imgy - 1) * (y3 - ya) / (yb - ya))
    if xk >= 0 and xk < imgx and yk >= 0 and yk < imgy:
        image.putpixel((xk, yk), (0, 0, 255))

    if n == int(n):
        name = str(n)
        image.save(name, "PNG")
        n = n+1
        for c in range(imgx):
            for d in range(imgy):
                image.putpixel((c, d), (0, 0, 0))
