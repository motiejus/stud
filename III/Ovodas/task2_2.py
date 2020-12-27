#!/usr/bin/python3

import sys
import csv
from math import radians, degrees, tan, atan, sin, cos

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


phi_loks = 27.308  # loksodromos platuma 12 ilgumoje interpoliavus

rphi_1, rphi_2 = radians(phi_1), radians(phi_2)
rlambda_1, rlambda_2 = radians(lambda_1), radians(lambda_2)
phil = round((phi_p+phi_s)/2)
nphi = int((phi_s-phi_p)/dphi)+1
nlambda = int((lambda_r-lambda_v)/dlambda)+1
midlambda = int(lambda_r+lambda_v)/2
midnlambda = int((lambda_r-midlambda)/dlambda)+1

# label orientations
W, E, N, S = (-25, -5), (10, -5), (-5, 10), (-5, -20)
SW, NE = (-10, -10), (5, 5)

kr = {}
with open("krasovskio.csv") as f:
    for row in csv.DictReader(f):
        kr[float(row['phi'])] = {k: float(v) for k, v in row.items()}

alpha = (kr[phi_1]["lgr"]-kr[phi_2]["lgr"])/(kr[phi_2]["lgU"]-kr[phi_1]["lgU"])
Ualpha = (10**kr[phi_p]["lgU"])**alpha
U1alpha = (10**kr[phi_1]["lgU"])**alpha
U2alpha = (10**kr[phi_2]["lgU"])**alpha
C1 = (kr[phi_1]["r"]*U1alpha)/alpha
C2 = (kr[phi_2]["r"]*U2alpha)/alpha
if abs(C1 - C2) / C1 > 1e-6:
    raise ValueError("too large error between C1 and C2")
Cmm = C1 * 1000 / M
qmm = Cmm/Ualpha


def yx(lat, lon):
    # lat - phi in degrees
    # lon - lambda in degrees
    lgU = kr[round(lat*2)/2.]["lgU"]
    Ualpha = (10**lgU)**alpha
    pmm = Cmm/Ualpha
    delta = alpha * lon
    xmm = qmm-pmm*cos(radians(delta))
    ymm = pmm*sin(radians(delta))
    return (ymm, xmm)


points = []
for i in range(nphi):
    phid = phi_p + i*dphi
    on_y = []
    for j in range(midnlambda):
        lambdad = j*dlambda
        ymm, xmm = yx(phid, lambdad)
        on_y.append((ymm, xmm))
        if j > 0:
            on_y.append((-ymm, xmm))
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
rmidlambda = radians(midlambda)
A = yx(phi_1, lambda_1-midlambda)
MidLoks = yx(phi_loks, 0)
B = yx(phi_2, lambda_2-midlambda)
loksodroma = ((A, MidLoks, B))
ax.plot(*(LineString(loksodroma).xy), color="xkcd:black", linewidth=.5)

# ortodroma
ctgu = ctg(rphi_1)*tan(rphi_2)*cosec(rlambda_2-rlambda_1)-ctg(rlambda_2-rlambda_1)
u = arccot(ctgu)
ortodroma = []
for lambdad in lambda_range:
    phi_ort = atan(tan(rphi_1)*cosec(u)*sin(u-rlambda_1+radians(lambdad)))
    ortodroma.append(yx(round(degrees(phi_ort)*2)/2, lambdad-midlambda))
ax.plot(*(LineString(ortodroma).xy), color="xkcd:black", linewidth=.5)

annotate(ax, "A", A, SW)
annotate(ax, "B", B, NE)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        plt.savefig(sys.argv[1], bbox_inches='tight')
        print("Saved %s" % sys.argv[1])
    else:
        plt.show()
