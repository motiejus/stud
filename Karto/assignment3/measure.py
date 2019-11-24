#!/usr/bin/env python3
from decimal import Decimal as Dec
from deg import Deg

from math import tan, pi

def fmt(deg):
    if deg > 180:
        deg -= 360
    elif deg < -180:
        deg += 360
    return "%12.7f" % deg

def pr(deg): return 270 + deg
def pv(deg): return 270 - deg
def vp(deg): return 180 + deg
def vs(deg): return 180 - deg
def sv(deg): return 90 + deg
def sr(deg): return 90 - deg
def rs(deg): return deg
def rp(deg): return 360 - deg

# Sklypu pradiniu tasku (1 ir 15) koordinates:
X1 = Dec('16639.290')
Y1 = Dec('25500.960')
X15 = Dec('17191.590')
Y15 = Dec('25121.430')

# Sklypu sujungimo tasko T3 koordinates:
XT3 = Dec('16971.790')
YT3 = Dec('26685.160')

Xcoords = Dec('17000')
Ycoords = Dec('26700')

# T1, T2
XT1 = Dec('16640.989')
YT1 = Dec('25379.137')
XT2 = Dec('17271.328')
YT2 = Dec('25325.608')

# Pataisos ATKARPOMS:
A = Dec('-2.207')
B = Dec('1.999')
C = Dec('4.838')
D = Dec('2.862')
E = Dec('-5.907')
F = Dec('-3.744')
G = Dec('-1.466')
H = Dec('6.841')
M = Dec('-4.824')

# Pataisos KAMPAMS:
K = Dec('-7.7422786')
L = Dec('-6.6428275')
N = Dec('-4.2872043')
P = Dec('-3.1145084')
R = Dec('-7.2564859')
S = Dec('3.8874407')
T = Dec('-8.7554531')

L1L1  = Dec('125.829') + G
L1L2  = Dec('81.682') + E
L1L3  = Dec('61.206') + H
L1L4  = Dec('121.055') + D
L1L5  = Dec('79.892') + B
L1L6  = Dec('159.299') + H
L1L7  = Dec('76.500') + E
L1L8  = Dec('51.091') + G
L1L9  = Dec('93.765') + F
L1L10 = Dec('58.926') + D
L1L11 = Dec('79.061') + M
L1L12 = Dec('121.209') + D
L1L13 = Dec('94.071') + C
L2L1  = Dec('205.221') + C
L2L2  = Dec('122.820') + G
L2L3  = Dec('178.657') + H
L2L4  = Dec('116.987') + B
L2L5  = Dec('84.793') + H
L2L6  = Dec('138.291') + F
L2L7  = Dec('85.607') + H
L2L8  = Dec('114.589') + G
L2L9  = Dec('79.210') + D

# Drawing angles
DK1K1  = pr(Deg.guess('84-03-08.3').frac + P)
DK1K2  = rp(Deg.guess('112-58-25.4').frac + S)
DK1K3  = vp(Deg.guess('54.3107235').frac + L)
DK1K4  = pr(Deg.guess('84-33-44.2').frac + S)
DK1K5  = pv(Deg.guess('7.8383177').frac + P)
DK1K6  = vp(Deg.guess('23-15-32.7').frac + P)
DK1K7  = pv(Deg.guess('126.2540802').frac + K)
DK1K8  = pv(Deg.guess('205-29-57.8').frac + K)
DK1K9  = rs(Deg.guess('101.7366025').frac + S)
DK1K10 = sv(Deg.guess('160-23-45.2').frac + T)
DK1K11 = pv(Deg.guess('79.8680017').frac + K)
DK1K12 = vs(Deg.guess('52-28-42.4').frac + R)
DK1K13 = sr(Deg.guess('109-01-49.8').frac + T)
DK2K1  = vs(Deg.guess('84-00-34.4').frac + L)
DK2K2  = rs(Deg.guess('76.1245808').frac + N)
DK2K3  = pr(Deg.guess('54-13-28.3').frac + P)
DK2K4  = rp(Deg.guess('182.7394778').frac + S)
DK2K5  = sr(Deg.guess('162-45-25.7').frac + L)
DK2K6  = pr(Deg.guess('60-41-55.2').frac + S)
DK2K7  = rp(Deg.guess('69.4792556').frac + R)
DK2K8  = rp(Deg.guess('130-50-06.1').frac + L)
DK2K9  = vs(Deg.guess('84-08-54.3').frac + K)

# Answer angles
K1K1  = Deg.guess('84-03-08.3').frac + P
K1K2  = Deg.guess('112-58-25.4').frac + S
K1K3  = Deg.guess('54.3107235').frac + L
K1K4  = Deg.guess('84-33-44.2').frac + S
K1K5  = Deg.guess('7.8383177').frac + P
K1K6  = Deg.guess('23-15-32.7').frac + P
K1K7  = Deg.guess('126.2540802').frac + K
K1K8  = Deg.guess('205-29-57.8').frac + K
K1K9  = Deg.guess('101.7366025').frac + S
K1K10 = Deg.guess('160-23-45.2').frac + T
K1K11 = Deg.guess('79.8680017').frac + K
K1K12 = Deg.guess('52-28-42.4').frac + R
K1K13 = Deg.guess('109-01-49.8').frac + T
K2K1  = Deg.guess('84-00-34.4').frac + L
K2K2  = Deg.guess('76.1245808').frac + N
K2K3  = Deg.guess('54-13-28.3').frac + P
K2K4  = Deg.guess('182.7394778').frac + S
K2K5  = Deg.guess('162-45-25.7').frac + L
K2K6  = Deg.guess('60-41-55.2').frac + S
K2K7  = Deg.guess('69.4792556').frac + R
K2K8  = Deg.guess('130-50-06.1').frac + L
K2K9  = Deg.guess('84-08-54.3').frac + K

