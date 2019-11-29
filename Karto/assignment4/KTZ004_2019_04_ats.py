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
%.3f""" % L1 + """
Visas kelio A-03 plotis
%.3f""" % L1 + """
Koeficientas L1 plocio atidejimui (+/-0.001)
+1.0
=== Kelias A-05 ===
Plotis L2 (duotas)
%.3f""" % L2 + """
Plotis L3 (duotas)
%.3f""" % L3 + """
Visas kelio A-05 plotis
%.3f""" % A05_plotis + """
Koeficientas L2 plocio atidejimui (+/-0.001)
%+.3f""" % (-L2/(L2+L3)) + """
Koeficientas L3 plocio atidejimui (+/-0.001)
%+.3f""" % (L3/(L2+L3)) + """
=== Kelias A-08 ===
Plotis L4 (duotas)
%.3f""" % L3 + """
Plotis L5 (duotas)
%.3f""" % L5 + """
Plotis L6 (duotas)
%.3f""" % L6 + """
Plotis L7 (duotas)
%.3f""" % L7 + """
Plotis L8 (duotas)
%.3f""" % L8 + """
Plotis L9 (duotas)
%.3f""" % L9 + """
Visas kelio A-08 plotis
%.3f""" % A08_plotis + """
Koeficientas L4 plocio atidejimui (+/-0.001)
%+.3f""" % (-L4/(L4+L5+L6+L7+L8+L9)) + """
Koeficientas L5 plocio atidejimui (+/-0.001)
%+.3f""" % (-L5/(L4+L5+L6+L7+L8+L9)) + """
Koeficientas L6 plocio atidejimui (+/-0.001)
%+.3f""" % (-L6/(L4+L5+L6+L7+L8+L9)) + """
Koeficientas L7 plocio atidejimui (+/-0.001)
%+.3f""" % (L7/(L4+L5+L6+L7+L8+L9)) + """
Koeficientas L8 plocio atidejimui (+/-0.001)
%+.3f""" % (L8/(L4+L5+L6+L7+L8+L9)) + """
Koeficientas L9 plocio atidejimui (+/-0.001)
%+.3f""" % (L9/(L4+L5+L6+L7+L8+L9)) + """
=== Griovys G-11 ===
Plotis L10 (duotas)
%.3f""" % L10 + """
Plotis L11 (duotas)
%.3f""" % L11 + """
Plotis L12 (duotas)
%.3f""" % L12 + """
Plotis L13 (duotas)
%.3f""" % L13 + """
Visas griovio G-11 plotis
%.3f""" % G11_plotis + """
Koeficientas L10 plocio atidejimui (+/-0.001)
%+.3f""" % (-L10/(L10+L11+L12+L13)) + """
Koeficientas L11 plocio atidejimui (+/-0.001)
%+.3f""" % (-L11/(L10+L11+L12+L13)) + """
Koeficientas L12 plocio atidejimui (+/-0.001)
%+.3f""" % (L12/(L10+L11+L12+L13)) + """
Koeficientas L13 plocio atidejimui (+/-0.001)
%+.3f""" % (L13/(L10+L11+L12+L13)) + """
=== Apskaiciuoti keliu ir grioviu plociai BRAIZYMUI (0.001 tikslumu) ===
Kelio A-03 plotis
%.3f""" % A03_plotis + """
Kelio A-05 plotis
%.3f""" % A05_plotis + """
Kelio A-08 plotis
%.3f""" % A08_plotis + """
Griovio G-11 plotis
%.3f""" % G11_plotis + """
=== Apskaiciuota daugiakampio krastine D1 (0.001 tikslumu) ===
%.3f""" % D1 + """
=== Apskaiciuotas daugiakampio pasuk.kampas K1 (0.0001 laipsnio tikslumu) ===
%.4f""" % K1 + """
=== Apskaiciuotas atstumas iki uzliejimo zonos A1 (0.001 tikslumu) ===
%.3f""" % A1 + """
=============== Ismatuota brezinyje ================
=== Keliu ir grioviu asiu ilgiai (0.001 m tikslumu) ===
== Kelias A-03 ==
Asies 11-12-13-14-15-16-17-18 ilgis
%.3f""" % keliu_ilgiai['A-03'] + """
==Kelias A-05 ==
Asies 4-5-6-7-8-9-10 ilgis
%.3f""" % keliu_ilgiai['A-05'] + """
== Kelias A-08 ==
Asies 1-2-3 ilgis
%.3f""" % keliu_ilgiai['A-08'] + """
== Griovys G-11 ==
Asies 19-20-21-22-23-24 ilgis 
%.3f""" % keliu_ilgiai['G-11'] + """
Visas keliu/Grioviu tinklo ilgis (pagal asis) 
%.3f""" % sum(keliu_ilgiai.values()) + """
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
