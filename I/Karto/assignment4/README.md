4 užduotis
==========

Ši užduotis buvo brėžta dviem būdais:
- autocad.
- matplotlib.

Autocad sprendime kelių linijos persidengiančios, ne visos, ir keliai yra
"bepločiai", nes neturėjau tinkamo AutoCAD.

Matplotlib sprendime kelių linijos padarytos teisingai, keliai teisingai
susloksniuoti, tačiau brėžinys nėra pilnas.

Kaip pasileisti matplotlib sprendimą?
-------------------------------------

Jis interaktyvus. Reikia [Python][1], [Matplotlib][2], [Shapely][3], [Descartes][4]:

```
$ python ./draw.py
```

Peržiūra:

![matplotlib schema][schema2]

Sugeneruoti atsakymus
---------------------

`KTZ004_2019_04_ats.txt` ir `teodolitinio_ejimo_resultatai.txt` yra sugeneruoti
priklausomai nuo pradinių duomenų (duomenys `measure.py`). Kad sugeneruotumėte
šiuos failus, reikia [Python][1], [Shapely][2] ir [Make][5] (Make
neprivalomas, patikrinkite `Makefile`):

```
$ make
```

[1]: https://python.org/
[2]: https://matplotlib.org/3.1.1/users/installing.html
[3]: https://pypi.org/project/Shapely/
[4]: https://pypi.org/project/descartes/
[5]: https://www.gnu.org/software/make/
[schema2]: https://raw.githubusercontent.com/motiejus/stud/master/Karto/assignment4/schema2.png
