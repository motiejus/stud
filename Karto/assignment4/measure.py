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

class PAL(namedtuple('PAL', ['point', 'ang', 'len'])):
    def __str__(self):
        return "%2d: ang:%8.4f len:%7.3f" % (self.point, self.ang, self.len)

A= Dec('6.094')
B= Dec('-2.923')
C= Dec('-13.462')
N= Dec('9.512')

X11 = Dec('6091968.055')
Y11 = Dec('485944.146')

A11_2 = guess('70-16-17')

# point angle length
pals = [
  PAL(11, guess('103-03-03'), Dec('164.126')),
  PAL(2,  guess('218-27-42'), Dec('149.851')),
  PAL(19, guess('211-44-30'), Dec('82.384') ),
  PAL(3,  guess('67-26-49') , Dec('259.022')),
  PAL(24, guess('67-33-06') , Dec('319.331')),
  PAL(12, guess('279-03-59'), Dec('74.764') ),
  PAL(13, guess('278-54-55'), Dec('81.640') ),
  PAL(14, guess('119-27-45'), Dec('31.888') ),
  PAL(15, guess('160-50-28'), Dec('84.073') ),
  PAL(16, guess('207-42-31'), Dec('70.072') ),
  PAL(17, guess('206-18-01'), Dec('73.378') ),
  PAL(10, guess('90-55-10') , Dec('66.625') ),
  PAL(18, guess('100-18-10'), Dec('97.003') ),
  PAL(9,  guess('148-30-56'), Dec('121.003')),
  PAL(8,  guess('285-20-57'), Dec('131.915')),
  PAL(23, guess('29-44-22') , Dec('102.086')),
  PAL(22, guess('276-33-49'), Dec('158.324')),
  PAL(7,  guess('82-07-47') , Dec('72.157') ),
  PAL(6,  guess('104-15-46'), Dec('107.938')),
  PAL(21, guess('234-17-37'), Dec('104.082')),
  PAL(5,  guess('283-30-57'), Dec('154.332')),
  PAL(20, guess('152-15-58'), Dec('68.972') ),
  PAL(1,  guess('101-20-01'), Dec('151.531')),
  PAL(4,  guess('150-15-41'), Dec('179.336')),
]

if __name__ == '__main__':
    print("""
    Pradinis direkcinis kampas: %.4f""" % (90 - A11_2) + """
    """)


    for i in pals:
        print(i)
