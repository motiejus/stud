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
- kurie du oro uosta yra arčiausiai vienas kito? O toje pačioje šalyje?
- kokį atstumą skristume aplink žemę, jei iš Vilniaus skristume ta pačia platuma?
- kiek kartų reikia nuskristi United Economy klase aplink žemę Vilniaus
  platumoje, kad uždirbtume [nemokamus pusryčius][2]?

Duomenų bazės sukūrimas
-----------------------

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

Sukūrėme duombazę su visais oro uostais; patikrinkime, kas viduje:

```
psql airportgames <<<"
SELECT
    iata,
    name,
    to_char(st_y (geom), '999.99') AS latitude,
    to_char(st_x (geom), '999.99') AS longitude,
    to_char(st_z (geom), '9999') AS altitude
FROM
    airports
WHERE
    iata IN ('VNO', 'RIX', 'TLL');
"
 iata |             name              | latitude | longitude | altitude
------+-------------------------------+----------+-----------+----------
 TLL  | Lennart Meri Tallinn Airport  |   59.41  |   24.83   |    40
 RIX  | Riga International Airport    |   56.92  |   23.97   |    11
 VNO  | Vilnius International Airport |   54.63  |   25.29   |   198
```

Užklausos
---------

**Kokie oro uostai yra labiausiai nutolę vienas nuo kito?**

```
SELECT
    a.country AS a_country,
    a.name AS a_name,
    a.iata AS a_iata,
    b.country AS b_country,
    b.name AS b_name,
    b.iata AS b_iata,
    to_char(st_distance (a.geom, b.geom, FALSE) / 1000, '99999.99') AS distance_km
FROM
    airports a,
    airports b
WHERE
    a.iata != '\N'
    AND b.iata != '\N'
    AND a.gid > b.gid
ORDER BY
    distance_km DESC
LIMIT 10;
```

**Kurie du oro uosta yra arčiausiai vienas kito?**
```
SELECT
    a.country AS a_country,
    a.name AS a_name,
    a.iata AS a_iata,
    b.country AS b_country,
    b.name AS b_name,
    b.iata AS b_iata,
    to_char(st_distance (a.geom, b.geom, FALSE) / 1000, '0.99') AS distance_km
FROM
    airports a,
    airports b
WHERE
    a.iata != '\N'
    AND b.iata != '\N'
    AND a.gid > b.gid
ORDER BY
    distance_km ASC
LIMIT 10;
```

Pakeitus `DESC` į `ASC` ankstesnėje užklausoje gauname:

**Kokį atstumą skristume aplink žemę, jei iš Vilniaus skristume ta pačia platuma?**
**Kiek kartų reikia nuskristi United Economy klase aplink žemę Vilniaus
  platumoje, kad uždirbtume [nemokamus pusryčius][2]?**


[1]: https://en.wikipedia.org/wiki/International_Air_Transport_Association_code
[2]: https://www.united.com/ual/en/us/fly/mileageplus/premier/full-premier-benefits-chart.html
[3]: https://openflights.org/data.html
