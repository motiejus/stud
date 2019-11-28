#!/usr/bin/env python3
import matplotlib.pyplot as plt
from shapely.geometry import LineString
from math import sqrt

def heptagon(linelen, slant):
    inner_angle = 180*5/7
    pts = [(0, 0)]
    dx = linelen * sin(
    for _ in range(7):

def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color='#6699cc', alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)

fig, ax = plt.subplots()
line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])

#plot_coords(ax, line)
#plot_bounds(ax, line)
plot_line(ax, line)

ax.set_title('Užliejamų plotų brėžinys')

plt.show()
