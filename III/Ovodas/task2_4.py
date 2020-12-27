#!/usr/bin/python3

import csv
from math import sin, cos, acos, radians, degrees, atan

from consts import phi_1, lambda_1, phi_2, lambda_2


# krasovskio
kr = {}
with open("krasovskio.csv") as f:
    for row in csv.DictReader(f):
        kr[float(row['phi'])] = {k: float(v) for k, v in row.items()}


def sec(x):
    return 1/cos(x)


# konstantos/radianai
midphi = (phi_1+phi_2)/2
rphi_1, rphi_2 = radians(phi_1), radians(phi_2)
rlambda_1, rlambda_2 = radians(lambda_1), radians(lambda_2)

# ortodroma
rdelta = acos(sin(rphi_1)*sin(rphi_2) + cos(rphi_1)*cos(rphi_2)*cos(rlambda_2-rlambda_1))
delta = degrees(rdelta)
R = 6366255.58  # rutulio spindulys iš pavyzdžio
ortodromos_ilgis = rdelta * R

# loksodroma
D_1 = kr[phi_1]["D"]
D_2 = kr[phi_2]["D"]
ralpha_loks = atan(60*(lambda_2 - lambda_1) / (D_2 - D_1))

loksodromos_ilgis = (rphi_2 - rphi_1) * kr[midphi]["R"] * sec(ralpha_loks)

if __name__ == '__main__':
    print("Ortodromos ilgis (m): %d" % round(ortodromos_ilgis))
    print("Loksodromos ilgis (m): %d" % round(loksodromos_ilgis))
