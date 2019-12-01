#!/usr/bin/env python3
from math import sqrt

import numpy as np
from scipy.spatial.distance import euclidean

A = -7.756
B = 4.686
C = -7.663
Z = -7.103
E = 6.405
F = -6.552
G = 6.931
N = -3.986
M = -5.285

# Atraminiu liniju koordinates ir uzkirciu ilgiai(m) [Koord. LKS94 sistemoje jau sukeistos]:
# -- Atrama T23-T24-T25 --
XT23 = 564383.829 + N
YT23 = 6173144.853 + A
T23 = np.array([XT23, YT23])
# ---------------
XT24 = 564444.357 + F
YT24 = 6173086.343 + C
T24 = np.array([XT24, YT24])
# ---------------
XT25 = 564673.556 + B
YT25 = 6173055.598 + M
T25 = np.array([XT25, YT25])
# ---------------
print("""
Kontrolinis atstumas T23-T24 = 82.293 ?= %.3f""" % euclidean(T23,T24) + """
Kontrolinis atstumas T24-T25 = 242.105 ?= %.3f""" % euclidean(T24,T25) + """
----- 1 tasko uzkirciai (metrais)----------
T23-1 = 161.722
T24-1 = 125.560
T25-1 = 169.686
----- 2 tasko uzkirciai (metrais)----------
T23-2 = 91.681
T24-2 = 58.350
T25-2 = 220.938
----- 3 tasko uzkirciai (metrais)----------
T23-3 = 82.431
T24-3 = 126.263
T25-3 = 294.537
----- 9 tasko uzkirciai (metrais)----------
T23-9 = 265.534
T24-9 = 227.287
T25-9 = 132.783
----- 10 tasko uzkirciai (metrais)----------
T23-10 = 288.522
T24-10 = 238.487
T25-10 = 89.932
----- 11 tasko uzkirciai (metrais)----------
T23-11 = 211.001
T24-11 = 165.636
T25-11 = 126.845
-- Atrama T26-T27-T28 --
""")
XT26 = 564414.733 + G
YT26 = 6173298.332 + N
T26 = np.array([XT26, YT26])
print("""
XT26 = %.3f""" % XT26 + """
YT26 = %.3f""" % YT26 + """
---------------
""")
XT27 = 564564.172 + G
YT27 = 6173312.063 + B
T27 = np.array([XT27, YT27])
print("""
XT27 = %.3f""" % XT27 + """
YT27 = %.3f""" % YT27 + """
---------------
""")
XT28 = 564770.145 + N
YT28 = 6173230.520 + N
T28 = np.array([XT28, YT28])
print("""
XT28 = %.3f""" % XT28 + """
YT28 = %.3f""" % YT28 + """
---------------
Kontrolinis atstumas T26-T27 = 151.109 ?= %.3f""" % euclidean(T26, T27) + """
Kontrolinis atstumas T27-T28 = 214.908 ?= %.3f""" % euclidean(T27, T28) + """
----- 4 tasko uzkirciai (metrais)----------
T26-4 = 101.226
T27-4 = 137.261
T28-4 = 284.950
----- 5 tasko uzkirciai (metrais)----------
T26-5 = 32.511
T27-5 = 125.052
T28-5 = 319.540
----- 6 tasko uzkirciai (metrais)----------
T26-6 = 155.114
T27-6 = 46.286
T28-6 = 196.223
----- 7 tasko uzkirciai (metrais)----------
T26-7 = 247.440
T27-7 = 128.403
T28-7 = 107.731
----- 8 tasko uzkirciai (metrais)----------
T26-8 = 258.183
T27-8 = 149.388
T28-8 = 109.161


Objektu koordinates:
X12 = 564474.034 + M
Y12 = 6173175.426 + F
---------------
X13 = 564505.240 + C
Y13 = 6173237.929 + E
---------------
X14 = 564519.570 + C
Y14 = 6173255.007 + F
---------------
X15 = 564615.010 + A
Y15 = 6173215.649 + Z
---------------
X16 = 564627.375 + E
Y16 = 6173220.989 + Z
---------------
X17 = 564627.105 + N
Y17 = 6173210.067 + Z
---------------
X18 = 564607.740 + C
Y18 = 6173171.025 + Z
---------------
X19 = 564558.331 + B
Y19 = 6173177.716 + Z
---------------
X20 = 564546.236 + M
Y20 = 6173183.298 + Z
---------------
X21 = 564558.601 + N
Y21 = 6173188.638 + C
---------------
X22 = 564539.728 + F
Y22 = 6173230.148 + E
---------------

 --------- Kiti duomenys ----------------

N1 objekto kampu skaicius = 10

Objektu N1,M1,M2,M3 matmenys (metrais)
B1 = 7.844
B2 = 21.868
B3 = 11.344
B4 = 12.464
B5 = 23.702
B6 = 15.508

Objekto M3 pasukimo kampas (laipsniais)
K1 = 58.5910


---- A sklypui prikauso: ----
1 objektas = M3
2 objektas = N3
3 objektas = N2
Pastaba. Like objektai priklauso B sklypui.

Sklypus pradeti dalinti nuo ribos tasko Nr. 4
Pastaba. Dalinimas baigiamas bet kuriame kitame (ne pradiniame)sklypo ribos taske.

Sklypo ribu (tvoru) Sutartiniai Zenklai (SZ)
1. Isorine sklypo riba:
SZ virsuniu skaicius
SZ1 = 4
Daugiakampio krastines ilgis (m)
R1 = 2.550
Atstumas tarp sutartiniu zenklu centru (m)
D1 = 10.863
Tvoros aukstis (m)
H1 = 1.95

2. Sklypo zemes dalijimo riba:
SZ virsuniu skaicius
SZ2 = 6
Daugiakampio krastines ilgis (m)
R2 = 1.454
Atstumas tarp sutartiniu zenklu centru (m)
D2 = 4.173
Ribos tvoros aukstis (m)
H2 = 2.20



Medziu aukstis (m)
Hm = 2.94
""")
