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
t1_storgalio_zieves_storis=10.0 # mm
t1_plongalio_zieves_storis=7.5 # mm
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

t2_storgalio_apimtis_su_zieve=136.7 # cm
t2_plongalio_apimtis_su_zieve=58.7  # cm
t2_storgalio_skersmuo_su_zieve=t2_storgalio_apimtis_su_zieve/pi  # cm
t2_plongalio_skersmuo_su_zieve=t2_plongalio_apimtis_su_zieve/pi  # cm

t2_rastu_kiekis=3
t2_rastu_ilgis=4.5 # m
t2_storgalio_zieves_storis=21.6 # mm
t2_plongalio_zieves_storis=11.6 # mm
t2_storgalio_skersmuo_be_zieves=round(t2_storgalio_skersmuo_su_zieve-t2_storgalio_zieves_storis/10*2+.5) # cm
t2_plongalio_skersmuo_be_zieves=round(t2_plongalio_skersmuo_su_zieve-t2_plongalio_zieves_storis/10*2+.5) # cm

t2_vieno_rasto_turis=nupjauto_kugio_turis(t2_rastu_ilgis, t2_plongalio_skersmuo_be_zieves/100, t2_storgalio_skersmuo_be_zieves/100) # m3
t2_visu_rastu_turis=t2_vieno_rasto_turis*t2_rastu_kiekis # m3
t2_medienos_svoris=794 # kg/m3
t2_visu_rastu_svoris=t2_visu_rastu_turis*t2_medienos_svoris # kg
t2_gaunamas_popieriaus_kiekis_perc=9.74 # [0-100]%
t2_gaunamas_popieriaus_kiekis_trupm=t2_gaunamas_popieriaus_kiekis_perc/100 # [0-1]
t2_medienos_svoris_popieriaus_gaminimui=t2_visu_rastu_svoris*t2_gaunamas_popieriaus_kiekis_trupm # kg
t2_popieriaus_tankis=0.09 # kg/m2
t2_viso_pagaminto_popieriaus_plotas=t2_medienos_svoris_popieriaus_gaminimui/t2_popieriaus_tankis # m2
t2_vieno_lapo_plotas=.75*.9 # m2
t2_pagaminta_popieriaus_lapu=int(t2_viso_pagaminto_popieriaus_plotas/t2_vieno_lapo_plotas) # kiekis


tpl2="""2.   Popierius gaminamas is medienos pvz. AZUOLAS (duota)
Egle
Popieriaus gamybos metodas (nurodytas)
Mechaninis/Cheminis
Rastu kiekis (duotas)
3
Storgalio apimtis cm (0.0) (duota)
{t2_storgalio_apimtis_su_zieve:.1f}
Plongalio apimtis cm (0.0) (duota)
{t2_plongalio_apimtis_su_zieve:.1f}
Rastu ilgis (duotas)
{t2_rastu_ilgis:.2f}
== Skaiciavimai ==
Apskaiciuotas STORGALIO skersmuo su zieve (0.00 cm tikslumu)
{t2_storgalio_skersmuo_su_zieve:.2f}
Storgalio zieves storis (is lenteles 0.0 mm tikslumu)
{t2_storgalio_zieves_storis:.1f}
Storgalio skersmuo (be zv.) su pataisa del rasto nelygumo (0.00 cm tikslumu)
{t2_storgalio_skersmuo_be_zieves:.2f}
Apskaiciuotas PLONGALIO skersmuo su zieve (0.00 cm tikslumu)
{t2_plongalio_skersmuo_su_zieve:.2f}
Plongalio zieves storis (is lenteles 0.0 mm tikslumu)
{t2_plongalio_zieves_storis:.1f}
Plongalio (be zv.) skersmuo su pataisa del rasto nelygumo (0.00 cm tikslumu)
{t2_plongalio_skersmuo_be_zieves:.2f}
VIENO rasto turis (0.000 m3 tikslumu)
{t2_vieno_rasto_turis:.3f}
VISU rastu turis (0.000 m3 tikslumu)
{t2_visu_rastu_turis:.3f}
Visu rastu Medienos svoris (0.000 kg tikslumu)
{t2_visu_rastu_svoris:.3f}
Gaunamas popieriaus kiekis priklausomai muo gamybos metodo (% duota)
{t2_gaunamas_popieriaus_kiekis_perc:.2f}
Medienos svoris popieriaus gaminimui (0.000 kg tikslumu)
{t2_medienos_svoris_popieriaus_gaminimui:.3f}
Viso pagaminto popieriaus plotas (0.000 m2 tikslumu)
{t2_viso_pagaminto_popieriaus_plotas:.3f}
Vieno gaminamo lapo plotas (0.000 m2 tikslumu)
{t2_vieno_lapo_plotas:.3f}
Pagaminta popieriaus lapu (vnt.)
{t2_pagaminta_popieriaus_lapu}"""
print(tpl2.format(**(dict(locals()))))

