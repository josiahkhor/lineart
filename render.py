import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, pi

def circle_points(r, n=100):
    return [(cos(2*pi/n*x)*r,sin(2*pi/n*x)*r, 2*pi/n*x) for x in range(0,n+1)]

def line_points(t, r, l=10):
    tt = t + pi/2
    p1 = (cos(t)*r + cos(tt)*l, sin(t)*r + sin(tt) * l)
    p2 = (cos(t)*r , sin(t)*r)
    p3 = (cos(t)*r - cos(tt)*l, sin(t)*r - sin(tt) * l)
    return [p1, p2, p3]

circle = circle_points(5)

x = [x for x, _ , _ in circle]
y = [y for _, y, _ in circle]

plt.plot(x, y, 'o')
for _, _, t in circle:
    line = line_points(t, 5)
    x = [x for x, _ in line]
    y = [y for _, y in line]
    plt.plot(x, y, '-')
plt.axes().set_aspect('equal','datalim')
plt.show()