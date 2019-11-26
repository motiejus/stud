#!/usr/bin/env python3

from measure import *

print("""Uzduotis Nr. 
KTZ004_2019_04
Braize (Pavarde_Vardas):
Motiejus_Jakstys
=== Apskaiciuotos posukio tasku koordinates (LKS94 koord.sist. 0.00 tikslumu)===""")
for v in vertices:
    print("Tasko Nr.%d koordinates" % v.point)
    print("X = %.3f" % v.coords.lksx)
    print("Y = %.3f" % v.coords.lksy)

print("""=== Apskaiciuoti liniju stiliu kurimo parametrai (0.001 tikslumu) ===
=== Kelias A-03 ===
Plotis L1 (duotas)
*******
Visas kelio A-03 plotis
*******
Koeficientas L1 plocio atidejimui (+/-0.001)
*******
=== Kelias A-05 ===
Plotis L2 (duotas)
*******
Plotis L3 (duotas)
*******
Visas kelio A-05 plotis
*******
Koeficientas L2 plocio atidejimui (+/-0.001)
*******
Koeficientas L3 plocio atidejimui (+/-0.001)
*******
=== Kelias A-08 ===
Plotis L4 (duotas)
*******
Plotis L5 (duotas)
*******
Plotis L6 (duotas)
*******
Plotis L7 (duotas)
*******
Plotis L8 (duotas)
*******
Plotis L9 (duotas)
*******
Visas kelio A-08 plotis
*******
Koeficientas L4 plocio atidejimui (+/-0.001)
*******
Koeficientas L5 plocio atidejimui (+/-0.001)
*******
Koeficientas L6 plocio atidejimui (+/-0.001)
*******
Koeficientas L7 plocio atidejimui (+/-0.001)
*******
Koeficientas L8 plocio atidejimui (+/-0.001)
*******
Koeficientas L9 plocio atidejimui (+/-0.001)
*******
=== Griovys G-11 ===
Plotis L10 (duotas)
*******
Plotis L11 (duotas)
*******
Plotis L12 (duotas)
*******
Plotis L13 (duotas)
*******
Visas griovio G-11 plotis
*******
Koeficientas L10 plocio atidejimui (+/-0.001)
*******
Koeficientas L11 plocio atidejimui (+/-0.001)
*******
Koeficientas L12 plocio atidejimui (+/-0.001)
*******
Koeficientas L13 plocio atidejimui (+/-0.001)
*******
=== Apskaiciuoti keliu ir grioviu plociai BRAIZYMUI (0.001 tikslumu) ===
Kelio A-03 plotis
*******
Kelio A-05 plotis
*******
Kelio A-08 plotis
*******
Griovio G-11 plotis
*******
=== Apskaiciuota daugiakampio krastine D1 (0.001 tikslumu) ===
*******
=== Apskaiciuotas daugiakampio pasuk.kampas K1 (0.0001 laipsnio tikslumu) ===
*******
=== Apskaiciuotas atstumas iki uzliejimo zonos A1 (0.001 tikslumu) ===
*******
=============== Ismatuota brezinyje ================
=== Keliu ir grioviu asiu ilgiai (0.001 m tikslumu) ===
== Kelias A-03 ==
Asies 11-12-13-14-15-16-17-18 ilgis
*******
==Kelias A-05 ==
Asies 4-5-6-7-8-9-10 ilgis
*******
== Kelias A-08 ==
Asies 1-2-3 ilgis
*******
== Griovys G-11 ==
Asies 19-20-21-22-23-24 ilgis 
*******
Visas keliu/Grioviu tinklo ilgis (pagal asis) 
*******
=== Uzlietu zemenaudmenu plotai (0.001 m2 tikslumu) ===
Miskas
*******
Ariama
*******
Sodas
*******
Pieva
*******
Ganykla
*******
Krumai
*******
Kelias A-03
*******
Kelias A-05
*******
Kelias A-08
*******
Griovys G-11
*******
Visas prognozuojamo uzliejimo plotas (0.001 m2 tikslumu)
*******
Visas uzlietas plotas (0.001 m2 tikslumu)
*******
Plotas kuris liko neuzlietas (0.001 m2 tikslumu)
*******""")
