#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

from collections import namedtuple
from shapely.geometry import LineString, asPolygon
from descartes import PolygonPatch

from measure import *

juosta = namedtuple('juosta', ['plotis', 'kryptis', 'dashes', 'spalva'])
kelias = namedtuple('kelias', ['virsunes', 'plotis', 'kat', 'dashes', 'spalva', 'juostos'])

CONTINUOUS = (1,0)
DASHDOTX2 = (10,3,2,3)
DASHED = (100,20)


a08 = kelias(
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
)

a05 = kelias(
        virsunes=[4,5,6,7,8,9,10],
        plotis=A05_plotis,
        kat=KAT2,
        dashes=DASHDOTX2,
        spalva='red',
        juostos=(
            juosta(L3, 'right', CONTINUOUS, 'brown'),
            juosta(L2, 'left',  CONTINUOUS, 'brown'),
        ),
)

a03 = kelias(
        virsunes=[11,12,13,14,15,16,17,18],
        plotis=A03_plotis,
        kat=KAT3,
        dashes=CONTINUOUS,
        spalva='pink',
        juostos=(
            juosta(L1, 'right', DASHED, 'pink'),
        ),
)

g11 = kelias(
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
)


# implementacija
fig, ax = plt.subplots()
ax.set_title('Užliejamų plotų brėžinys')

for kelias in [a08, a05, a03, g11]:
    # ašis
    kelias_line = LineString([Points[i].xy for i in kelias.virsunes ])
    ax.plot(*kelias_line.xy, linewidth=2, dashes=kelias.dashes, color=kelias.spalva, zorder=kelias.kat)

    # offset'ai
    offset_multiplier = kelias.plotis/(kelias.juostos[0].plotis + kelias.juostos[-1].plotis)
    offset_lines = []
    for offset in kelias.juostos:
        l = kelias_line.parallel_offset(offset.plotis * offset_multiplier, offset.kryptis, join_style=2)
        offset_lines.append(l)
        ax.plot(*l.xy, linewidth=.5, dashes=offset.dashes, color=offset.spalva, zorder=kelias.kat)
    # kelio poligonas su plotu
    kelias_poly = np.vstack((offset_lines[0].coords, offset_lines[-1].coords))
    ax.add_patch(PolygonPatch(asPolygon(kelias_poly), fc='white', zorder=kelias.kat, linewidth=0))


plt.show()
