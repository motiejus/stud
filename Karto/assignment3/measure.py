#!/usr/bin/env python3
from decimal import Decimal as Dec
from deg import Deg

def fmt(deg):
    if deg > 180:
        deg -= 360
    elif deg < -180:
        deg += 360
    return "%12.7f" % deg

def pr(deg): return fmt(270 + deg)
def pv(deg): return fmt(270 - deg)
def vp(deg): return fmt(180 + deg)
def vs(deg): return fmt(180 - deg)
def sv(deg): return fmt(90 + deg)
def sr(deg): return fmt(90 - deg)
def rs(deg): return fmt(deg)
def rp(deg): return fmt(360 - deg)

# Sklypu pradiniu tasku (1 ir 15) koordinates:
X1 = Dec('16639.290')
Y1 = Dec('25500.960')
X15 = Dec('17191.590')
Y15 = Dec('25121.430')

# Sklypu sujungimo tasko T3 koordinates:
XT3 = Dec('16971.790')
YT3 = Dec('26685.160')

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

print("""Sklypu pradiniu tasku (1 ir 15) koordinates:
X1 = 16639.290
Y1 = 25500.960
X15 = 17191.590
Y15 = 25121.430

Sklypu sujungimo tasko T3 koordinates:
XT3 = 16971.790
YT3 = 26685.160

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
1K-1  = %s""" % pr(Deg.guess('84-03-08.3').frac + P) + """
1K-2  = %s""" % rp(Deg.guess('112-58-25.4').frac + S) + """
1K-3  = %s""" % vp(Deg.guess('54.3107235').frac + L) + """
1K-4  = %s""" % pr(Deg.guess('84-33-44.2').frac + S) + """
1K-5  = %s""" % pv(Deg.guess('7.8383177').frac + P) + """
1K-6  = %s""" % vp(Deg.guess('23-15-32.7').frac + P) + """
1K-7  = %s""" % pv(Deg.guess('126.2540802').frac + K) + """
1K-8  = %s""" % pv(Deg.guess('205-29-57.8').frac + K) + """
1K-9  = %s""" % rs(Deg.guess('101.7366025').frac + S) + """
1K-10 = %s""" % sv(Deg.guess('160-23-45.2').frac + T) + """
1K-11 = %s""" % pv(Deg.guess('79.8680017').frac + K) + """
1K-12 = %s""" % vs(Deg.guess('52-28-42.4').frac + R) + """
1K-13 = %s""" % sr(Deg.guess('109-01-49.8').frac + T) + """

2K-1  = %s""" % vs(Deg.guess('84-00-34.4').frac + L) + """
2K-2  = %s""" % rs(Deg.guess('76.1245808').frac + N) + """
2K-3  = %s""" % pr(Deg.guess('54-13-28.3').frac + P) + """
2K-4  = %s""" % rp(Deg.guess('182.7394778').frac + S) + """
2K-5  = %s""" % sr(Deg.guess('162-45-25.7').frac + L) + """
2K-6  = %s""" % pr(Deg.guess('60-41-55.2').frac + S) + """
2K-7  = %s""" % rp(Deg.guess('69.4792556').frac + R) + """
2K-8  = %s""" % rp(Deg.guess('130-50-06.1').frac + L) + """
2K-9  = %s""" % vs(Deg.guess('84-08-54.3').frac + K)
)
