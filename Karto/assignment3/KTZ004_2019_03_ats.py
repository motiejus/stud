#!/usr/bin/env python3

from measure import *

def xy(xy):
    return "X= %.3f\nY= %.3f" % xy

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
X= 16762.101
Y= 25481.372
Tasko Nr.3 koordinates
X= 16727.863
Y= 25413.773
Tasko Nr.4 koordinates
X= 16682.039
Y= 25363.469 
Tasko Nr.5 koordinates
X= 16805.910
Y= 25360.116
Tasko Nr.6 koordinates
X= 16799.166
Y= 25278.503
Tasko Nr.7 koordinates
X= 16643.190
Y= 25221.287
Tasko Nr.8 koordinates
X= 16581.158
Y= 25254.983
Tasko Nr.9 koordinates
X= 16596.293
Y= 25302.244
Tasko Nr.10 koordinates
X= 16572.048
Y= 25388.939
Tasko Nr.11 koordinates
X= 16542.699
Y= 25334.566
Tasko Nr.12 koordinates
X= 16472.045
Y= 25311.781
Tasko Nr.13 koordinates
X= 16472.045
Y= 25311.781
Tasko Nr.14 koordinates
X= 16481.977
Y= 25382.209
Tasko Nr.16 koordinates
X= 17145.648
Y= 25326.403
Tasko Nr.17 koordinates
X= 17183.476
Y= 25441.711 
Tasko Nr.18 koordinates
X= 17327.859
Y= 25325.250
Tasko Nr.19 koordinates
X= 17209.668
Y= 25338.982
Tasko Nr.20 koordinates
X= 17246.772
Y= 25255.196
Tasko Nr.21 koordinates
X= 17368.299
Y= 25197.454 
Tasko Nr.22 koordinates
X= 17411.383
Y= 25115.660 
Tasko Nr.23 koordinates
X= 17347.811
Y= 25022.089
Tasko Nr.24 koordinates
X= 17328.521
Y= 25101.862
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
%.1f""" % P1_virsutine + """
Iskasos Nr.1 plotas (P2) pagal slaito apacia (0.1 m2 tikslumu)
%.1f""" % P2_apatine + """
Iskasos Nr.1 turis (V1) paskaiciuotas pagal 2 formule (0.1 m3 tikslumu)
%.1f""" % fig1_v1 + """
Iskasos Nr.1 turis (V2) paskaiciuotas pagal 3 formule (0.1 m3 tikslumu)
%.1f""" % fig1_v2 + """
Galutinis iskasos Nr.1 turis (V) paskaiciuotas pagal 4 formule (1 m3 tikslumu)
%.f""" % fig1_v + """ 
Iskasos Nr.2 plotas (P3) pagal virsutine riba (0.1 m2 tikslumu)
%.1f""" % P3_virsutine + """
Iskasos Nr.2 plotas (P4) pagal slaito apacia (0.1 m2 tikslumu)
%.1f""" % P4_apatine + """
Iskasos Nr.2 turis (V1) paskaiciuotas pagal 2 formule (0.1 m3 tikslumu)
%.1f""" % fig2_v1 + """
Iskasos Nr.2 turis (V2) paskaiciuotas pagal 3 formule (0.1 m3 tikslumu)
%.1f""" % fig2_v2 + """
Galutinis iskasos Nr.2 turis (V) paskaiciuotas pagal 4 formule (1 m3 tikslumu)
%.0f""" % fig2_v + """ 
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
