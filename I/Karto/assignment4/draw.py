#!/usr/bin/env python3
from math import atan, pi
import numpy as np
import matplotlib.pyplot as plt

from collections import namedtuple
from shapely.geometry import LineString, asPolygon, Point as sPoint, asLineString
from descartes import PolygonPatch

from measure import *

# nubraižytos kelio linijos ir jų nubrėžti offset'ai iš dešinės į kairę.
kelias_l = namedtuple('kelias_l', ['line', 'offsets'])

N, E, S, W = (0,10), (10,0), (0,-10), (-10,0)
point_annotations = {
         1: S,  2: E,  3: N,  4: W,
         5: N,  6: S,  7: S,  8: N,
         9: E, 10: N, 11: S, 12: N,
        13: S, 14: W, 15: N, 16: N,
        17: N, 18: E, 19: N, 20: S,
        21: N, 22: S, 23: E, 24: N,
}
road_annotations = {'A-08':W, 'A-05':N, 'A-03':N, 'G-11':E}

# implementacija
fig, ax = plt.subplots()
ax.set_aspect('equal')
plt.grid(True)

# taškų anotacijos
for v in vertices:
    ax.annotate(v.point, xy=v.xy, zorder=KAT0, textcoords='offset points',
            fontsize='small', xytext=point_annotations[v.point])

keliai_l = {}
# kelių piešimas
for id, kelias in keliai.items():
    # ašis
    kelias_line = LineString([Points[i].xy for i in kelias.virsunes])
    ax.plot(*kelias_line.xy, linewidth=2, dashes=kelias.dashes, color=kelias.spalva, zorder=kelias.kat)
    # offset'ai
    offset_multiplier = kelias.plotis/(kelias.juostos[0].plotis + kelias.juostos[-1].plotis)
    offset_lines = []
    for offset in kelias.juostos:
        l = kelias_line.parallel_offset(offset.plotis*offset_multiplier, offset.kryptis, join_style=2)
        offset_lines.append(l)
        ax.plot(*l.xy, linewidth=.5, dashes=offset.dashes, color=offset.spalva, zorder=kelias.kat)
    # kelio poligonas su plotu
    kelias_poly = np.vstack((offset_lines[0].coords, offset_lines[-1].coords))
    ax.add_patch(PolygonPatch(asPolygon(kelias_poly), fc='white', zorder=kelias.kat, linewidth=0))
    keliai_l[id] = kelias_l(line=kelias_line, offsets=offset_lines)

# kelių anotacijos
for id, kelias in keliai_l.items():
    linestart, lineend = np.array(kelias.offsets[-1].coords)[0:2]
    delta = lineend - linestart
    angle = atan(delta[1]/delta[0])*180/pi
    offset = road_annotations[id]
    ax.annotate(id, kelias.offsets[-1].coords[0], zorder=KAT0, textcoords='offset points',
            fontsize='small', xytext=offset, rotation=angle)

# septynkampis
prev_dirang = float(K1)*pi/180
step = 5/7*pi
heptagon = [np.array(Points[6].xy)]
for i in range(1, 7):
    dxy = np.array([float(D1)*cos(prev_dirang), float(D1)*sin(prev_dirang)])
    heptagon.append(heptagon[i-1] + dxy)
    prev_dirang += pi - step
ax.add_patch(PolygonPatch(asPolygon(heptagon), linewidth=2, fc='xkcd:white', ec='xkcd:magenta'))

# septynkampio centras
x0, y0 = Points[6].xy
x = x0 + float(D1)/(2*sin(pi/7))*sin(pi/7-float(K1)*pi/180)
y = y0 + float(D1)/(2*sin(pi/7))*cos(pi/7-float(K1)*pi/180)
center = sPoint(x, y)

# užlieta erdvė apskritimas
radius = float(D1)/2/sin(pi/7)-float(A1)
angles = np.linspace(0, 2*pi, num=360)
circle_y = y + np.sin(angles) * radius
circle_x = x + np.cos(angles) * radius
ax.plot(circle_x, circle_y)

if __name__ == '__main__':
    plt.show()
