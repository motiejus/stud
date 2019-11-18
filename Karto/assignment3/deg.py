from decimal import Decimal as D

class Deg:
    def __str__(self):
        return "%03d-%02d-%04.2f" % (self.deg, self.mm, self.ss)

    def __init__(self, deg, mm, ss):
        self.deg = D(deg)
        self.mm = D(mm)
        self.ss = D(ss)

    @classmethod
    def from_1(cls, deg):
        assert isinstance(deg, D)

        pdeg, pmm = divmod(deg, 1)
        pmm = pmm * D(60)
        pmm, pss = divmod(pmm, 1)
        pss = pss * D(60)
        return cls(pdeg, pmm, pss)

    @classmethod
    def guess(cls, instr):
        if '-' in instr:
            deg, mm, ss = instr.split('-')
            return Deg(deg, mm, ss)
        return cls.from_1(D(instr))

    @property
    def frac(self):
        return (
            self.deg +
            self.mm / D(60) +
            self.ss / D(3600)).normalize()


import unittest
class TestDeg(unittest.TestCase):
    def test_deg(self):
        w = Deg.guess('125.505')
        self.assertEqual(125, w.deg)
        self.assertEqual(30, w.mm)
        self.assertEqual(18, w.ss)

    def test_guess(self):
        w = Deg.guess('112-58-25.4')
        self.assertEqual(112, w.deg)
        self.assertEqual(58, w.mm)
        self.assertEqual(D('25.4'), w.ss)
        frac = "%3.7f" % w.frac
        self.assertEqual('112.9737222', frac)

    def test_str_lower(self):
        w = Deg(120, 1, 42.541)
        self.assertEqual("120-01-42.54", str(w))

    def test_str_upper(self):
        w = Deg(120, 1, 42.545)
        self.assertEqual("120-01-42.55", str(w))
