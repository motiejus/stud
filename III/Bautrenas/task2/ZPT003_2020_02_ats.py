#!/usr/bin/python3

storgalio_apimtis=119.4
plongalio_apimtis=46.2
rastu_ilgis=5.38
storgalio_zieves_storis=10.6
plongalio_zieves_storis=10.5
storgalio_skersmuo_su_zieve=int(storgalio_apimtis+storgalio_zieves_storis*2)
plongalio_skersmuo_su_zieve=int(plongalio_apimtis+plongalio_zieves_storis*2)


tpl="""
Uzduoties Nr. 
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
{storgalio_apimtis:.1f}
Plongalio apimtis cm (0.0) (duota)
{plongalio_apimtis:.1f}
Rastu ilgis (duotas)
{rastu_ilgis:.2f}
== Skaiciavimai ==
Apskaiciuotas STORGALIO skersmuo su zieve (0.00 cm tikslumu)
{storgalio_skersmuo_su_zieve:.2f}
Storgalio zieves storis (is lenteles 0.0 mm tikslumu)
{storgalio_zieves_storis:.1f}
Storgalio skersmuo (be zv.) su pataisa del rasto nelygumo (0.00 cm tikslumu)
*******
Apskaiciuotas PLONGALIO skersmuo su zieve (0.00 cm tikslumu)
{plongalio_skersmuo_su_zieve:.2f}
Plongalio zieves storis (is lenteles 0.0 mm tikslumu)
{plongalio_zieves_storis:.1f}
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
