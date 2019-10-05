#!/usr/bin/env python3

def deg(deg, mm, ss):
    return deg + mm/60.0 + ss/3600.0

A= +5.928
B= +2.420
C= +4.716
P1= +0.594
P2= +0.942
P3= -0.475
 
print("""
Uzduotis:   
Pagal duotus duomenis apskaiciuoti (ivedant nurodytas pataisas) braizymui reikalingus parametrus ir nubraizyti (ziur.[02uzd_schema.pdf]):  
1. Savartyno [1-5-2-6-3-4-1] ribas 
2. Suformuoti (naudojant konstrukcines linijas) apsaugine zona. 
3. Nubraizyti apsaugines zonos ribas [7-8-9-10-11-12-7]. 
4. Nustatyti pusiaukampiniu susikirtimo taska Nr.13 
5. Nubraizyti keliu asis nurodytomis kryptimis ir atideti reikiamus kaliu plocius 
6. Koordinaciu tinkla nubraizyti masteliu M 1:500 naudojant 'Konstrukcines linijas'.  Koordinaciu tinklo pradzia apskaiciuoti pagal 8 tasko koordinates. 
 
=== Pradiniu tasku koordinates (LKS94 sistemoje) ===
1
X = 6171050.082 + B = %.3f""" % (6171050.082 + B ) + """
Y = 586491.217 + B = %.3f""" % (586491.217 + B ) + """
2
X = 6171121.58 + C = %.3f""" % (6171121.58 + C ) + """
Y = 586544.037 + B = %.3f""" % (586544.037 + B ) + """
3
X = 6171135.686 + B = %.3f""" % (6171135.686 + B ) + """
Y = 586464.874 + A = %.3f""" % (586464.874 + A ) + """
 
=== Apsaugos zonos plociai ===
A1 = 15.235 + C = %.3f""" % (15.235 + C ) + """
A2 = 20.077 + B = %.3f""" % (20.077 + B ) + """
A3 = 34.104 + B = %.3f""" % (34.104 + B ) + """
A4 = 22.871 + B = %.3f""" % (22.871 + B ) + """
A5 = 31.543 + A = %.3f""" % (31.543 + A ) + """
A6 = 29.664 + B = %.3f""" % (29.664 + B ) + """
 
=== Pusiaukampines === 
 Pusiaukampines brezti is kampu Nr.8 ir Nr.10 virsuniu.
 
=== Keliu asiu kryptys ===
1 kelio asis [13-8]
2 kelio asis [13-10]
3 kelio asis [13-12]
 
=== Keliu plociai nuo kelio asies:
A7 (1 kelias) = 5.908 + P2 = %.3f""" % (5.908 + P2 ) + """
A8 (2 kelias) = 7.958 + P2 = %.3f""" % (7.958 + P2 ) + """
A9 (3 kelias) = 3.766 + P3 = %.3f""" % (3.766 + P3 ) + """
 
=== Kampai (L-M-S) ===
K1-1 = [34-45-27.4] + A (laipsniu) = %.4f""" % (deg(34,45,27.4) + A) + """
K1-2 = [117-52-27.8] + B (laipsniu) = %.4f""" % (deg(117,52,27.8) + B) + """
K2-1 = [32-31-42.0] + C (laipsniu) = %.4f""" % (deg(32,31,42.0) + C) + """
K2-2 = [137-32-18.6] + B (laipsniu) = %.4f""" % (deg(137,32,18.6) + B) + """
K3-1 = [156-10-9.0] + C (laipsniu) = %.4f""" % (deg(156,10,9.0) + C) + """
K3-2 = [123-0-16.1] + B (laipsniu) = %.4f""" % (deg(123,0,16.1) + B) + """

=== Ismatuoti (nustatyti) brezinyje ===
1. Tasku Nr. 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 koordinates
2. Atkarpu 1-5, 5-2, 2-6, 6-3, 3-4 ir 4-1 ilgius
3. Sklypo (savartyno)[1-5-2-6-3-4-1] plota (be keliais uzimamo ploto).
4. Apsaugos zonos plota (be keliais uzimamo ploto) ir visa isorini perimetra.
5. Keliais uzimama plota savartyno ribose
6. Keliais uzimama plota apsaugos zonos ribose
7. Ribos (8-7-12) su Valstybiniu misku ilgi (be keliu plociu)
8. Ribos (8-9-10-11-12) su gamyklos teritorija ilgi (be keliu plociu)
 
=== Apskaiciuoti ===
1. Paskaiciuoti, kiek reikes sumoketi mokesciu i valstybes biudzeta uz visos teritorijos eksploatacijos laika, jei:
1.1 Visas eksploatacijos laikas (menesiais) = 168.23
1.2 Savartyno(be keliais uzimamo ploto) vieno aro prieziuros mokestis (Eur. per men.) = 53.08
1.3 Apsaugos zonos (be keliais uzimamo ploto) vieno hektaro prieziuros mokestis (Eur. per men.) = 1073.97
1.4 Keliu (savartyne ir apsaugos zonoje) prieziuros vieno kv.metro  mokestis (Eur. per men.) = 0.35
2. Paskaiciuoti, kiek reikes medziagu apsaugines zonos aptverimui, jei:
2.1 Riba su valstybiniu misku (be keliu plociu) aptverta spygliuota viela:
 spygl.viel.eiliu skaicius = 5
 spygl.viel. 1m kaina (Eur.) = 6.06
2.2 Riba su gamyklos teritorija (be keliu plociu) aptverta vielos tinklu:
 viel.tinkl. tvoros aukstis (m) = 4.70
 viel.tinkl. 1m2 kaina = 10.53

Pastabos: 
1. Brezinio schema pateikta rinkmenoje [02uzd_schema.pdf] 
2. Visi matmenys duoti metrais, o koordinaciu sistema - LKS94  (braizant butina sukeisti koordinaciu asis, o irasant atsakymus - jas vel atkeisti). 
Pvz1. Zinomo tsk. koord. (duotos) X=6151234 Y=311245, braizant ivedame   311245,6151234 
Pvz2. Nuskaityto is brezinio tsk. koordinates X=504256 Y=6084578,  rasome i atsakymu sablona  X=6084578 Y=504256
3. Plotus, tsk.koordinates ir linijinius dydzius apskaiciuoti bei ismatuoti 0.001 tikslumu, o kampus apskaiciuoti ir atideti brezinyje 0.0001 laipsnio tikslumu.
4. Reikalavimai uzduoties atlikimui (rinkmenu pavadinimams, atsakymu sablono pildymui, atlikimo terminui, skaitmenu desimtaines dalies atskyrimui ir t.t.)tokie patys kaip ir ankstesneje uzduotyje. 
5. Visos brezinio dalys (ribos, keliai, uzrasai ir t.t.) braizomos skirtingomis spalvomis ir skirtinguose sluoksniuose. 
6. Sluoksniu skaicius neribojamas, bet sluoksniu pavadinimai turi aiskiai nusakyti ju paskirti, pavyzdziui, 'konstrukscines_linijos', 'savartyno_riba', 'koordinaciu_tinklas' ir t.t.). 
7. Braizomu liniju tipas, stricho tankumas ir spalva pasirenkama laisvai, bet brezinyje privalo buti 'Sutartiniai zenklai' su reikiamais paaiskinimais.  
8. Apsaugos zonos ribos formuojamos ir pusiaukampines  braizomos TIK konstrukcinemis linijomis (atskirame sluoksnyje).  Konstrukcines linijos 'nekarpomos', t.y. apsaugines zonos tikrosios ribos braizomos 'virs' konstrukciniu liniju ir kitame sluoksnyje.
9. Taskas Nr.13, tai uzduotyje nurodytu pusiaukampiniu susikirtimo taskas. 
10. Visos pagalbines linijos (konstrukcines linijos, pusiaukampines, keliu asys) netrinamos, t.y  paliekamos atskiruose pagalbiniuose sluoksniuoe, kurie turetu buti tik isjungti.  
11. Butina surasyti visu tasku nr. ir kitus butinus uzrasus palengvinancius brezinio informacijos suvokima (ziur.[02uzd_schema.pdf]). 
12. Visi numeruoti taskai pazymimi uzspalvintais rutuliukai (atskirame sluoksnyje).  Rutuliukai braizomi naudojant komanda [Donut] ir ivedant siuos dydzius: inside diameter... = 0, outside diameter... = 0.75 
13. Koordinaciu tinklas braizomas istisinemis konstrukcinemis linijomis, kurios 'apkarpomos' taip, kad dengtu visa brezini.  Koordinaciu reiksmiu (skaitmenu) ir koordinaciu tinklo (konstrukciniu liniju) spalva turi buti Nr.253 (ziur.[02uzd_schema.pdf])
14. Keliu linijos turi 'islysti' (uz apsaugines zonos ribos) mazdaug 7 metrus (ziur.[02uzd_schema.pdf]) 
15. Brezini apibrezti remeliu (remelio forma ir dydis nurodytas pratybu metu), uzpildyti (realiais duomenimis) brezinio legenda (stampa) ir pasirasyti.
16. Brezinio remelio dydi parinkti taip, kad tilptu visas brezinys, o lapo matmenys  butu standartiniai, t.y. A4, A3, A2 arba A1 formato (ziur.[02uzd_schema.pdf]).
17. Originalus brezinys is savo vietos nejudinamas, t.y.  brezinio lapas su remeliu 'uzdedamas' (atskirame sluoksnyje) ant brezinio, o ne brezinys stumiamas i lapa. 
18. Brezinio schema [02uzd_schema.pdf] TIK pavyzdine, t.y. brezinys braizomas pagal duomenis nurodytus Jusu uzduotyje, o ne taip kaip schemoje.
""")