rek_kaina = Dec('871.29')
rek_plotas = Dec('97895.626')

nauj_kaina = Dec('545.84') / 22
nauj_plotas = Dec('34469.766')

ekspl_kaina = Dec('16.48') / 8
ekspl_plotas = Dec('22960.319')

visa_kaina = (
        rek_kaina * rek_plotas +
        nauj_kaina * nauj_plotas +
        ekspl_kaina * ekspl_plotas
)

H1 = 4.82
SK1 = 41.08
A1 = H1 * tan(SK1 * pi / 180)

H2 = 20.38
SK2 = 17.69
A2 = H2 * tan(SK2 * pi / 180)

if __name__ == '__main__':
    print("""Sklypu pradiniu tasku (1 ir 15) koordinates:
    Atkarpos:
    1L-1  = %7.3f""" % (Dec('125.829') + G) + """
    1L-2  = %7.3f""" % (Dec('81.682') + E) + """
    1L-3  = %7.3f""" % (Dec('61.206') + H) + """
    1L-4  = %7.3f""" % (Dec('121.055') + D) + """
    1L-5  = %7.3f""" % (Dec('79.892') + B) + """
    1L-6  = %7.3f""" % (Dec('159.299') + H) + """
    1L-7  = %7.3f""" % (Dec('76.500') + E) + """
    1L-8  = %7.3f""" % (Dec('51.091') + G) + """
    1L-9  = %7.3f""" % (Dec('93.765') + F) + """
    1L-10 = %7.3f""" % (Dec('58.926') + D) + """
    1L-11 = %7.3f""" % (Dec('79.061') + M) + """
    1L-12 = %7.3f""" % (Dec('121.209') + D) + """
    1L-13 = %7.3f""" % (Dec('94.071') + C) + """
     
    2L-1 = %7.3f""" % (Dec('205.221') + C) + """
    2L-2 = %7.3f""" % (Dec('122.820') + G) + """
    2L-3 = %7.3f""" % (Dec('178.657') + H) + """
    2L-4 = %7.3f""" % (Dec('116.987') + B) + """
    2L-5 = %7.3f""" % (Dec('84.793') + H) + """
    2L-6 = %7.3f""" % (Dec('138.291') + F) + """
    2L-7 = %7.3f""" % (Dec('85.607') + H) + """
    2L-8 = %7.3f""" % (Dec('114.589') + G) + """
    2L-9 = %7.3f""" % (Dec('79.210') + D) + """

    Kampai:
    1K-1  = %s""" % fmt(pr(Deg.guess('84-03-08.3').frac + P)) + """
    1K-2  = %s""" % fmt(rp(Deg.guess('112-58-25.4').frac + S)) + """
    1K-3  = %s""" % fmt(vp(Deg.guess('54.3107235').frac + L)) + """
    1K-4  = %s""" % fmt(pr(Deg.guess('84-33-44.2').frac + S)) + """
    1K-5  = %s""" % fmt(pv(Deg.guess('7.8383177').frac + P)) + """
    1K-6  = %s""" % fmt(vp(Deg.guess('23-15-32.7').frac + P)) + """
    1K-7  = %s""" % fmt(pv(Deg.guess('126.2540802').frac + K)) + """
    1K-8  = %s""" % fmt(pv(Deg.guess('205-29-57.8').frac + K)) + """
    1K-9  = %s""" % fmt(rs(Deg.guess('101.7366025').frac + S)) + """
    1K-10 = %s""" % fmt(sv(Deg.guess('160-23-45.2').frac + T)) + """
    1K-11 = %s""" % fmt(pv(Deg.guess('79.8680017').frac + K)) + """
    1K-12 = %s""" % fmt(vs(Deg.guess('52-28-42.4').frac + R)) + """
    1K-13 = %s""" % fmt(sr(Deg.guess('109-01-49.8').frac + T)) + """

    2K-1  = %s""" % fmt(vs(Deg.guess('84-00-34.4').frac + L)) + """
    2K-2  = %s""" % fmt(rs(Deg.guess('76.1245808').frac + N)) + """
    2K-3  = %s""" % fmt(pr(Deg.guess('54-13-28.3').frac + P)) + """
    2K-4  = %s""" % fmt(rp(Deg.guess('182.7394778').frac + S)) + """
    2K-5  = %s""" % fmt(sr(Deg.guess('162-45-25.7').frac + L)) + """
    2K-6  = %s""" % fmt(pr(Deg.guess('60-41-55.2').frac + S)) + """
    2K-7  = %s""" % fmt(rp(Deg.guess('69.4792556').frac + R)) + """
    2K-8  = %s""" % fmt(rp(Deg.guess('130-50-06.1').frac + L)) + """
    2K-9  = %s""" % fmt(vs(Deg.guess('84-08-54.3').frac + K))
    )
