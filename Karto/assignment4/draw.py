#!/usr/bin/env python3
import matplotlib.pyplot as plt
from shapely.geometry import LineString

from measure import *

fig, ax = plt.subplots()

A08_l = LineString([Points[i].xy for i in [1,2,3] ])
A08_multiplier = A08_plotis/(L4+L5+L6+L7+L8+L9)

A08_offsetR1 = A08_l.parallel_offset(L6*A08_multiplier, 'right', join_style=2)
A08_offsetR2 = A08_l.parallel_offset((L6+L5)*A08_multiplier, 'right', join_style=2)
A08_offsetR3 = A08_l.parallel_offset((L6+L5+L4)*A08_multiplier, 'right', join_style=2)
A08_offsetL1 = A08_l.parallel_offset(L7*A08_multiplier, 'left', join_style=2)
A08_offsetL2 = A08_l.parallel_offset((L7+L8)*A08_multiplier, 'left', join_style=2)
A08_offsetL3 = A08_l.parallel_offset((L7+L8+L9)*A08_multiplier, 'left', join_style=2)
ax.plot(*A08_l.xy, linewidth=2, dashes=[5,2,2,5], color='red', zorder=KAT3)
ax.plot(*A08_offsetR1.xy, linewidth=.5, zorder=KAT1, color='black')
ax.plot(*A08_offsetR2.xy, linewidth=.5, dashes=[5,3], color='lightgreen', zorder=KAT1)
ax.plot(*A08_offsetR3.xy, linewidth=.5, dashes=[5,3], color='lightgreen', zorder=KAT1)
ax.plot(*A08_offsetL1.xy, linewidth=.5, zorder=KAT1, color='black')
ax.plot(*A08_offsetL2.xy, linewidth=.5, dashes=[5,3], color='lightgreen', zorder=KAT1)
ax.plot(*A08_offsetL3.xy, linewidth=.5, dashes=[5,3], color='lightgreen', zorder=KAT1)

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
