#!/usr/bin/python3

from shapely.geometry import LineString, box

from task2_1 import (
        loksodroma as cilindr_loksodroma,
        ortodroma as cilindr_ortodroma,
        yx as cilindr_yx
)
from task2_2 import (
        loksodroma as kugine_loksodroma,
        ortodroma as kugine_ortodroma
)
from task2_4 import loksodromos_ilgis, ortodromos_ilgis
from consts import M, maxlambda

# mastelių koeficientų lentelė
mLentele = (
    ((10, 16), 0.897),
    ((16, 22), 0.919),
    ((22, 28), 0.952),
    ((28, 34), 1.000),
    ((34, 40), 1.065),
    ((40, 46), 1.152),
    ((46, 52), 1.270),
)

# Kūginė projekcija: loksodroma
apsk_kugine_loksodroma = LineString(kugine_loksodroma).length * M / 1000
proc_kugine_loksodroma = 100*(loksodromos_ilgis-apsk_kugine_loksodroma)/loksodromos_ilgis
# Kūginė projekcija: ortodroma
apsk_kugine_ortodroma = LineString(kugine_ortodroma).length * M / 1000
proc_kugine_ortodroma = 100*(ortodromos_ilgis-apsk_kugine_ortodroma)/apsk_kugine_ortodroma


# Merkatoriaus projekcija (cilindrinė)
def apsk_cilindr(linija):
    """Apskaičiuoti duotos linijos ilgį cilindrinėje projekcijoje.

    Liniją padalina į dalis pagal mLentele koordinates, ir
    sudeda kiekvieno segmento ilgį padauginus iš koeficiento.
    """
    ls = LineString(linija)
    total = 0
    for (phifrom, phito), coeff in mLentele:
        # stačiakampis, apribojantis liniją
        poly = box(*cilindr_yx(phifrom, 0), *cilindr_yx(phito, maxlambda))
        # stačiakampio ir linijos sankirta -- gauname tik liniją, kurios ilgį
        # reikia priskaičiuoti
        subline = ls.intersection(poly)
        # pridedame santykinį linijos ilgį prie sumos
        total += subline.length * coeff
    return total * M / 1000


matav_cilindr_ortodroma = apsk_cilindr(cilindr_ortodroma)
proc_cilindr_ortodroma = 100*(ortodromos_ilgis-matav_cilindr_ortodroma)/ortodromos_ilgis
matav_cilindr_loksodroma = apsk_cilindr(cilindr_loksodroma)
proc_cilindr_loksodroma = 100*(loksodromos_ilgis-matav_cilindr_loksodroma)/loksodromos_ilgis


tpl = """Sferinės loksodromos ilgis (m): {loksodromos_ilgis:.0f}
Sferinės ortodromos ilgis (m): {ortodromos_ilgis:.0f}

Apskaičiuotas kūginės loksodromos ilgis (m):     {apsk_kugine_loksodroma:.0f}  paklaida: {proc_kugine_loksodroma:+.2f}%
Apskaičiuotas kūginės ortodromos ilgis (m):      {apsk_kugine_ortodroma:.0f}  paklaida: {proc_kugine_ortodroma:+.2f}%
Apskaičiuotas cilindrinės loksodromos ilgis (m): {matav_cilindr_loksodroma:.0f}  paklaida: {proc_cilindr_loksodroma:+.2f}%
Apskaičiuotas cilindrinės ortodromos ilgis (m):  {matav_cilindr_ortodroma:.0f}  paklaida: {proc_cilindr_ortodroma:+.2f}%"""

if __name__ == '__main__':
    print(tpl.format(**dict(locals())))
