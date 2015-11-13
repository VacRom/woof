# Essentially the same as the other program, except that this acts as
# an 'overlay' to show stability over time.

import random
from PIL import Image, ImageDraw
scale = 3
x = 2000 * scale
y = 1081
image = Image.new("RGB", (x, y))
draw = ImageDraw.Draw(image)
draw.line((1, 1, x, 1), fill=(255, 255, 255))
draw.line((1, 1, 1, y), fill=(255, 255, 255))
a = 1
while a < x:
    draw.line((a, 1, a, y), fill=(64, 64, 64))
    a = a + scale * 100
a = 1
while a < x:
    draw.line((a, 1, a, y), fill=(255, 102, 102))
    a = a + scale * 500
a = 1
while a < x:
    draw.line((1, a, x, a), fill=(64, 64, 64))
    a = a + 108
lb = 0.0
ub = 4.0
ite = 50000
for a in range(x):
    l = lb + (ub - lb) * float(a) / (x - 1)
    f = random.random()
    print(a)
    for b in range(ite):
        f = l * f * (1 - f)
        if b < 33:
            image.putpixel((a, int(f * y)), (0, 0, 255))
        if b > (ite - 1000) and b < (ite - 32):
            image.putpixel((a, int(f * y)), (0, 255, 0))
        if b > (ite - 33):
            image.putpixel((a, int(f * y)), (255, 0, 0))

image.save("bif.png", "PNG")
