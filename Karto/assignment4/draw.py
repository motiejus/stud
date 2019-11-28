#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

from collections import namedtuple
from shapely.geometry import LineString, asPolygon
from descartes import PolygonPatch

from measure import *

juosta = namedtuple('juosta', ['plotis', 'kryptis', 'dashes', 'spalva'])
kelias = namedtuple('kelias', ['virsunes', 'plotis', 'kat', 'dashes', 'spalva', 'juostos'])

fig, ax = plt.subplots()

a08 = kelias(
        virsunes=[1,2,3],
        plotis=A08_plotis,
        kat=KAT1,
        dashes=[10,3,2,3],
        spalva='red',
        juostos=(
            juosta(L6+L5+L4, 'right', (100,20), 'lightgreen'),
            juosta(L6+L5,    'right', (100,20), 'lightgreen'),
            juosta(L6,       'right',    (1,0),      'black'),
            juosta(L7,        'left',    (1,0),      'black'),
            juosta(L7+L8,     'left', (100,20), 'lightgreen'),
            juosta(L7+L8+L9,  'left', (100,20), 'lightgreen'),
        ),
)

a03 = kelias(
        virsunes=[11,12,13,14,15,16,17,18],
        plotis=A03_plotis,
        kat=KAT3,
        dashes=(1,0),
        spalva='pink',
        juostos=(
            offset(L1, 'right', (100,20), 'pink'),
        ),
)



for kelias in [a08, a03]:
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


A05_l = LineString([Points[i].xy for i in [4,5,6,7,8,9,10] ])
A05_offsetL = A05_l.parallel_offset(L2, 'left', join_style=2)
A05_offsetR = A05_l.parallel_offset(L3, 'right', join_style=2)
ax.plot(*A05_l.xy, zorder=KAT2)
ax.plot(*A05_offsetL.xy, dashes=[5,5], zorder=KAT2)
ax.plot(*A05_offsetR.xy, dashes=[5,5], zorder=KAT2)

ax.set_title('Užliejamų plotų brėžinys')

plt.show()
