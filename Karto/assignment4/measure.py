#!/usr/bin/env python3
from collections import namedtuple
from decimal import Decimal as Dec
from math import sin, cos, pi

def normalize(ang):
    while ang > 180:
        ang -= 360
    while ang <= -180:
        ang += 360
    return ang

def guess(inp):
    if isinstance(inp, str) and '-' in inp:
        deg, mm, ss = inp.split('-')
        ddeg, dmm, dss = Dec(deg), Dec(mm), Dec(ss)
        return ddeg + dmm/60 + dss/3600
    else:
        return Dec(instr)

class Point(namedtuple('Point', ['acadx', 'acady'])):
    @property
    def lksx(self):
        return self.acady
    @property
    def lksy(self):
        return self.acadx

class Vertex:
    def __init__(self, point, length, angle, dirang=Dec(), coords = Point(Dec(), Dec())):
        self.point = point
        self.len = length
        self.ang = angle
        self.dirang = dirang
        self.coords = coords

A = Dec('6.094')
B = Dec('-2.923')
C = Dec('-13.462')
N = Dec('9.512')

L1 = Dec('16.321')
# === Kelias A-05 ===
L2 = Dec('9.109')
L3 = Dec('4.819')
# === Kelias A-08 ===
L4 = Dec('2.675')
L5 = Dec('2.059')
L6 = Dec('1.262')
L7 = Dec('4.170')
L8 = Dec('6.005')
L9 = Dec('6.453')
# === Griovys G-11 ===
L10 = Dec('4.882')
L11 = Dec('3.305')
L12 = Dec('2.210')
L13 = Dec('4.381')

A05_plotis = L2 + L3
A08_plotis = sum([L4,L5,L6,L7,L8,L9])
G11_plotis = sum([L10,L11,L12,L13])

# Directional coords + angle
X11 = Dec('6091968.055')
Y11 = Dec('485944.146')
A11_2 = guess('70-16-17')

vertices = [
  #  point   len             angle               dirangle  coords
  Vertex(11, Dec('164.126'), guess('103-03-03'), A11_2,    Point(X11, Y11)),
  Vertex(2,  Dec('149.851'), guess('218-27-42')),
  Vertex(19, Dec('82.384' ), guess('211-44-30')),
  Vertex(3,  Dec('259.022'), guess('67-26-49' )),
  Vertex(24, Dec('319.331'), guess('67-33-06' )),
  Vertex(12, Dec('74.764' ), guess('279-03-59')),
  Vertex(13, Dec('81.640' ), guess('278-54-55')),
  Vertex(14, Dec('31.888' ), guess('119-27-45')),
  Vertex(15, Dec('84.073' ), guess('160-50-28')),
  Vertex(16, Dec('70.072' ), guess('207-42-31')),
  Vertex(17, Dec('73.378' ), guess('206-18-01')),
  Vertex(10, Dec('66.625' ), guess('90-55-10' )),
  Vertex(18, Dec('97.003' ), guess('100-18-10')),
  Vertex(9,  Dec('121.003'), guess('148-30-56')),
  Vertex(8,  Dec('131.915'), guess('285-20-57')),
  Vertex(23, Dec('102.086'), guess('29-44-22' )),
  Vertex(22, Dec('158.324'), guess('276-33-49')),
  Vertex(7,  Dec('72.157' ), guess('82-07-47' )),
  Vertex(6,  Dec('107.938'), guess('104-15-46')),
  Vertex(21, Dec('104.082'), guess('234-17-37')),
  Vertex(5,  Dec('154.332'), guess('283-30-57')),
  Vertex(20, Dec('68.972' ), guess('152-15-58')),
  Vertex(1,  Dec('151.531'), guess('101-20-01')),
  Vertex(4,  Dec('179.336'), guess('150-15-41')),
]

angle_sum = Dec(0)
for v in vertices:
    angle_sum += v.ang
theoretical_angle_sum = Dec(int((len(vertices)-2)*180))

for i, v in enumerate(vertices[1:]):
    prev = vertices[i]
    v.dirang = prev.dirang + 180 - v.ang
    dx = Dec(float(prev.len) * cos(float(prev.dirang) * pi/180))
    dy = Dec(float(prev.len) * sin(float(prev.dirang) * pi/180))
    v.coords = Point(prev.coords.acadx + dx, prev.coords.acady + dy)


"""
Kelio A-03 plotis = 17.401 + A =
Kelio A-05 plotis = 13.705 + B =
Kelio A-08 plotis = 29.006 + C =
Griovio G-11 plotis = 14.776 + N =
"""

KA03_plotis = Dec('17.401') + A
KA05_plotis = Dec('13.705') + B
KA08_plotis = Dec('29.006') + C
G11_plotis = Dec('14.776') + N

# 9-kampio krastine D1
D1 = Dec('174.667') + C
# Daugiakampio pasukimo kampas (K1)
K1 = Dec('13.147') + B
# Atstumas iki tikrosios uzliejimo zonos (A1) (0.001 tikslumu)
A1 = Dec('67.536') + B

if __name__ == '__main__':
    print("angle sum %.4f, theoretical angle sum %d" % \
            (angle_sum, theoretical_angle_sum))

    for i, v in enumerate(vertices):
        nxt = vertices[0 if i == len(vertices) - 1 else i+1]

        pts = "%d-%d" % (v.point, nxt.point)
        draw = "@%.3f<%.4f" % (v.len, normalize(90 - v.dirang))
        print("%5s: %19s  acadcoords:(%.3f,%.3f)" % \
                (pts, draw, v.coords.acadx, v.coords.acady))

    print("""
    Kelio A-03 plotis = 17.401 + A = %.3f""" % KA03_plotis + """
    Kelio A-05 plotis = 13.705 + B = %.3f""" % KA05_plotis + """
    Kelio A-08 plotis = 29.006 + C = %.3f""" % KA08_plotis + """
    Griovio G-11 plotis = 14.776 + N = %.3f""" % G11_plotis + """

    Prognozuojamo uzliejimo zona, tai taisyklingas 9-kampis
    9-kampio krastine D1 = %.3f""" % D1 + """
    Daugiakampio pasukimo kampas (K1) (0.0001 laipsnio tikslumu)
    K1 = %.4f""" % K1 + """

    Tikroji uzliejimo zona, tai taisyklingas apskritimas, kurio centras TURI SUTAPTI su daugiakampio centru.
    Atstumas iki tikrosios uzliejimo zonos (A1) (0.001 tikslumu)
    A1 = %.3f""" % A1 + """
    """)
