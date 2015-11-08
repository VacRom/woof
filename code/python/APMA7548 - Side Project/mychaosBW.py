# Importing Image tools from Python Imaging Library (PIL)
import random
from PIL import Image, ImageDraw

# Resolution of the image, x by y pixels. Scaling the graph with a
# factor larger than 1 will increase the accuracy of the map. By
# default, it is set to 1.
scale = 2
x = 2000 * scale
y = 1081

# This is the command for generating an image based on a RGB color and
# the given coordinates.
image = Image.new("RGB", (x, y))

draw = ImageDraw.Draw(image)
# The lambda and x-axis.
draw.line((1, 1, x, 1), fill=(255, 255, 255))
draw.line((1, 1, 1, y), fill=(255, 255, 255))


# Vertical tick marks.
a = 1
# Small intervals with step size dl = 0.2.
while a < x:
    draw.line((a, 1, a, y), fill=(64, 64, 64))
    a = a + scale * 100

a = 1
# Large intervals with step size dl = 1.0.
while a < x:
    draw.line((a, 1, a, y), fill=(255, 102, 102))
    a = a + scale * 500

# Horizontal tick marks.
a = 1
# Small intervals with step size dx = 0.1
while a < x:
    draw.line((1, a, x, a), fill=(64, 64, 64))
    a = a + 108
# Set lower bound and upper bound for the horizontal
# axis i.e. parameter lambda, l. We shall take l between 0.0 and 4.0.
lb = 0.0
ub = 4.0

# Number of iterations for the function. The larger, the better. Set
# at a value at least 1000.
ite = 50000

# Note that when the resolution is large then there is a greater
# likelyhood of having 'gaps' at the bifurcation points.

# a is the value of the current x-pixel.
for a in range(x):
    # Determine the value of lambda with the lower bound, upper-bound,
    # and the current position of the x-pixel.
    l = lb + (ub - lb) * float(a) / (x - 1)
    # We give a random initial condition, x_0, between [0,1). Note
    # that if, by chance, f is equal to 0, we arrive are stuck at the
    # stable solution (0,0).
    f = random.random()
    # Prints the current value of the x-pixel so that we can tell how
    # far the program has generated an image.
    print(a)
    # Now we take a fixed a, a random x_0, and now we iterate the fucntion.
    for b in range(ite):
        f = l * f * (1 - f)
        # Only plot the last few iterations onto the map. Say, the
        # last 1000 iterations.
        if b > (ite - 1000):
            # Plot the last thousand pointS.
            image.putpixel((a, int(f * y)), (255, 255, 255))
image.save("bifBW.png", "PNG")
