
from decimal import Decimal

def deg(deg, mm, ss):
    return (Decimal(deg) +
        Decimal(mm) / Decimal(60) +
        Decimal(ss) / Decimal(3600)).normalize()
