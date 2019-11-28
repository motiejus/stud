#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

from collections import namedtuple
from shapely.geometry import LineString, asPolygon
from descartes import PolygonPatch

from measure import *

offset = namedtuple('offset', ['width', 'direction', 'dashes', 'color'])
kelias = namedtuple('kelias', ['line', 'width', 'kat', 'dashes', 'color', 'offsets'])

fig, ax = plt.subplots()

a08 = kelias(
        line=LineString([Points[i].xy for i in [1,2,3] ]),
        width=A08_plotis,
        kat=KAT1,
        dashes=[10,3,2,3],
        color='red',
        offsets=(
            offset(L6+L5+L4, 'right', [100,20], 'lightgreen'),
            offset(L6+L5,    'right', [100,20], 'lightgreen'),
            offset(L6,       'right',    [1,0],      'black'),
            offset(L7,        'left',    [1,0],      'black'),
            offset(L7+L8,     'left', [100,20], 'lightgreen'),
            offset(L7+L8+L9,  'left', [100,20], 'lightgreen'),
        ),
)

for kelias in [a08]:
    # ašis
    ax.plot(*kelias.line.xy, linewidth=2, dashes=kelias.dashes, color=kelias.color, zorder=kelias.kat)

    # offset'ai
    offset_multiplier = kelias.width/(kelias.offsets[0].width + kelias.offsets[-1].width)
    offset_lines = []
    for offset in kelias.offsets:
        l = kelias.line.parallel_offset(offset.width * offset_multiplier, offset.direction, join_style=2)
        offset_lines.append(l)
        ax.plot(*l.xy, linewidth=.5, dashes=offset.dashes, color=offset.color, zorder=kelias.kat)
    # kelio poligonas su plotu
    kelias_poly = np.vstack((offset_lines[0].coords, offset_lines[-1].coords))
    ax.add_patch(PolygonPatch(asPolygon(kelias_poly), fc='white', zorder=kelias.kat, linewidth=0))



A03_l = LineString([Points[i].xy for i in [11,12,13,14,15,16,17,18] ])
A03_offsetR = A03_l.parallel_offset(A03_plotis, 'right', join_style=2)
ax.plot(*A03_l.xy, zorder=KAT3)
ax.plot(*A03_offsetR.xy, dashes=[5,5], zorder=KAT3)

A05_l = LineString([Points[i].xy for i in [4,5,6,7,8,9,10] ])
A05_offsetL = A05_l.parallel_offset(L2, 'left', join_style=2)
A05_offsetR = A05_l.parallel_offset(L3, 'right', join_style=2)
ax.plot(*A05_l.xy, zorder=KAT2)
ax.plot(*A05_offsetL.xy, dashes=[5,5], zorder=KAT2)
ax.plot(*A05_offsetR.xy, dashes=[5,5], zorder=KAT2)

ax.set_title('Užliejamų plotų brėžinys')

plt.show()
