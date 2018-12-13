import matplotlib.pyplot as plt
import numpy as np
from matplotlib.transforms import Bbox
from math import cos, sin, pi

black = '#000000'
blue = '#0000ff'
green = '#00b300'
red = '#cc0000'
a4_aspectratio = 1.414
offset = 0.005 # Because having a vertical line looks weird
scaling_factor_dpi = 5

portrait1 = [
    {
        'color': blue,
        'radius': 15
        },
    {
        'color': black,
        'radius': 25
        },
    {
        'color': green,
        'radius': 35
        },
    {   'color': red,
        'radius': 45
        }
]

def circle_points(r, n=75):
    return [(cos(2*pi/n*x+offset)*r,sin(2*pi/n*x+offset)*r, 2*pi/n*x+offset) for x in range(0,n+1)]

def line_points(t, r, l=150):
    tt = t + pi/2
    p1 = (cos(t)*r + cos(tt)*l, sin(t)*r + sin(tt) * l)
    p2 = (cos(t)*r , sin(t)*r)
    p3 = (cos(t)*r - cos(tt)*l, sin(t)*r - sin(tt) * l)
    return [p1, p2, p3]

def portrait(params):
    fig = plt.figure()
    ax = plt.Axes(fig,[0,0,1,1])
    fig.add_axes(ax)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    for param in params:
        circle = circle_points(param.get('radius'))

        x = [x for x, _ , _ in circle]
        y = [y for _, y, _ in circle]

        for _, _, t in circle:
            line = line_points(t, param.get('radius'))
            x = [x for x, _ in line]
            y = [y for _, y in line]
            ax.plot(x, y, '-', color=param.get('color'), linewidth=0.2)
    ax.set_aspect('equal')
    ax.set_xlim(right=55, left=-55)
    ax.set_ylim(top=55*a4_aspectratio,bottom=-55*a4_aspectratio)
    ax.margins(0,0)
    ax.set_axis_off()
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    #plt.show()
    fig.savefig("test.png", dpi=480, bbox_inches=Bbox(np.array([[1.495, 0], [4.91, 4.8]])), pad_inches=0)

portrait(portrait1)