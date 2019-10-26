Trumpas įvadas į GIS programuotojui
===================================

Jei tau nesvetimos duomenų bazės ar programavimas, ir iš žinių norėjote
daugiau, šis įrašas -- jums. Labai trumpai susipažinsime, kaip sukurti
"erdvinę" duomenų bazę ir leisti naudingas užklausas.

Turinys:
- Kas yra PostGis?
- Užduoties aprašymas.
- Užduoties vykdymas.
- Pavyzdžiai.

Kas yra PostGis?
----------------

PostGis yra PostgreSQL įskiepis, pridedantis naujų duomenų tipų ir funkcijų,
skirtų dirbti su erdve. Ką tai reiškia? Išspręskime užduotį ir sužinosime.

Užduotis
--------

Susikurkime PostgreSQL lentelę su viso pasaulio oro uostais (bent tais, kurie
turi [IATA kodą][1]) ir pažaiskime su duomenimis. Turėdami visus pasaulio oro
uostus galime sugalvoti daug klausimų, bet man šiuo metu įdomu:
- kokie du oro uostai yra labiausiai nutolę vienas nuo kito?
- kurie du oro uosta yra arčiausiai vienas kito?
- kiek kartų reikia nuskristi United Economy klase iš Vilniaus į San
  Franciską ir atgal (pro Frankfurtą), kad uždirbčiau [nemokamus pusryčius][2] prieš
  skrydį?

Užduoties vykdymas
------------------

Susidarys iš kelių dalių:
- Duomenų bazės sukūrimas.
- Duomenų importavimas.
- Užklausos.

Oro uostų informaciją gausime iš [openflights.org][3]; `airports.dat` failas
jūsų patogumui yra šioje repositorijoje. Sukurkime ir importuokime duomenų bazę
(skriptai paprasti, rekomenduoju peržiūrėti):

```
$ ./managedb init
```



[1]: https://en.wikipedia.org/wiki/International_Air_Transport_Association_code
[2]: https://www.united.com/ual/en/us/fly/mileageplus/premier/full-premier-benefits-chart.html
[3]: https://openflights.org/data.html
