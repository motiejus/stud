#!/usr/bin/python3

from math import ceil

bt = int(515.349913 * 1024)
p1 = 14000
p2 = 36878
p3 = 14214
p4 = 16253

# viso puslapiu skirtingoms sekcijoms
viso_psl_a = ceil(bt*.44*.666/(p1/6.)+bt*.44*.334/(p2/6.))
viso_psl_b = ceil(bt*.56*.657/(p3/6.)+bt*.56*.343/(p4/6.))

print("""Uzduotis Nr. 
1
Skaiciavo(Pavarde Vardas):
Jakstys Motiejus
 ===  Skaiciavimo rezultatai: ===
Zinomas informacijos kiekis (duotas)(irasyti pvz. 1.221400 GB) :  
515.349913 KB
Visas simboliu skaicius duotame informacijos kiekyje (1 simb.tiksl.):  
"""+
"%d" % bt + """
A. teksto dalies sriftas (irasyti pavadinima)(duotas) :
CAMBERIC
A. teksto dalies kiekis (0.0%)(duotas):
44.0%
Visas simboliu kiekis spausdinamas A. sriftu (1 simb.tiksl.):
"""+
"%d" % round(bt * .44) + """
A.1 teksto dalies srifto dydis (punktais) (duotas) :
16
A.1teksto dalies srifto dydzio kiekis (0.0%)(duotas):
66.6%
Visas A.1 dydzio simboliu kiekis tekste: 
"""+
"%d" % round(bt*.44*.666)  + """
Vidutinis A.1 simboliu kiekis puslapyje (1 simb.tiksl.):
"""+
"%d" % round(p1 / 6.)  + """
Popieriaus kiekis A.1 spausdinimui (0.01 psl. tiksl.):
"""+
"%.2f" % (bt*.44*.666/(p1/6.)) + """
A.2 teksto dalies srifto dydis (punktais) (duotas) :
6
A.2teksto dalies srifto dydzio kiekis (0.0%)(duotas):
33.4%
Visas A.2 dydzio simboliu kiekis tekste: 
"""+
"%d" % round(bt*.44*.334)  + """
Vidutinis A.2 simboliu kiekis puslapyje (1 simb.tiksl.):
"""+
"%d" % round(p2 / 6.)  + """
Popieriaus kiekis A.2 spausdinimui (0.01 psl. tiksl.):
"""+
"%.2f" % (bt*.44*.334/(p2/6.)) + """
Visas psl./lapu kiekis reikalingas spausdinat A. sriftu:
"""+
"%d" % viso_psl_a + """
B. teksto dalies sriftas (irasyti pavadinima)(duotas) :
AMELIA
B. teksto dalies kiekis (0.0%)(duotas):
56.0%
Visas simboliu kiekis spausdinamas B. sriftu (1 simb.tiksl.):
"""+
"%d" % round(bt * .56) + """
B.1 teksto dalies srifto dydis (punktais) (duotas) :
16
B.1teksto dalies srifto dydzio kiekis (0.0%)(duotas):
65.7%
Visas B.1 dydzio simboliu kiekis tekste: 
"""+
"%d" % round(bt*.56*.657)  + """
Vidutinis B.1 simboliu kiekis puslapyje (1 simb.tiksl.):
"""+
"%d" % round(p3 / 6.) + """
Popieriaus kiekis B.1 spausdinimui (0.01 psl. tiksl.):
"""+
"%.2f" % (bt*.56*.657/(p3/6.)) + """
B.2 teksto dalies srifto dydis (punktais) (duotas) :
14
B.2teksto dalies srifto dydzio kiekis (0.0%)(duotas):
34.3%
Visas B.2 dydzio simboliu kiekis tekste: 
"""+
"%d" % round(bt*.56*.343)  + """
Vidutinis B.2 simboliu kiekis puslapyje (1 simb.tiksl.):
"""+
"%d" % round(p4 / 6.) + """
Popieriaus kiekis B.2 spausdinimui (0.01 psl. tiksl.):
"""+
"%.2f" % (bt*.56*.343/(p4/6.)) + """
Visas psl./lapu kiekis reikalingas spausdinat B. sriftu:
"""+
"%d" % viso_psl_b + """
Tirazas (egz.)(duotas) 
173
Visas popieriaus kiekis reikalingas visu egz. atspausdinimui (0.01 psl. tiksl.)
"""+
"%.2f" % (ceil((viso_psl_a + viso_psl_b)/2)*173) + """
Popieriaus paketu kiekis (pokais 0.01 poko tikslumu)
"""+
"%.2f" % (ceil((viso_psl_a + viso_psl_b)/2)*173/200) + """
Popieriaus paketu kiekis atsargai (pokais) priklausomai nuo tirazo (0.01 poko tikslumu).
"""+
"%.2f" % (ceil((viso_psl_a + viso_psl_b)/2)*173/200*0.0114) + """
Visas popieriaus paketu kiekis (pokais)[Paskaiciuotas+Atsarga] (0.01 poko tikslumu)
"""+
"%.2f" % (ceil((viso_psl_a + viso_psl_b)/2)*173/200*1.0114) + """
Viso reikalingo popieriaus kaina (0.01 Eu tikslumu)
"""+
"%.2f" % (ceil(ceil((viso_psl_a + viso_psl_b)/2)*173/200*1.0114)*3.05) + """
Kokioje Word versijoje skaiciuoti simboliai (irasyti pvz. Word2007)
LaTeX + GNU AWK 5.0.1. LaTeX įvesties ir išvesties dokumentai ir AWK programa
prisegta. Programos išvestis duotiems kodo failams:

    ./stats.awk amelia14.tex amelia16.tex camberic16.tex camberic6.tex
    number of characters in part1: 14000
    number of characters in part2: 36878
    number of characters in part3: 14214
    number of characters in part4: 16253
""")
