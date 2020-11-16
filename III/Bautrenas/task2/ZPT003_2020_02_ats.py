#!/usr/bin/python3
from math import pi

def nupjauto_kugio_turis(h, d1, d2):
    r1, r2 = d1/2, d2/2
    return pi/3*h*(r1**2 + r1*r2 + r2**2)

storgalio_apimtis_su_zieve=119.4 # cm
plongalio_apimtis_su_zieve=46.2  # cm
storgalio_skersmuo_su_zieve=storgalio_apimtis_su_zieve/pi  # cm
plongalio_skersmuo_su_zieve=plongalio_apimtis_su_zieve/pi  # cm

rastu_kiekis=5
rastu_ilgis=5.38 # m
storgalio_zieves_storis=10.6 # mm
plongalio_zieves_storis=10.5 # mm
storgalio_skersmuo_be_zieves=round(storgalio_skersmuo_su_zieve-storgalio_zieves_storis/10*2+.5) # cm
plongalio_skersmuo_be_zieves=round(plongalio_skersmuo_su_zieve-plongalio_zieves_storis/10*2+.5) # cm

vieno_rasto_turis=nupjauto_kugio_turis(rastu_ilgis, plongalio_skersmuo_be_zieves/100, storgalio_skersmuo_be_zieves/100) # m3
visu_rastu_turis=vieno_rasto_turis*rastu_kiekis # m3
medienos_svoris=800 # kg/m3
visu_rastu_svoris=visu_rastu_turis*medienos_svoris # kg
gaunamas_popieriaus_kiekis_perc=6.82 # [0-100]%
gaunamas_popieriaus_kiekis_trupm=gaunamas_popieriaus_kiekis_perc/100 # [0-1]
medienos_svoris_popieriaus_gaminimui=visu_rastu_svoris*gaunamas_popieriaus_kiekis_trupm # kg
popieriaus_tankis=0.09 # kg/m2
viso_pagaminto_popieriaus_plotas=medienos_svoris_popieriaus_gaminimui/popieriaus_tankis # m2
vieno_lapo_plotas=.75*.9 # m2
pagaminta_popieriaus_lapu=int(viso_pagaminto_popieriaus_plotas/vieno_lapo_plotas) # kiekis

