#!/usr/bin/env python3
from decimal import Decimal

from deg import Deg

# Pataisos ATKARPOMS:
A = Decimal('-2.207')
B = Decimal('1.999')
C = Decimal('4.838')
D = Decimal('2.862')
E = Decimal('-5.907')
F = Decimal('-3.744')
G = Decimal('-1.466')
H = Decimal('6.841')
M = Decimal('-4.824')

# Pataisos KAMPAMS:
K = Decimal('-7.7422786')
L = Decimal('-6.6428275')
N = Decimal('-4.2872043')
P = Decimal('-3.1145084')
R = Decimal('-7.2564859')
S = Decimal('3.8874407')
T = Decimal('-8.7554531')
 
# Sklypu pradiniu tasku (1 ir 15) koordinates:
X1 = Decimal('16639.290')
Y1 = Decimal('25500.960')
X15 = Decimal('17191.590')
Y15 = Decimal('25121.430')

# Sklypu sujungimo tasko T3 koordinates:
XT3 = Decimal('16971.790')
YT3 = Decimal('26685.160')

print("""
Atkarpos:
1L-1 = 125.829 + G = %.3f""" % (Decimal('125.829') + G) + """
1L-2 = 81.682 + E = %.3f""" % (Decimal('81.682') + E) + """
1L-3 = 61.206 + H = %.3f""" % (Decimal('61.206') + H) + """
1L-4 = 121.055 + D = %.3f""" % (Decimal('121.055') + D) + """
1L-5 = 79.892 + B = %.3f""" % (Decimal('79.892') + B) + """
1L-6 = 159.299 + H = %.3f""" % (Decimal('159.299') + H) + """
1L-7 = 76.500 + E = %.3f""" % (Decimal('76.500') + E) + """
1L-8 = 51.091 + G = %.3f""" % (Decimal('51.091') + G) + """
1L-9 = 93.765 + F = %.3f""" % (Decimal('93.765') + F) + """
1L-10 = 58.926 + D = %.3f""" % (Decimal('58.926') + D) + """
1L-11 = 79.061 + M = %.3f""" % (Decimal('79.061') + M) + """
1L-12 = 121.209 + D = %.3f""" % (Decimal('121.209') + D) + """
1L-13 = 94.071 + C = %.3f""" % (Decimal('94.071') + C) + """
 
2L-1 = 205.221 + C = %.3f""" % (Decimal('205.221') + C) + """
2L-2 = 122.820 + G = %.3f""" % (Decimal('122.820') + G) + """
2L-3 = 178.657 + H = %.3f""" % (Decimal('178.657') + H) + """
2L-4 = 116.987 + B = %.3f""" % (Decimal('116.987') + B) + """
2L-5 = 84.793 + H = %.3f""" % (Decimal('84.793') + H) + """
2L-6 = 138.291 + F = %.3f""" % (Decimal('138.291') + F) + """
2L-7 = 85.607 + H = %.3f""" % (Decimal('85.607') + H) + """
2L-8 = 114.589 + G = %.3f""" % (Decimal('114.589') + G) + """
2L-9 = 79.210 + D = %.3f""" % (Decimal('79.210') + D) + """

Kampai:
1K-1(L-M-S) = 84-03-08.3 + P
1K-2(L-M-S) = 112-58-25.4 + S
1K-3(L) = 54.3107235 + L
1K-4(L-M-S) = 84-33-44.2 + S
1K-5(L) = 7.8383177 + P
1K-6(L-M-S) = 23-15-32.7 + P
1K-7(L) = 126.2540802 + K
1K-8(L-M-S) = 205-29-57.8 + K
1K-9(L) = 101.7366025 + S
1K-10(L-M-S) = 160-23-45.2 + T
1K-11(L) = 79.8680017 + K
1K-12(L-M-S) = 52-28-42.4 + R
1K-13(L-M-S) = 109-01-49.8 + T

2K-1(L-M-S) = 84-00-34.4 + L
2K-2(L) = 76.1245808 + N
2K-3(L-M-S) = 54-13-28.3 + P
2K-4(L) = 182.7394778 + S
2K-5(L-M-S) = 162-45-25.7 + L
2K-6(L-M-S) = 60-41-55.2 + S
2K-7(L) = 69.4792556 + R
2K-8(L-M-S) = 130-50-06.1 + L
2K-9(L-M-S) = 84-08-54.3 + K

# Iskasu parametrai:
Iskasos Nr.1 gylis H1 = 4.82(m)
Iskasos Nr.1 slaito polinkio kampas SK1 = 41.08(laipsniai)
Iskasos Nr.2 gylis H2 = 20.38(m)
Iskasos Nr.2 slaito polinkio kampas SK2 = 17.69(laipsniai)
""")
