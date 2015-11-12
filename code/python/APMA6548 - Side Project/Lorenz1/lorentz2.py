import random
from PIL import Image
imgx = 800
imgy = 600
image = Image.new("RGB", (imgx, imgy))

maxIt = 20000
frame = 250
maxPic = int(maxIt//frame)
size = 30
xa = -size
xb = size
ya = -size
yb = size

# initial state
x = random.random() * size * 2 - 1
y = random.random() * size * 2 - 1
z = random.random() * size * 2 - 1

# dx/dt = delta * (y - x)
# dy/dt = r * x - y - x * z
# dz/dt = x * y - b * z
delta = float(10)
r = float(28)
b = float(8) / 3
h = 1e-3

def Lorenz(x, y, z):
    dx_dt = delta * (y - x)
    dy_dt = r * x - y - x * z
    dz_dt = x * y - b * z
    x += dx_dt * h
    y += dy_dt * h
    z += dz_dt * h
    return (x, y, z)

c = 0
d = 0

for i in range(maxIt):
    n = i/frame
    print(n, i, frame, maxPic, c, d)
    (x, y, z) = Lorenz(x, y, z)
    xi = int((imgx - 1) * (x - xa) / (xb - xa))
    yi = int((imgy - 1) * (y - ya) / (yb - ya))
    if xi >= 0 and xi < imgx and yi >= 0 and yi < imgy:
        image.putpixel((xi, yi), (255, 100, 100))
    if n == int(n):
        name = str(n)
        image.save(name, "JPEG")
    if n == maxPic:
        quit
    if type(i/frame) == int:
        n = n+1
        for c in range(imgx):
            for d in range(imgy):
                image.putpixel((c, d), (0, 0, 0))
