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
bearings = {
    23: np.array([564383.829+N, 6173144.853+A]),
    24: np.array([564444.357+F, 6173086.343+C]),
    25: np.array([564673.556+B, 6173055.598+M]),
    26: np.array([564414.733+G, 6173298.332+N]),
    27: np.array([564564.172+G, 6173312.063+B]),
    28: np.array([564770.145+N, 6173230.520+N]),
}

print("""Atraminiu liniju koordinates ir uzkirciu ilgiai(m):""")

for id, bearing in bearings.items():
    print("T%d: (%.3f,%.3f)" % (id, bearing[0], bearing[1]))

print("""
---------------
Kontr. atst. T23-T24 =  82.293 ?= %.3f""" % euclidean(bearings[23],bearings[24]) + """
Kontr. atst. T24-T25 = 242.105 ?= %.3f""" % euclidean(bearings[24],bearings[25]) + """
Kontr. atst. T26-T27 = 151.109 ?= %.3f""" % euclidean(bearings[26], bearings[27]) + """
Kontr. atst. T27-T28 = 214.908 ?= %.3f""" % euclidean(bearings[27], bearings[28]) + """

Objektu koordinates:""")
objs = {
    12: np.array([564474.034+M, 6173175.426+F]),
    13: np.array([564505.240+C, 6173237.929+E]),
    14: np.array([564519.570+C, 6173255.007+F]),
    15: np.array([564615.010+A, 6173215.649+Z]),
    16: np.array([564627.375+E, 6173220.989+Z]),
    17: np.array([564627.105+N, 6173210.067+Z]),
    18: np.array([564607.740+C, 6173171.025+Z]),
    19: np.array([564558.331+B, 6173177.716+Z]),
    20: np.array([564546.236+M, 6173183.298+Z]),
    21: np.array([564558.601+N, 6173188.638+C]),
    22: np.array([564539.728+F, 6173230.148+E]),
}
for id, obj in objs.items():
    print("%d: (%.3f,%.3f)" % (id, obj[0], obj[1]))
