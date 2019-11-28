#!/usr/bin/env python3
import matplotlib.pyplot as plt
from shapely.geometry import LineString

from measure import *

fig, ax = plt.subplots()

KA08_l = LineString([Points[i].xy for i in [1,2,3] ])
KA08_Lwidth = (L7+L8+L9)/A08_plotis
KA08_Rwidth = (L6+L5+L4)/A08_plotis

KA08_offsetR1 = KA08_l.parallel_offset(L6, 'right', join_style=2)
KA08_offsetR2 = KA08_l.parallel_offset(L6+L5, 'right', join_style=2)
KA08_offsetR3 = KA08_l.parallel_offset(L6+L5+L4, 'right', join_style=2)
KA08_offsetL1 = KA08_l.parallel_offset(L7, 'left', join_style=2)
KA08_offsetL2 = KA08_l.parallel_offset(L7+L8, 'left', join_style=2)
KA08_offsetL3 = KA08_l.parallel_offset(L7+L8+L9, 'left', join_style=2)
ax.plot(*KA08_l.xy, dashes=[5,5], zorder=KAT3)
ax.plot(*KA08_offsetR1.xy, zorder=KAT1)
ax.plot(*KA08_offsetR2.xy, dashes=[5,5], zorder=KAT1)
ax.plot(*KA08_offsetR3.xy, dashes=[5,5], zorder=KAT1)
ax.plot(*KA08_offsetL1.xy, zorder=KAT1)
ax.plot(*KA08_offsetL2.xy, dashes=[5,5], zorder=KAT1)
ax.plot(*KA08_offsetL3.xy, dashes=[5,5], zorder=KAT1)

KA03_l = LineString([Points[i].xy for i in [11,12,13,14,15,16,17,18] ])
KA03_offsetR = KA03_l.parallel_offset(KA03_plotis, 'right', join_style=2)
ax.plot(*KA03_l.xy, zorder=KAT3)
ax.plot(*KA03_offsetR.xy, dashes=[5,5], zorder=KAT3)

KA05_l = LineString([Points[i].xy for i in [4,5,6,7,8,9,10] ])
KA05_offsetL = KA05_l.parallel_offset(L2, 'left', join_style=2)
KA05_offsetR = KA05_l.parallel_offset(L3, 'right', join_style=2)
ax.plot(*KA05_l.xy, zorder=KAT2)
ax.plot(*KA05_offsetL.xy, dashes=[5,5], zorder=KAT2)
ax.plot(*KA05_offsetR.xy, dashes=[5,5], zorder=KAT2)

ax.set_title('Užliejamų plotų brėžinys')

plt.show()
