from decimal import Decimal

class Deg:
    def __str__(self):
        return "%03d - %02d - %02d" % (self.deg, self.mm, self.ss)

    def __init__(self, deg, mm, ss):
        self.deg = Decimal(deg)
        self.mm = Decimal(mm)
        self.ss = Decimal(ss)

    @staticmethod
    def from_1(deg):
        assert isinstance(deg, Decimal)

        pdeg, pmm = divmod(deg, 1)
        pmm = pmm * Decimal(60)
        pmm, pss = divmod(pmm, 1)
        pss = pss * Decimal(60)
        return Deg(pdeg, pmm, pss)

    def frac(self):
        return (
            self.deg +
            self.mm / Decimal(60) +
            self.ss / Decimal(3600)).normalize()
