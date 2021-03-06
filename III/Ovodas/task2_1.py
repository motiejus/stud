#!/usr/bin/python3

import sys
import csv

from math import radians, degrees, tan, atan, pi, log, sin, cos
from shapely.geometry import LineString
import matplotlib.pyplot as plt

from consts import (
        phi_p, phi_s, dphi,
        phi_1, phi_2,
        lambda_1, lambda_2, lambda_range,
        lambda_v, lambda_r, dlambda,
        M
)


def c(x):
    return "{}°".format(x)


def annotate(ax, text, point, heading):
    ax.annotate(text, point, textcoords="offset points", xytext=heading)


def ctg(x):
    return cos(x)/sin(x)


def arccot(x):
    return atan(1/x)


def cosec(x):
    return 1/sin(x)


rphi_1, rphi_2 = radians(phi_1), radians(phi_2)
rlambda_1, rlambda_2 = radians(lambda_1), radians(lambda_2)
phil = round((phi_p+phi_s)/2)
nphi = int((phi_s-phi_p)/dphi)+1
nlambda = int((lambda_r-lambda_v)/dlambda)+1

# label orientations
W, E, N, S = (-25, -5), (10, -5), (-5, 10), (-5, -20)
SW, NE = (-10, -10), (5, 5)

kr = {}
with open("krasovskio.csv") as f:
    for row in csv.DictReader(f):
        kr[float(row['phi'])] = row
betamm = float(kr[phil]["r"]) * 1000 / M


def yx(lat, lon):
    # lat - phi in degrees
    # lon - lambda in degrees
    phi = radians(lat)
    U = tan(pi/4 + phi/2)
    xmm = betamm * log(U)
    ymm = betamm * radians(lon)
    return (ymm, xmm)


points = []
for i in range(nphi):
    phid = phi_p + i*dphi
    on_y = []
    for j in range(nlambda):
        lambdad = lambda_v + j*dlambda
        on_y.append(yx(phid, lambdad))
    points.append(sorted(on_y))


fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis("off")


# abscises
for i in range(nphi):
    row = [points[i][j] for j in range(nlambda)]
    ax.plot(*(LineString(row).xy), color="xkcd:black", linewidth=.5)
    annotate(ax, c(phi_p+i*dphi), row[0], W)
    annotate(ax, c(phi_p+i*dphi), row[-1], E)

# ordinates
for i in range(nlambda):
    col = [points[j][i] for j in range(nphi)]
    ax.plot(*(LineString(col).xy), color="xkcd:black", linewidth=.5)
    annotate(ax, c(lambda_v+i*dlambda), col[0], S)
    annotate(ax, c(lambda_v+i*dlambda), col[-1], N)

# loksodroma
A = yx(phi_1, lambda_1)
B = yx(phi_2, lambda_2)
loksodroma = ((A, B))
ax.plot(*(LineString(loksodroma).xy), color="xkcd:black", linewidth=.5)

# ortodroma
ctgu = ctg(rphi_1)*tan(rphi_2)*cosec(rlambda_2-rlambda_1)-ctg(rlambda_2-rlambda_1)
u = arccot(ctgu)
ortodroma = []
for lambdad in lambda_range:
    phi_ort = atan(tan(rphi_1)*cosec(u)*sin(u-rlambda_1+radians(lambdad)))
    ortodroma.append(yx(round(degrees(phi_ort)*2)/2, lambdad))
ax.plot(*(LineString(ortodroma).xy), color="xkcd:black", linewidth=.5)

annotate(ax, "A", A, SW)
annotate(ax, "B", B, NE)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        plt.savefig(sys.argv[1], bbox_inches='tight')
        print("Saved %s" % sys.argv[1])
    else:
        plt.show()
