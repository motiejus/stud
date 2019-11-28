from math import pi

def deg(inp):
    """return angle in radians"""
    if isinstance(inp, str) and '-' in inp:
        deg, mm, ss = inp.split('-')
        ddeg, dmm, dss = float(deg), float(mm), float(ss)
        deg = ddeg + dmm/60 + dss/3600
    else:
        deg = float(instr)

    return deg * pi / 180