t12_isviso_pagaminta_lapu=int(t1_pagaminta_popieriaus_lapu+t2_pagaminta_popieriaus_lapu) # vnt
t12_popieriaus_gamybos_kaina=969.42 # eur
t12_vieno_popieriaus_lapo_savikaina=t12_popieriaus_gamybos_kaina/t12_isviso_pagaminta_lapu # eur

tpl12="""== APIBENDRINIMAS ==
Isviso pagaminta popieriaus lapu (vnt.)
{t12_isviso_pagaminta_lapu}
Popieriaus gamybos kaina Eu (duota)
{t12_popieriaus_gamybos_kaina:.2f}
Vieno popieriaus lapo savikaina (0.00 Eu)
{t12_vieno_popieriaus_lapo_savikaina:.2f}"""
print(tpl12.format(**(dict(locals()))))


t3_gaminamo_kartono_plotis=500 # mm
t3_gaminamo_kartono_ilgis=700 # mm
t3_gaminamo_kartono_metro_svoris=330 # g/m2
t3_rastu_kiekis=6
t3_storgalio_apimtis_su_zieve=121.0 # cm
t3_plongalio_apimtis_su_zieve=13.2 # cm
t3_rastu_ilgis=3.46

t3_storgalio_skersmuo_su_zieve=t3_storgalio_apimtis_su_zieve/pi  # cm
t3_plongalio_skersmuo_su_zieve=t3_plongalio_apimtis_su_zieve/pi  # cm
t3_storgalio_zieves_storis=25.8
t3_storgalio_skersmuo_be_zieves=round(t3_storgalio_skersmuo_su_zieve-t3_storgalio_zieves_storis/10*2+.5) # cm
t3_plongalio_zieves_storis=5.0
t3_plongalio_skersmuo_be_zieves=round(t3_plongalio_skersmuo_su_zieve-t3_plongalio_zieves_storis/10*2+.5) # cm

t3_vieno_rasto_turis=nupjauto_kugio_turis(t3_rastu_ilgis, t3_plongalio_skersmuo_be_zieves/100, t3_storgalio_skersmuo_be_zieves/100) # m3
t3_visu_rastu_turis=t3_vieno_rasto_turis*t3_rastu_kiekis # m3

t3_medienos_svoris=762
t3_visu_rastu_svoris=t3_visu_rastu_turis*t3_medienos_svoris # kg
t3_gaunamas_popieriaus_kiekis_perc=28.11 # [0-100]%
t3_gaunamas_popieriaus_kiekis_trupm=t3_gaunamas_popieriaus_kiekis_perc/100 # [0-1]
t3_medienos_svoris_popieriaus_gaminimui=t3_visu_rastu_svoris*t3_gaunamas_popieriaus_kiekis_trupm # kg
t3_popieriaus_tankis=0.09 # kg/m2
t3_viso_pagaminto_popieriaus_plotas=t3_medienos_svoris_popieriaus_gaminimui/t3_popieriaus_tankis # m2
t3_vieno_lapo_plotas=.75*.9 # m2
t3_pagaminta_popieriaus_lapu=int(t3_viso_pagaminto_popieriaus_plotas/t3_vieno_lapo_plotas) # kiekis

