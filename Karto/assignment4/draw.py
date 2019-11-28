#!/usr/bin/env python3
import matplotlib.pyplot as plt
from shapely.geometry import LineString

from measure import *

fig, ax = plt.subplots()

KA03_l = LineString([Points[i].xy for i in [11,12,13,14,15,16,17,18] ])
KA03_offset = KA03_l.parallel_offset(KA03_plotis, 'right', join_style=2)

ax.plot(*(KA03_l.xy), linewidth=1)
ax.plot(*(KA03_offset.xy), linewidth=1, dashes=[5,5])

ax.set_title('Užliejamų plotų brėžinys')

plt.show()
