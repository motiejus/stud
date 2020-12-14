#!/usr/bin/python3

from math import sin, cos, sqrt, e, log, radians, pi, degrees

sinq = lambda x: sin(x)**2
sqr = lambda x: x**2

# duota
B = radians(13)

# didysis pusašis
a = 6378137

# suspaudimas
alpha = 1/298.25722

# mažasis pusašis
b = a*(1-alpha)

# ekscentricitetas
e2 = (a**2-b**2)/(a**2)

# meridiano kreivumo spindulys
M = a*(1-e2)/((1-e2*sinq(B))**3/2)

# meridiano vertikalės kreivumo spindulys
N = a/sqrt(1-e2*sinq(B))

# vidutinis kreivumo spindulys
R = sqrt(M*N)

# lygiagretės spindulys
r = N * cos(B)

# Lygiagretės lanko ilgis metrais
Sn = r/degrees(1)

## Trapecijos plotas esant 1 radiano platumai
P = sqr(b)/2 * ( sin(B)/(1-e2*sinq(B)) + 1/(2*e)*log( (1+e*sin(B))/(1-e*sin(B)) ) )

g = globals()
for v in ["b", "e2", "M", "N", "R", "r", "Sn", "P"]:
    print("%2s: %18.4f" % (v, g[v]))