tpl3="""==== KNYGINIS KARTONAS ====
Gaminamo kartono pavadinimas pvz. REX/1 (duota)
SRA2/2
Gaminamo kartono lapo plotis W (mm)
{t3_gaminamo_kartono_plotis}
Gaminamo kartono lapo ilgis L (mm)
{t3_gaminamo_kartono_ilgis}
Gaminamo kartono metro kv. svoris  (g/m2)
{t3_gaminamo_kartono_metro_svoris}
1.   Kartonas gaminamas is medienos pvz. AZUOLAS (duota)
Drebule
kartono gamybos metodas (nurodytas)
Mechaninis
Rastu kiekis (duotas)
{t3_rastu_kiekis}
Storgalio apimtis su zieve cm (0.0) (duota)
{t3_storgalio_apimtis_su_zieve:.1f}
Plongalio apimtis su zieve  cm (0.0) (duota)
{t3_plongalio_apimtis_su_zieve:.1f}
Rastu ilgis (duotas)
{t3_rastu_ilgis:.2f}
== Skaiciavimai ==
Apskaiciuotas STORGALIO skersmuo su zieve (0.00 cm tikslumu)
{t3_storgalio_skersmuo_su_zieve:.2f}
Storgalio zieves storis (is lenteles 0.0 mm tikslumu)
{t3_storgalio_zieves_storis:.1f}
Storgalio skersmuo (be zv.) su pataisa del rasto nelygumo (0.00 cm tikslumu)
{t3_storgalio_skersmuo_be_zieves:.2f}
Apskaiciuotas PLONGALIO skersmuo su zieve (0.00 cm tikslumu)
{t3_plongalio_skersmuo_su_zieve:.2f}
Plongalio zieves storis (is lenteles 0.0 mm tikslumu)
{t3_plongalio_zieves_storis:.1f}
Plongalio (be zv.) skersmuo su pataisa del rasto nelygumo (0.00 cm tikslumu)
{t3_plongalio_skersmuo_be_zieves:.2f}
VIENO rasto turis (0.000 m3 tikslumu)
{t3_vieno_rasto_turis:.3f}
VISU rastu turis (0.000 m3 tikslumu)
{t3_visu_rastu_turis:.3f}
Visos rastu Medienos svoris (0.000 kg tikslumu)
{t3_visu_rastu_svoris:.3f}
Gaunamas kartono kiekis muo medienos svorio (% duota)
{t3_gaunamas_popieriaus_kiekis_perc:.2f}
Medienos svoris kartono gaminimui (0.000 kg tikslumu)
{t3_medienos_svoris_popieriaus_gaminimui:.3f}
Viso pagaminto kartono plotas (0.000 m2 tikslumu)
{t3_viso_pagaminto_popieriaus_plotas:.3f}
Vieno gaminamo lapo plotas (0.000 m2 tikslumu)
{t3_vieno_lapo_plotas:.3f}
Pagaminta kartono lapu (vnt.)
{t3_pagaminta_popieriaus_lapu}"""
print(tpl3.format(**(dict(locals()))))

t4_gaminamo_kartono_plotis=500 # mm
t4_gaminamo_kartono_ilgis=700 # mm
t4_gaminamo_kartono_metro_svoris=330 # g/m2
t4_rastu_kiekis=9
t4_storgalio_apimtis_su_zieve=148.6 # cm
t4_plongalio_apimtis_su_zieve=30.2 # cm
t4_rastu_ilgis=5.2

t4_storgalio_skersmuo_su_zieve=t4_storgalio_apimtis_su_zieve/pi  # cm
t4_plongalio_skersmuo_su_zieve=t4_plongalio_apimtis_su_zieve/pi  # cm
t4_storgalio_zieves_storis=48.4 # mm
t4_storgalio_skersmuo_be_zieves=round(t4_storgalio_skersmuo_su_zieve-t4_storgalio_zieves_storis/10*2+.5) # cm
t4_plongalio_zieves_storis=7.0 # mm
t4_plongalio_skersmuo_be_zieves=round(t4_plongalio_skersmuo_su_zieve-t4_plongalio_zieves_storis/10*2+.5) # cm

t4_vieno_rasto_turis=nupjauto_kugio_turis(t4_rastu_ilgis, t4_plongalio_skersmuo_be_zieves/100, t4_storgalio_skersmuo_be_zieves/100) # m3
t4_visu_rastu_turis=t4_vieno_rasto_turis*t4_rastu_kiekis # m3

