#!/usr/bin/python3

import csv
from math import degrees, radians, tan, pi, log
from shapely.geometry import LineString
import matplotlib.pyplot as plt

phi_p, phi_s, dphi = 13, 49, 6
lambda_v, lambda_r, dlambda = 0, 24, 6
M = 25e6
phil = round((phi_p+phi_s)/2)
nphi = int((phi_s-phi_p)/dphi)+1
nlambda = int((lambda_r-lambda_v)/dlambda)+1

# label orientations
W, E, N, S = (-25, -5), (10, -5), (-5, 10), (-5, -20)

krasovskio = {}
with open("krasovskio.csv") as f:
    for row in csv.DictReader(f):
        krasovskio[float(row['phi'])] = row
betamm = float(krasovskio[phil]["r"]) * 1000 / M

points = []
for i in range(nphi):
    phid = phi_p + i*dphi
    phi = radians(phid)
    U = tan(pi/4 + phi/2)
    xmm = betamm * log(U)
    on_y = []
    for j in range(nlambda):
        lambdad = lambda_v + j*dlambda
        ymm = betamm * lambdad / degrees(1)
        on_y.append((ymm, xmm))
    points.append(on_y)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis("off")


def annotate(ax, nr, point, heading):
    text = "{}°".format(nr)
    ax.annotate(text, point, textcoords="offset points", xytext=heading)


# abscises
for i in range(nphi):
    row = [points[i][j] for j in range(nlambda)]
    ax.plot(*(LineString(row).xy), color="xkcd:black", linewidth=.5)
    annotate(ax, phi_p+i*dphi, row[0], W)
    annotate(ax, phi_p+i*dphi, row[-1], E)

# ordinates
for i in range(nlambda):
    col = [points[j][i] for j in range(nphi)]
    ax.plot(*(LineString(col).xy), color="xkcd:black", linewidth=.5)
    annotate(ax, lambda_v+i*dlambda, col[0], S)
    annotate(ax, lambda_v+i*dlambda, col[-1], N)

if __name__ == '__main__':
    plt.show()
