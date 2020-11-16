#!/usr/bin/python3
from math import pi

def nupjauto_kugio_turis(h, d1, d2):
    r1, r2 = d1/2, d2/2
    return pi/3*h*(r1**2 + r1*r2 + r2**2)

t1_storgalio_apimtis_su_zieve=119.4 # cm
t1_plongalio_apimtis_su_zieve=46.2  # cm
t1_storgalio_skersmuo_su_zieve=t1_storgalio_apimtis_su_zieve/pi  # cm
t1_plongalio_skersmuo_su_zieve=t1_plongalio_apimtis_su_zieve/pi  # cm

t1_rastu_kiekis=5
t1_rastu_ilgis=5.38 # m
t1_storgalio_zieves_storis=10.6 # mm
t1_plongalio_zieves_storis=10.5 # mm
t1_storgalio_skersmuo_be_zieves=round(t1_storgalio_skersmuo_su_zieve-t1_storgalio_zieves_storis/10*2+.5) # cm
t1_plongalio_skersmuo_be_zieves=round(t1_plongalio_skersmuo_su_zieve-t1_plongalio_zieves_storis/10*2+.5) # cm

t1_vieno_rasto_turis=nupjauto_kugio_turis(t1_rastu_ilgis, t1_plongalio_skersmuo_be_zieves/100, t1_storgalio_skersmuo_be_zieves/100) # m3
t1_visu_rastu_turis=t1_vieno_rasto_turis*t1_rastu_kiekis # m3
t1_medienos_svoris=800 # kg/m3
t1_visu_rastu_svoris=t1_visu_rastu_turis*t1_medienos_svoris # kg
t1_gaunamas_popieriaus_kiekis_perc=6.82 # [0-100]%
t1_gaunamas_popieriaus_kiekis_trupm=t1_gaunamas_popieriaus_kiekis_perc/100 # [0-1]
t1_medienos_svoris_popieriaus_gaminimui=t1_visu_rastu_svoris*t1_gaunamas_popieriaus_kiekis_trupm # kg
t1_popieriaus_tankis=0.09 # kg/m2
t1_viso_pagaminto_popieriaus_plotas=t1_medienos_svoris_popieriaus_gaminimui/t1_popieriaus_tankis # m2
t1_vieno_lapo_plotas=.75*.9 # m2
t1_pagaminta_popieriaus_lapu=int(t1_viso_pagaminto_popieriaus_plotas/t1_vieno_lapo_plotas) # kiekis

tpl1="""Uzduoties Nr. 
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
{t1_storgalio_apimtis_su_zieve:.1f}
Plongalio apimtis cm (0.0) (duota)
{t1_plongalio_apimtis_su_zieve:.1f}
Rastu ilgis (duotas)
{t1_rastu_ilgis:.2f}
== Skaiciavimai ==
Apskaiciuotas STORGALIO skersmuo su zieve (0.00 cm tikslumu)
{t1_storgalio_skersmuo_su_zieve:.2f}
Storgalio zieves storis (is lenteles 0.0 mm tikslumu)
{t1_storgalio_zieves_storis:.1f}
Storgalio skersmuo (be zv.) su pataisa del rasto nelygumo (0.00 cm tikslumu)
{t1_storgalio_skersmuo_be_zieves:.2f}
Apskaiciuotas PLONGALIO skersmuo su zieve (0.00 cm tikslumu)
{t1_plongalio_skersmuo_su_zieve:.2f}
Plongalio zieves storis (is lenteles 0.0 mm tikslumu)
{t1_plongalio_zieves_storis:.1f}
Plongalio (be zv.) skersmuo su pataisa del rasto nelygumo (0.00 cm tikslumu)
{t1_plongalio_skersmuo_be_zieves:.2f}
VIENO rasto turis (0.000 m3 tikslumu)
{t1_vieno_rasto_turis:.3f}
VISU rastu turis (0.000 m3 tikslumu)
{t1_visu_rastu_turis:.3f}
Visu rastu Medienos svoris (0.000 kg tikslumu)
{t1_visu_rastu_svoris:.3f}
Gaunamas popieriaus kiekis priklausomai muo gamybos metodo (% duota)
{t1_gaunamas_popieriaus_kiekis_perc:.2f}
Medienos svoris popieriaus gaminimui (0.000 kg tikslumu)
{t1_medienos_svoris_popieriaus_gaminimui:.3f}
Viso pagaminto popieriaus plotas (0.000 m2 tikslumu)
{t1_viso_pagaminto_popieriaus_plotas:.3f}
Vieno gaminamo lapo plotas (0.000 m2 tikslumu)
{t1_vieno_lapo_plotas:.3f}
Pagaminta popieriaus lapu (vnt.)
{t1_pagaminta_popieriaus_lapu}"""
print(tpl1.format(**(dict(locals()))))
tpl2="""2.   Popierius gaminamas is medienos pvz. AZUOLAS (duota) 
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

print(tpl2.format(**(dict(locals()))))
