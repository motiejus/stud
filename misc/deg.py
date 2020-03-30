from collections import namedtuple


from decimal import Decimal as Dec


class Deg(namedtuple('Deg', ['deg', 'mm', 'ss'])):
    def __str__(self):
        return "%03d-%02d-%.1f" % (self.deg, self.mm, self.ss)


def guess(inp):
    if isinstance(inp, str) and '-' in inp:
        deg, mm, ss = inp.split('-')
        ddeg, dmm, dss = Dec(deg), Dec(mm), Dec(ss)
        return ddeg + dmm/60 + dss/3600
    else:
        return Dec(inp)


def hms(deg):
    assert isinstance(deg, Dec)
    pdeg, pmm = divmod(deg, 1)
    pmm = pmm * Dec(60)
    pmm, pss = divmod(pmm, 1)
    pss = pss * Dec(60)
    return Deg(pdeg, pmm, pss)