tpl="""Uzduoties Nr. 
ZPT003_2020_02
Skaiciavo(Pavarde Vardas):
Jakstys_Motiejus
==== POPIERIUS ====
Gaminamo popieriaus pavadinimas pvz. ULTRA/62 (duota) 
Ultra3C
Gaminamo popieriaus lapo plotis W (mm) 
750
Gaminamo popieriaus lapo ilgis L (mm) 
900
Gaminamo popieriaus metro kv. svoris  (g/m2) 
95
1.   Popierius gaminamas is medienos pvz. AZUOLAS (duota) 
Baltalksnis
Popieriaus gamybos metodas (nurodytas) 
Cheminis/Sulfitinis
Rastu kiekis (duotas)
5
Storgalio apimtis cm (0.0) (duota)
{storgalio_apimtis_su_zieve:.1f}
Plongalio apimtis cm (0.0) (duota)
{plongalio_apimtis_su_zieve:.1f}
Rastu ilgis (duotas)
{rastu_ilgis:.2f}
== Skaiciavimai ==
Apskaiciuotas STORGALIO skersmuo su zieve (0.00 cm tikslumu)
{storgalio_skersmuo_su_zieve:.2f}
Storgalio zieves storis (is lenteles 0.0 mm tikslumu)
{storgalio_zieves_storis:.1f}
Storgalio skersmuo (be zv.) su pataisa del rasto nelygumo (0.00 cm tikslumu)
{storgalio_skersmuo_be_zieves:.2f}
Apskaiciuotas PLONGALIO skersmuo su zieve (0.00 cm tikslumu)
{plongalio_skersmuo_su_zieve:.2f}
Plongalio zieves storis (is lenteles 0.0 mm tikslumu)
{plongalio_zieves_storis:.1f}
Plongalio (be zv.) skersmuo su pataisa del rasto nelygumo (0.00 cm tikslumu)
{plongalio_skersmuo_be_zieves:.2f}
VIENO rasto turis (0.000 m3 tikslumu)
{vieno_rasto_turis:.3f}
VISU rastu turis (0.000 m3 tikslumu)
{visu_rastu_turis:.3f}
Visu rastu Medienos svoris (0.000 kg tikslumu)
{visu_rastu_svoris:.3f}
Gaunamas popieriaus kiekis priklausomai muo gamybos metodo (% duota)
{gaunamas_popieriaus_kiekis_perc:.2f}
Medienos svoris popieriaus gaminimui (0.000 kg tikslumu)
{medienos_svoris_popieriaus_gaminimui:.3f}
Viso pagaminto popieriaus plotas (0.000 m2 tikslumu)
{viso_pagaminto_popieriaus_plotas:.3f}
Vieno gaminamo lapo plotas (0.000 m2 tikslumu)
{vieno_lapo_plotas:.3f}
Pagaminta popieriaus lapu (vnt.)
{pagaminta_popieriaus_lapu}
2.   Popierius gaminamas is medienos pvz. AZUOLAS (duota) 
*******
Popieriaus gamybos metodas (nurodytas) 
*******
Rastu kiekis (duotas)
*******
Storgalio apimtis cm (0.0) (duota)
*******
Plongalio apimtis cm (0.0) (duota)
*******
Rastu ilgis (duotas)
*******
== Skaiciavimai ==
Apskaiciuotas STORGALIO skersmuo su zieve (0.00 cm tikslumu)
*******
Storgalio zieves storis (is lenteles 0.0 mm tikslumu)
*******
Storgalio skersmuo (be zv.) su pataisa del rasto nelygumo (0.00 cm tikslumu)
*******
Apskaiciuotas PLONGALIO skersmuo su zieve (0.00 cm tikslumu)
*******
Plongalio zieves storis (is lenteles 0.0 mm tikslumu)
*******
Plongalio (be zv.) skersmuo su pataisa del rasto nelygumo (0.00 cm tikslumu)
*******
VIENO rasto turis (0.000 m3 tikslumu)
*******
VISU rastu turis (0.000 m3 tikslumu)
*******
Visu rastu Medienos svoris (0.000 kg tikslumu)
*******
Gaunamas popieriaus kiekis priklausomai muo gamybos metodo (% duota)
*******
Medienos svoris popieriaus gaminimui (0.000 kg tikslumu)
*******
Viso pagaminto popieriaus plotas (0.000 m2 tikslumu)
*******
Vieno gaminamo lapo plotas (0.000 m2 tikslumu)
*******
Pagaminta popieriaus lapu (vnt.)
*******
== APIBENDRINIMAS == 
Isviso pagaminta popieriaus lapu (vnt.) 
*******
Popieriaus gamybos kaina Eu (duota) 
*******
Vieno popieriaus lapo savikaina (0.00 Eu) 
*******
==== KNYGINIS KARTONAS ====
Gaminamo kartono pavadinimas pvz. REX/1 (duota) 
*******
Gaminamo kartono lapo plotis W (mm) 
*******
Gaminamo kartono lapo ilgis L (mm) 
*******
Gaminamo kartono metro kv. svoris  (g/m2) 
*******
1.   Kartonas gaminamas is medienos pvz. AZUOLAS (duota) 
*******
kartono gamybos metodas (nurodytas) 
*******
Rastu kiekis (duotas)
*******
Storgalio apimtis su zieve cm (0.0) (duota)
*******
Plongalio apimtis su zieve  cm (0.0) (duota)
*******
Rastu ilgis (duotas)
*******
== Skaiciavimai ==
Apskaiciuotas STORGALIO skersmuo su zieve (0.00 cm tikslumu)
*******
Storgalio zieves storis (is lenteles 0.0 mm tikslumu)
*******
Storgalio skersmuo (be zv.) su pataisa del rasto nelygumo (0.00 cm tikslumu)
*******
Apskaiciuotas PLONGALIO skersmuo su zieve (0.00 cm tikslumu)
*******
Plongalio zieves storis (is lenteles 0.0 mm tikslumu)
*******
Plongalio (be zv.) skersmuo su pataisa del rasto nelygumo (0.00 cm tikslumu)
*******
VIENO rasto turis (0.000 m3 tikslumu)
*******
VISU rastu turis (0.000 m3 tikslumu)
*******
Visos rastu Medienos svoris (0.000 kg tikslumu)
*******
Gaunamas kartono kiekis muo medienos svorio (% duota)
*******
Medienos svoris kartono gaminimui (0.000 kg tikslumu)
*******
Viso pagaminto kartono plotas (0.000 m2 tikslumu)
*******
Vieno gaminamo lapo plotas (0.000 m2 tikslumu)
*******
Pagaminta kartono lapu (vnt.)
*******
2.   Kartonas gaminamas is medienos pvz. AZUOLAS (duota) 
*******
kartono gamybos metodas (nurodytas) 
*******
Rastu kiekis (duotas)
*******
Storgalio apimtis su zieve cm (0.0) (duota)
*******
Plongalio apimtis su zieve  cm (0.0) (duota)
*******
Rastu ilgis (duotas)
*******
== Skaiciavimai ==
Apskaiciuotas STORGALIO skersmuo su zieve (0.00 cm tikslumu)
*******
Storgalio zieves storis (is lenteles 0.0 mm tikslumu)
*******
Storgalio skersmuo (be zv.) su pataisa del rasto nelygumo (0.00 cm tikslumu)
*******
Apskaiciuotas PLONGALIO skersmuo su zieve (0.00 cm tikslumu)
*******
Plongalio zieves storis (is lenteles 0.0 mm tikslumu)
*******
Plongalio (be zv.) skersmuo su pataisa del rasto nelygumo (0.00 cm tikslumu)
*******
VIENO rasto turis (0.000 m3 tikslumu)
*******
VISU rastu turis (0.000 m3 tikslumu)
*******
Visos rastu Medienos svoris (0.000 kg tikslumu)
*******
Gaunamas kartono kiekis muo medienos svorio (% duota)
*******
Medienos svoris kartono gaminimui (0.000 kg tikslumu)
*******
Viso pagaminto kartono plotas (0.000 m2 tikslumu)
*******
Vieno gaminamo lapo plotas (0.000 m2 tikslumu)
*******
Pagaminta kartono lapu (vnt.)
*******
== APIBENDRINIMAS == 
Isviso pagaminta kartono lapu (vnt.) 
*******
kartono gamybos kaina Eu (duota) 
*******
Vieno kartono lapo savikaina (0.00 Eu) 
*******
"""

print(tpl.format(**(dict(locals()))))
