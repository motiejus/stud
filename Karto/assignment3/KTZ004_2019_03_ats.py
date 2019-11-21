#!/usr/bin/env python3

from measure import *

def xy(xy):
    return "X= %.3f\nY= %.3f" % xy

def off1(x, y):
    return x - (XT3 - XT1), y - (YT3 - YT1)

def off2(x, y):
    return x - (XT3 - XT2), y - (YT3 - YT2)

print("""Uzduotis Nr.
KTZ004_2019_03
Braize (Pavarde_Vardas):
Motiejus_Jakstys
=== Pradiniu tasku koordinates (0.000 tikslumu)(duotos)===
X1 = %s""" % X1 + """
Y1 = %s""" % Y1 + """
X15 = %s""" % X15 + """
Y15 = %s""" % Y15 + """
XT3 = %s""" % XT3 + """
YT3 = %s""" % YT3 + """
=== Apskaiciuoti atkarpu ilgiai (0.000 tikslumu) ===
1L-1 = %s""" % L1L1 + """
1L-2 = %s""" % L1L2 + """
1L-3 = %s""" % L1L3 + """
1L-4 = %s""" % L1L4 + """
1L-5 = %s""" % L1L5 + """
1L-6 = %s""" % L1L6 + """
1L-7 = %s""" % L1L7 + """
1L-8 = %s""" % L1L8 + """
1L-9 = %s""" % L1L9 + """
1L-10 = %s""" % L1L10 + """
1L-11 = %s""" % L1L11 + """
1L-12 = %s""" % L1L12 + """
1L-13 = %s""" % L1L13 + """
2L-1 = %s""" % L2L1 + """
2L-2 = %s""" % L2L2 + """
2L-3 = %s""" % L2L3 + """
2L-4 = %s""" % L2L4 + """
2L-5 = %s""" % L2L5 + """
2L-6 = %s""" % L2L6 + """
2L-7 = %s""" % L2L7 + """
2L-8 = %s""" % L2L8 + """
2L-9 = %s""" % L2L9 + """
=== Apskaiciuoti kampai (0-00-00.1 ir 0.0000001 tikslumu) ===
Kampas Nr.1K-1
1K-1(L) = %.7f""" % K1K1 + """
1K-1(L-M-S) = %s""" % Deg.from_1(K1K1) + """
Kampas Nr.1K-2
1K-2(L) = %.7f""" % K1K2 + """
1K-2(L-M-S) = %s""" % Deg.from_1(K1K2) + """
Kampas Nr.1K-3
1K-3(L) = %.7f""" % K1K3 + """
1K-3(L-M-S) = %s""" % Deg.from_1(K1K3) + """
Kampas Nr.1K-4
1K-4(L) = %.7f""" % K1K4 + """
1K-4(L-M-S) = %s""" % Deg.from_1(K1K4) + """
Kampas Nr.1K-5
1K-5(L) = %.7f""" % K1K5 + """
1K-5(L-M-S) = %s""" % Deg.from_1(K1K5) + """
Kampas Nr.1K-6
1K-6(L) = %.7f""" % K1K6 + """
1K-6(L-M-S) = %s""" % Deg.from_1(K1K6) + """
Kampas Nr.1K-7
1K-7(L) = %.7f""" % K1K7 + """
1K-7(L-M-S) = %s""" % Deg.from_1(K1K7) + """
Kampas Nr.1K-8
1K-8(L) = %.7f""" % K1K8 + """
1K-8(L-M-S) = %s""" % Deg.from_1(K1K8) + """
Kampas Nr.1K-9
1K-9(L) = %.7f""" % K1K9 + """
1K-9(L-M-S) = %s""" % Deg.from_1(K1K9) + """
Kampas Nr.1K-10
1K-10(L) = %.7f""" % K1K10 + """
1K-10(L-M-S) = %s""" % Deg.from_1(K1K10) + """
Kampas Nr.1K-11
1K-11(L) = %.7f""" % K1K11 + """
1K-11(L-M-S) = %s""" % Deg.from_1(K1K11) + """
Kampas Nr.1K-12
1K-12(L) = %.7f""" % K1K12 + """
1K-12(L-M-S) = %s""" % Deg.from_1(K1K12) + """
Kampas Nr.1K-13
1K-13(L) = %.7f""" % K1K13 + """
1K-13(L-M-S) = %s""" % Deg.from_1(K1K13) + """
Kampas Nr.2K-1
2K-1(L) = %.7f""" % K2K1 + """
2K-1(L-M-S) = %s""" % Deg.from_1(K2K1) + """
Kampas Nr.2K-2
2K-2(L) = %.7f""" % K2K2 + """
2K-2(L-M-S) = %s""" % Deg.from_1(K2K2) + """
Kampas Nr.2K-3
2K-3(L) = %.7f""" % K2K3 + """
2K-3(L-M-S) = %s""" % Deg.from_1(K2K3) + """
Kampas Nr.2K-4
2K-4(L) = %.7f""" % K2K4 + """
2K-4(L-M-S) = %s""" % Deg.from_1(K2K4) + """
Kampas Nr.2K-5
2K-5(L) = %.7f""" % K2K5 + """
2K-5(L-M-S) = %s""" % Deg.from_1(K2K5) + """
Kampas Nr.2K-6
2K-6(L) = %.7f""" % K2K6 + """
2K-6(L-M-S) = %s""" % Deg.from_1(K2K6) + """
Kampas Nr.2K-7
2K-7(L) = %.7f""" % K2K7+ """
2K-7(L-M-S) = %s""" % Deg.from_1(K2K7) + """
Kampas Nr.2K-8
2K-8(L) = %.7f""" % K2K8 + """
2K-8(L-M-S) = %s""" % Deg.from_1(K2K8) + """
Kampas Nr.2K-9
2K-9(L) = %.7f""" % K2K9 + """
2K-9(L-M-S) = %s""" % Deg.from_1(K2K9) + """
=== Iskasos Nr.1 gylis H1 (0.00 tikslumu) (duotas)===
%.2f""" % H1 + """
=== Iskasos Nr.1 slaito polinkio kampas SK1 (0.01 tikslumu) (duotas)===
%.2f""" % SK1 + """
=== Apskaiciuotas atstumas iki slaito papedes A1 (0.00 tikslumu)===
%.2f""" % A1 + """
=== Iskasos Nr.2 gylis H2 (0.00 tikslumu) (duotas)===
%.2f""" % H2 + """
=== Iskasos Nr.2 slaito polinkio kampas SK2 (0.01 tikslumu) (duotas)===
%.2f""" % SK2 + """
=== Apskaiciuotas atstumas iki slaito papedes A2 (0.00 tikslumu)===
%.2f""" % A2 + """
=============== Ismatuota brezinyje ================
=== Tasku koordinates (0.001 tikslumu) ===
Tasko Nr.2 koordinates
""" + xy(off1(Dec('17074.0250'), Dec('26806.2717'))) + """
Tasko Nr.3 koordinates
""" + xy(off1(Dec('17006.4258'), Dec('26772.0343'))) + """
Tasko Nr.4 koordinates
""" + xy(off1(Dec('16956.1218 '), Dec('26726.2096'))) + """
Tasko Nr.5 koordinates
""" + xy(off1(Dec('16956.1218'), Dec('26726.2096'))) + """
Tasko Nr.6 koordinates
""" + xy(off1(Dec('16871.1565'), Dec('26843.3373'))) + """
Tasko Nr.7 koordinates
""" + xy(off1(Dec('16813.9395'), Dec('26687.3606'))) + """
Tasko Nr.8 koordinates
""" + xy(off1(Dec('16847.6364'), Dec('26625.3292'))) + """
Tasko Nr.9 koordinates
""" + xy(off1(Dec('16894.8971'), Dec('26640.4640'))) + """
Tasko Nr.10 koordinates
""" + xy(off1(Dec('16981.5918'), Dec('26616.2192'))) + """
Tasko Nr.11 koordinates
""" + xy(off1(Dec('16927.2194'), Dec('26586.8697'))) + """
Tasko Nr.12 koordinates
""" + xy(off1(Dec('26516.2159'), Dec('16904.4338'))) + """
Tasko Nr.13 koordinates
""" + xy(off1(Dec('16992.5045'), Dec('26428.8250'))) + """
Tasko Nr.14 koordinates
""" + xy(off1(Dec('16974.8617'), Dec('26526.1478'))) + """
Tasko Nr.16 koordinates
X= 17396.566
Y= 25075.488
Tasko Nr.17 koordinates
X= 17511.871
Y= 25113.316
Tasko Nr.18 koordinates
X= 17395.410
Y= 25257.699
Tasko Nr.19 koordinates
X= 17409.142
Y= 25139.508
Tasko Nr.20 koordinates
X= 17325.356
Y= 25176.612
Tasko Nr.21 koordinates
X= 17267.614 
Y= 25298.138
Tasko Nr.22 koordinates
X= 17185.820
Y= 25341.223
Tasko Nr.23 koordinates
X= 17092.249
Y= 25277.651
Tasko Nr.24 koordinates
X= 17172.022
Y= 25258.361
Tasko Nr. T1 koordinates
X= %.3f""" % XT1 + """
Y= %.3f""" % YT1 + """
Tasko Nr. T2 koordinates
X= %.3f""" % XT2 + """
Y= %.3f""" % YT2 + """
=== Atstumas tarp tasku 1-7 (0.001 tikslumu) ===
279.701
=== Atstumas tarp tasku 4-10 (0.001 tikslumu) ===
112.901
=== Atstumas tarp tasku 13-1 (0.001 tikslumu) ===
273.975
=== Atstumas tarp tasku 15-19 (0.001 tikslumu) ===
218.302
=== Atstumas tarp tasku 16-24 (0.001 tikslumu) ===
289.588
=== Atstumas tarp tasku 24-15 (0.001 tikslumu) ===
138.322
=== Atstumas tarp tasku T1-T2 (0.001 tikslumu) ===
928.606
=== Atstumas tarp tasku T1-T3 (0.001 tikslumu) ===
1266.775
=== Atstumas tarp tasku T2-T3 (0.001 tikslumu) ===
1543.369
=== Teritoriju plotai (m2) (0.001 tikslumu) ===
Iskasos Nr.1 plotas m2 (2011m)
63425.860
Iskasos Nr.2 plotas m2 (2019m)
1408.927
1 aro rekultivacijos(R) kaina eurais (nurodyta uzduotyje)
871.29
Visas rekultivuojamas plotas
97895.626
22 m2 nauju plotu(N) isisavinimo kaina eurais (nurodyta uzduotyje)
545.84
Visas naujai isisavintas plotas
34469.766
8 m2 toliau ekspluatuojamo(E) ploto kaina eurais (nurodyta uzduotyje)
16.48 
Visas toliau ekspluatuojamas plotas
22960.319
=== Iskasto grunto kiekio skaiciavimas ===
Iskasos Nr.1 plotas (P1) pagal virsutine riba (0.1 m2 tikslumu)
*******
Iskasos Nr.1 plotas (P2) pagal slaito apacia (0.1 m2 tikslumu)
*******
Iskasos Nr.1 turis (V1) paskaiciuotas pagal 2 formule (0.1 m3 tikslumu)
*******
Iskasos Nr.1 turis (V2) paskaiciuotas pagal 3 formule (0.1 m3 tikslumu)
*******
Galutinis iskasos Nr.1 turis (V) paskaiciuotas pagal 4 formule (1 m3 tikslumu)
*******
Iskasos Nr.2 plotas (P3) pagal virsutine riba (0.1 m2 tikslumu)
*******
Iskasos Nr.2 plotas (P4) pagal slaito apacia (0.1 m2 tikslumu)
*******
Iskasos Nr.2 turis (V1) paskaiciuotas pagal 2 formule (0.1 m3 tikslumu)
*******
Iskasos Nr.2 turis (V2) paskaiciuotas pagal 3 formule (0.1 m3 tikslumu)
*******
Galutinis iskasos Nr.2 turis (V) paskaiciuotas pagal 4 formule (1 m3 tikslumu)
*******
=== Apskaiciuotos kainos (0.01Eu tikslumu) ===
Visa rekultivacijos (R) kaina
%.2f""" % (rek_kaina * rek_plotas) + """
Nauju plotu (N) isisavinimo kaina
%.2f""" % (nauj_kaina * nauj_plotas) + """
Eksluatacijos (E) kaina
%.2f""" % (ekspl_kaina * ekspl_plotas) + """
Visa kaina (R+N+E)
%.2f""" % visa_kaina + """
""")
