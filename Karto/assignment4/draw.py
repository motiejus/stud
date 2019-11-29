#!/usr/bin/env python3
from math import atan, pi
import numpy as np
import matplotlib.pyplot as plt

from collections import namedtuple
from shapely.geometry import LineString, asPolygon
from descartes import PolygonPatch

from measure import *

juosta = namedtuple('juosta', ['plotis', 'kryptis', 'dashes', 'spalva'])
kelias = namedtuple('kelias', ['id', 'virsunes', 'plotis', 'kat', 'dashes', 'spalva', 'juostos'])

# nubraižytos kelio linijos ir jų nubrėžti offset'ai iš dešinės į kairę.
kelias_l = namedtuple('kelias_l', ['id', 'line', 'offsets'])

CONTINUOUS = (1,0)
DASHDOTX2 = (10,3,2,3)
DASHED = (100,20)

keliai = [
    kelias(
        id='A-08',
        virsunes=[1,2,3],
        plotis=A08_plotis,
        kat=KAT1,
        dashes=DASHDOTX2,
        spalva='red',
        juostos=(
            juosta(L6+L5+L4, 'right', DASHED,     'lightgreen'),
            juosta(L6+L5,    'right', DASHED,     'lightgreen'),
            juosta(L6,       'right', CONTINUOUS, 'black'),
            juosta(L7,       'left',  CONTINUOUS, 'black'),
            juosta(L7+L8,    'left',  DASHED,     'lightgreen'),
            juosta(L7+L8+L9, 'left',  DASHED,     'lightgreen'),
        ),
    ),
    kelias(
        id='A-05',
        virsunes=[4,5,6,7,8,9,10],
        plotis=A05_plotis,
        kat=KAT2,
        dashes=DASHDOTX2,
        spalva='red',
        juostos=(
            juosta(L3, 'right', CONTINUOUS, 'brown'),
            juosta(L2, 'left',  CONTINUOUS, 'brown'),
        ),
    ),
    kelias(
        id='A-03',
        virsunes=[11,12,13,14,15,16,17,18],
        plotis=A03_plotis,
        kat=KAT3,
        dashes=CONTINUOUS,
        spalva='pink',
        juostos=(
            juosta(L1, 'right', DASHED, 'pink'),
            juosta(0,   'left', DASHED, 'white'),
        ),
    ),
    kelias(
        id='G-11',
        virsunes=[19,20,21,22,23],
        plotis=G11_plotis,
        kat=KAT4,
        dashes=CONTINUOUS,
        spalva='red',
        juostos=(
            juosta(L10+L11, 'right', CONTINUOUS, 'blue'),
            juosta(L11,     'right', CONTINUOUS, 'lightblue'),
            juosta(L12,     'left',  CONTINUOUS, 'lightblue'),
            juosta(L12+L13, 'left',  CONTINUOUS, 'blue'),
        ),
    ),
]

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
plt.grid(True)

# taškų anotacijos
for v in vertices:
    ax.annotate(v.point, xy=v.xy, zorder=KAT0, textcoords='offset points', xytext=point_annotations[v.point])

keliai_l = {}
# kelių piešimas
for kelias in keliai:
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
    keliai_l[kelias.id] = kelias_l(id=kelias.id, line=kelias_line, offsets=offset_lines)

# kelių anotacijos
for id, kelias in keliai_l.items():
    linestart, lineend = np.array(kelias.offsets[-1].coords)[0:2]
    delta = lineend - linestart
    angle = atan(delta[1]/delta[0])*180/pi
    offset = road_annotations[id]
    ax.annotate(id, kelias.offsets[-1].coords[0], zorder=KAT0, textcoords='offset points', xytext=offset, rotation=angle)

# septynkampis
prev_dirang = float(K1)*pi/180
step = 5*7*pi
heptagon = [np.array(Points[6].xy)]
for i in range(1, 7):
    dxy = np.array([float(D1)*cos(prev_dirang), float(D1)*sin(prev_dirang)])
    heptagon.append(heptagon[i-1] + dxy)
    prev_dirang += step
ax.add_patch(PolygonPatch(asPolygon(heptagon), linewidth=2, fc='grey'))

plt.show()
