#!/usr/bin/python3

import sys

from math import sin, cos, radians
from shapely.geometry import LineString
import matplotlib.pyplot as plt



# bendri
lambda_0 = 0
dphi = 5
dlambda = 5
R = 6_388_945
H = 350_000
D = H + R

# Įdomesni
dphi = 2
dlambda = 2
phi_p, phi_s = 0, 32
lambda_v, lambda_r = -16, 16
plt.xkcd()

# mano
#phi_p, phi_s = 43, 53
#lambda_v, lambda_r = -5, 5

# Ovodo
# phi_p, phi_s = 40, 50
# lambda_v, lambda_r = -5, 5

# apskaičiuoti
nphi = int((phi_s-phi_p)/dphi)+1
phi_0 = (phi_p+phi_s)/2
nlambda = int((lambda_r-lambda_v)/dlambda)+1


def c(x):
    return "{}°".format(x)


def annotate(ax, text, point, heading):
    ax.annotate(text, point, textcoords="offset points", xytext=heading, fontsize='xx-small')


def yx(phi, lambd):
    # phi - lat in degrees
    # lambd - lon in degrees
    rphi = radians(phi)
    rlambd = radians(lambd)
    cosz = sin(rphi)*sin(rphi_0)+cos(rphi)*cos(rphi_0)*cos(rlambd-rlambda_0)
    sinzcosa = sin(rphi)*cos(rphi_0)-cos(rphi)*sin(rphi_0)
    sinzsina = cos(rphi)*sin(rlambd-rlambda_0)
    x = H*R*sinzcosa/(D-R*cosz)
    y = H*R*sinzsina/(D-R*cosz)
    return (y/1e4, x/1e4)


W, E, N, S = (-25, 0), (10, 0), (0, 10), (0, -25)


# verčiame laipsnius į radianus
for v in ['phi_0', 'phi_p', 'phi_s', 'lambda_0', 'lambda_v', 'lambda_r']:
    locals()["r"+v] = radians(locals()[v])

points = []
for i in range(nphi):
    phid = phi_p + i*dphi
    on_y = []
    for j in range(nlambda):
        lambdad = lambda_v + j*dlambda
        on_y.append(yx(phid, lambdad))
    points.append(sorted(on_y))


fig, ax = plt.subplots()
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


if __name__ == '__main__':
    if len(sys.argv) == 2:
        plt.savefig(sys.argv[1], bbox_inches='tight')
        print("Saved %s" % sys.argv[1])
    else:
        plt.show()
