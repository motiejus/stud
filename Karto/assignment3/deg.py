from decimal import Decimal

class Deg:
    def __str__(self):
        return "%03d-%02d-%04.2f" % (self.deg, self.mm, self.ss)

    def __init__(self, deg, mm, ss):
        self.deg = Decimal(deg)
        self.mm = Decimal(mm)
        self.ss = Decimal(ss)

    @classmethod
    def from_1(cls, deg):
        assert isinstance(deg, Decimal)

        pdeg, pmm = divmod(deg, 1)
        pmm = pmm * Decimal(60)
        pmm, pss = divmod(pmm, 1)
        pss = pss * Decimal(60)
        return cls(pdeg, pmm, pss)

    @classmethod
    def guess(cls, instr):
        if '-' in instr:
            deg, mm, ss = instr.split('-')
            return Deg(deg, mm, ss)
        return cls.from_1(Decimal(instr))

    def frac(self):
        return (
            self.deg +
            self.mm / Decimal(60) +
            self.ss / Decimal(3600)).normalize()


import unittest
class TestDeg(unittest.TestCase):
    def test_deg(self):
        w = Deg.guess('125.5')
        self.assertEqual(125, w.deg)
        self.assertEqual(30, w.mm)
        self.assertEqual(0, w.ss)

    def test_str_lower(self):
        w = Deg(120, 1, 42.541)
        self.assertEqual("120-01-42.54", str(w))

    def test_str_upper(self):
        w = Deg(120, 1, 42.545)
        self.assertEqual("120-01-42.55", str(w))
