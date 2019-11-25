#!/usr/bin/env python3
from collections import namedtuple
from decimal import Decimal as Dec

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
    def __init__(self, point, length, angle, dirang=Dec()):
        self.point = point
        self.len = length
        self.ang = angle
        self.dirang = dirang
        self.coords = Point(Dec(), Dec())
    def __str__(self):
        return "%2d:  len:%7.3f  ang:%8.4f  dirang:%8.4f  acadcoords:(%.3f,%.3f)" % \
                (self.point, self.len, self.ang,
                        self.dirang, self.coords.acadx, self.coords.acady)

A= Dec('6.094')
B= Dec('-2.923')
C= Dec('-13.462')
N= Dec('9.512')

# Directional coords + angle
X11 = Dec('6091968.055')
Y11 = Dec('485944.146')
A11_2 = guess('70-16-17')

vertices = [
  #  point   len             angle               dirangle
  Vertex(11, Dec('164.126'), guess('103-03-03'), A11_2),
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
    v.dirang = vertices[i].dirang + 180 - v.ang

if __name__ == '__main__':
    print("""
    Pradinis direkcinis kampas: %.4f""" % (90 - A11_2) + """
    """)

    print("angle sum %.4f, theoretical angle sum %d" % \
            (angle_sum, theoretical_angle_sum))

    for v in vertices:
        print(v)