t4_medienos_svoris=878
t4_visu_rastu_svoris=t4_visu_rastu_turis*t4_medienos_svoris # kg
t4_gaunamas_popieriaus_kiekis_perc=11.79 # [0-100]%
t4_gaunamas_popieriaus_kiekis_trupm=t4_gaunamas_popieriaus_kiekis_perc/100 # [0-1]
t4_medienos_svoris_popieriaus_gaminimui=t4_visu_rastu_svoris*t4_gaunamas_popieriaus_kiekis_trupm # kg
t4_popieriaus_tankis=0.09 # kg/m2
t4_viso_pagaminto_popieriaus_plotas=t4_medienos_svoris_popieriaus_gaminimui/t4_popieriaus_tankis # m2
t4_vieno_lapo_plotas=.75*.9 # m2
t4_pagaminta_popieriaus_lapu=int(t4_viso_pagaminto_popieriaus_plotas/t4_vieno_lapo_plotas) # kiekis


tpl4="""2.   Kartonas gaminamas is medienos pvz. AZUOLAS (duota)
Berzas
kartono gamybos metodas (nurodytas)
Cheminis/Sulfatinis
Rastu kiekis (duotas)
{t4_rastu_kiekis}
Storgalio apimtis su zieve cm (0.0) (duota)
{t4_storgalio_apimtis_su_zieve:.1f}
Plongalio apimtis su zieve  cm (0.0) (duota)
{t4_plongalio_apimtis_su_zieve:.1f}
Rastu ilgis (duotas)
{t4_rastu_ilgis:.2f}
== Skaiciavimai ==
Apskaiciuotas STORGALIO skersmuo su zieve (0.00 cm tikslumu)
{t4_storgalio_skersmuo_su_zieve:.2f}
Storgalio zieves storis (is lenteles 0.0 mm tikslumu)
{t4_storgalio_zieves_storis:.1f}
Storgalio skersmuo (be zv.) su pataisa del rasto nelygumo (0.00 cm tikslumu)
{t4_storgalio_skersmuo_be_zieves:.2f}
Apskaiciuotas PLONGALIO skersmuo su zieve (0.00 cm tikslumu)
{t4_plongalio_skersmuo_su_zieve:.2f}
Plongalio zieves storis (is lenteles 0.0 mm tikslumu)
{t4_plongalio_zieves_storis:.1f}
Plongalio (be zv.) skersmuo su pataisa del rasto nelygumo (0.00 cm tikslumu)
{t4_plongalio_skersmuo_be_zieves:.2f}
VIENO rasto turis (0.000 m3 tikslumu)
{t4_vieno_rasto_turis:.3f}
VISU rastu turis (0.000 m3 tikslumu)
{t4_visu_rastu_turis:.3f}
Visos rastu Medienos svoris (0.000 kg tikslumu)
{t4_visu_rastu_svoris:.3f}
Gaunamas kartono kiekis muo medienos svorio (% duota)
{t4_gaunamas_popieriaus_kiekis_perc:.2f}
Medienos svoris kartono gaminimui (0.000 kg tikslumu)
{t4_medienos_svoris_popieriaus_gaminimui:.3f}
Viso pagaminto kartono plotas (0.000 m2 tikslumu)
{t4_viso_pagaminto_popieriaus_plotas:.3f}
Vieno gaminamo lapo plotas (0.000 m2 tikslumu)
{t4_vieno_lapo_plotas:.3f}
Pagaminta kartono lapu (vnt.)
{t4_pagaminta_popieriaus_lapu}"""
print(tpl4.format(**(dict(locals()))))

t34_isviso_pagaminta_lapu=int(t3_pagaminta_popieriaus_lapu+t4_pagaminta_popieriaus_lapu) # vnt
t34_popieriaus_gamybos_kaina=969.42 # eur
t34_vieno_popieriaus_lapo_savikaina=t34_popieriaus_gamybos_kaina/t34_isviso_pagaminta_lapu # eur

tpl34="""== APIBENDRINIMAS ==
Isviso pagaminta kartono lapu (vnt.)
{t34_isviso_pagaminta_lapu}
kartono gamybos kaina Eu (duota)
{t34_popieriaus_gamybos_kaina:.2f}
Vieno kartono lapo savikaina (0.00 Eu)
{t34_vieno_popieriaus_lapo_savikaina:.2f}"""
print(tpl34.format(**(dict(locals()))))
