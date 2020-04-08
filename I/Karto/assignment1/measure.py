#!/usr/bin/env python3

def dd(deg, mm, ss):
    return deg + mm/60.0 + ss/3600.0

print("""
Uzduoti parenge  A.Bautrenas  (Topografiniai zemelapiai) 
2019.09.18 09:32:26(34346.79s)  RND=2

Uzduotis Nr. KTZ004_2019_01
Jakstys_Motiejus (1915375)
 === Atkarpos ir Plotai == (NAV_SK=0.17 NAV_BR=0.25) ===
Atlikti iki: 2019.10.02   09:32:26

1. Pagal duotus duomenis apskaiciuoti (reikiamu tikslumu ir ivedant nurodytas pataisas) braizymui reikalingus parametrus
2. Nubraizyti du, tarpusavyje persidengiancius, uzdarus sklypus [1-2-3-4-5-6-1] ir [7-8-9-10-11-12-7]   (ziur. 01uzd_schema.pdf). 
3. Nubraizytus sklypus padalinti atkarpomis [T17-T20] ir [T19-T24] 
4. Surasyti visu virsuniu, susikirtimo tasku ir plotu numerius (ziur. 01uzd_schema.pdf)
5. Apskaiciuoti arba pamatuoti brezinyje nurodytus dydzius
6. Surasyti gautus rezultatus i atsakymu sablona. 
 
Ismatuoti (nustatyti) brezinyje:
1. Nubraizytu sklypu virsuniu ir susikirtimo tasku koordinates
2. Atstumus tarp tasku 1-6,3-4,8-9,11-12,9-12,7-11,14-16,13-15,T19-T24 ir T17-T20
3. Visu arealu (P1,P2, ... ,P12,P13) plotus ir perimetrus
4. Bendra plota ir perimetra pagal isorini kontura t.y. tarp tasku nr. [2,3,23,9,14,5,13,7,25,6,18,12,11,15] (ziur. 01uzd_schema.pdf).

Pataisos:
A= -5.240
B= -4.557
C= -7.002
N= -4.793
""")
A= -5.240
B= -4.557
C= -7.002
N= -4.793
print("""Koordinates (apskaiciuoti 0.000 tikslumu):
1
X = 5057.942 + B = %.3f""" % (5057.942 + B) + """
Y = 5901.809 + A = %.3f """ % (5901.809 + A) + """
7
X = 5167.517 + B = %.3f""" % (5167.517 + B) + """
Y = 5098.994 + C = %.3f""" % (5098.994 + C) + """
5
X = 4422.884 + B = %.3f""" %(4422.884 + B) + """
Y = 5228.007 + B = %.3f""" %(5228.007 + B) + """
10
X = 4652.032 + N = %.3f""" %(4652.032 + N) + """
Y = 6255.474 + N = %.3f""" %(6255.474 + N) + """
 
Atkarpos (apskaiciuoti 0.000 tikslumu):
D1-2 = 482.006 + C = %.3f""" %(482.006 + C) + """
D2-3 = 840.979 + C = %.3f""" %(840.979 + C) + """
D4-5 = 620.514 + C = %.3f""" %(620.514 + C) + """
D5-6 = 1245.332 + A = %.3f""" %(1245.332 + A) + """
D7-8 = 575.871 + B = %.3f""" %(575.871 + B) + """
D7-12 = 743.403 + B = %.3f""" %(743.403 + B) + """
D9-10 = 346.711 + A = %.3f""" %(346.711 + A) + """
D10-11 = 596.984 + A = %.3f""" %(596.984 + A) + """
 
Kampai(L-M-S) (apskaiciuoti 0.0001 tikslumu):
K1 = [74-31-39] + B (laipsniu) = %.4f""" % (dd(74,31,39)+B) + """
K2 = [86-33-05] + C (laipsniu) = %.4f""" % (dd(86,33,5)+C) + """
K5-1 = [34-35-03] + C (laipsniu) = %.4f""" % (dd(34,35,3)+C) + """
K5-2 = [178-57-49] + C (laipsniu) = %.4f""" % (dd(178,57,49)+C) + """
K7-1 = [52-01-12] + A (laipsniu) = %.4f""" % (dd(52,1,12)+A) + """
K7-2 = [31-56-19] + B (laipsniu) = %.4f""" % (dd(31,56,19)+B) + """
K10-1 = [107-04-53] + A (laipsniu) = %.4f""" % (dd(107,4,53)+A) + """
K10-2 = [119-50-37] + B (laipsniu) = %.4f""" % (dd(119,50,37)+B) + """
 
=== Atstumai iki brez.remelio (apskaiciuoti 0.000 tikslumu)===
Dr17 = 375.789 + C = %.3f""" % (375.789 + C) + """
Dr19 = 465.488 + C = %.3f""" % (465.488 + C) + """
Dr20 = 418.447 + C = %.3f""" % (418.447 + C) + """
Dr24 = 345.571 + B = %.3f""" % (345.571 + B) + """

Pastabos: 
1. Brezinio braizymo schema pateikta rinkmenoje [01uzd_schema.pdf], o braizoma AutoCAD koordinaciu sistemoje.
2. Visi atkarpu matmenys duoti metrais, o kampai laipsnineje sistemoje [L-M-S]=[Laipsniai-Minutes-Sekundes]. Pries ivedant pataisa i kampus, butina juos peskaiciuoti i desimtaine sistema ir tik tada ivesti nurodyta pataisa.
3. Taskai T17,T19,T20 ir T24 yra atitinkamu krastiniu vidurio taskai (Midpoint).
4. Plotus, tsk.koordinates ir linijinius dydzius apskaiciuoti bei ismatuoti 0.001 tikslumu, o kampus apskaiciuoti ir atideti brezinyje 0.0001 laipsnio tikslumu.
5. Visu skaiciavimu ir matavimu rezultatai turi buti surasyti atsakymu sablone nurodytu tikslumu.
6. Brezinio rinkmenos pavadinimas turi sutapti su uzduoties numeriu, t.y.  brezinys turi buti pavadintas KTZ004_2019_01_brez.dwg
7. Atliktu skaiciavimu ir matavimu rezultatus bei kitus duomenis surasyti i rinkmena [01sablonas_ats.txt].  Rinkmenos [01sablonas_ats.txt] strukturos nekeisti. Atsakymus surasyti  tik i jiems skirtas vietas, t.y. vietoje 'zvaigzduciu' (*****).  Visu skaitmenu (atsakymu) desintaine dalis turi buti atskirta TASKU, o ne kableliu, pvz. 12345.236 [TAIP], 12345,236 [NE].  Neteisinga uzrasymo forma bus vertinama kaip klaida! 
8. Rinkmenos pavadinima [01sablonas_ats.txt] pakeisti i savo uzduoties nr., pvz. [KTZ004_2019_01_ats.txt] ir atsiusti kartu su breziniu.
9. Visi taskai ir plotai turi buti sunumeruoti (ziur. [01uzd_schema.pdf]),  o brezini butina pasirasyti! 
10. Sioje uzduotyje lapo su metrika ('stampu') ir koordinaciu  tinklo braizyti nereikia 
11. Visi numeruoti taskai pazymimi uzspalvintais rutuliukai. Rutuliukai braizomi naudojant komanda [Donut] ir ivedant siuos dydzius: inside diameter... = 0, outside diameter... = 1.85 
12. Brezinio remelis braizomas nuo tasku T17, T19, T20, T24 atidedant apskaiciuotus atstumus Dr17, Dr19, Dr20 ir Dr24 (ziureti [01uzd_schema.pdf]).
13. Brezinys ir skaiciavimo rezultatai turi buti atsiusti iki nurodyto termino. Uz kiekviena paveluota valanda vertinimo balas mazinamas 0.05 balo.
14. Nubraizytu sklypu forma gali skirtis nuo formos pateiktos brezinio schemoje ziur. [01uzd_schema.pdf])! 
15. Jei kurio nors ploto nera, pvz., P8 arba P13, tai vietoje zvaigzduciu irasykite 0 (nuli)! 
16. Jei braizant brezinio remeli nurodytais atstumais (ziur. [01uzd_schema.pdf] 2 lapas), remelis kerta arealu ribas, tai apskaiciuota atstuma didiname po 10.000 metru, tol, kol  remas nebekirs sklypo konturo. Pvz. remelio krastine nuo T19 tasko turi buti atideta 275.488  atstumu. Jei sio atstumo mazai, tai ji padidiname iki 285.488, jei dar maza -  didiname iki 295.488 ir t.t.  

Pabaiga: 2019.09.18 09:32:26
""")
