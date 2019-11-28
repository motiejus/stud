#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString, asPolygon
from shapely.coords import CoordinateSequence
from descartes import PolygonPatch

from measure import *

fig, ax = plt.subplots()

A08_l = LineString([Points[i].xy for i in [1,2,3] ])
A08_multiplier = A08_plotis/(L4+L5+L6+L7+L8+L9)

def offset(width, direction):
    return A08_l.parallel_offset(width * A08_multiplier, direction, join_style=2)
offsets = (
    (offset(L6+L5+L4, 'right'), (5,3), 'lightgreen'),
    (offset(L6+L5,    'right'), (5,3), 'lightgreen'),
    (offset(L6,       'right'), (1,0),      'black'),
    (offset(L7,        'left'), (1,0),      'black'),
    (offset(L7+L8,     'left'), [5,3], 'lightgreen'),
    (offset(L7+L8+L9,  'left'), [5,3], 'lightgreen'),
)
for line, dashes, color in offsets:
    ax.plot(*line.xy, linewidth=.5, dashes=dashes, color=color, zorder=KAT1)

A08_poly = np.vstack((offsets[0][0].coords, offsets[-1][0].coords))
ax.add_patch(PolygonPatch(asPolygon(A08_poly), fc='white', zorder=KAT1, linewidth=0))
ax.plot(*A08_l.xy, linewidth=2, dashes=[5,2,2,5], color='red', zorder=KAT1)


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
