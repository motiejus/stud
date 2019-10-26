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
    to_char(st_distance (a.geom, b.geom, TRUE) / 1000, '99999.99') AS distance_km
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
    a_country     |               a_name                | a_iata |        b_country        |               b_name               | b_iata | distance_km
------------------+-------------------------------------+--------+-------------------------+------------------------------------+--------+-------------
 China            | Zhangjiakou Ningyuan Airport        | ZQZ    | Argentina               | Antoine de Saint Exupéry Airport   | OES    |  20002.42
 Saudi Arabia     | King Khaled Air Base                | KMX    | French Polynesia        | Pukarua Airport                    | PUK    |  20000.78
 Indonesia        | Radin Inten II (Branti) Airport     | TKG    | Colombia                | Mariquita Airport                  | MQU    |  20000.53
 French Polynesia | Napuka Island Airport               | NAU    | Ethiopia                | Axum Airport                       | AXU    |  20000.47
 Nicaragua        | Corn Island                         | RNI    | Cocos (Keeling) Islands | Cocos (Keeling) Islands Airport    | CCK    |  20000.20
 China            | Jinggangshan Airport                | JGS    | Argentina               | Teniente Benjamin Matienzo Airport | TUC    |  19999.93
 Malaysia         | Long Lellang Airport                | LGL    | Brazil                  | Tefé Airport                       | TFF    |  19998.43
 New Zealand      | Hamilton International Airport      | HLZ    | Spain                   | Córdoba Airport                    | ODB    |  19998.36
 Indonesia        | Sultan Mahmud Badaruddin II Airport | PLM    | Colombia                | Benito Salas Airport               | NVA    |  19998.19
 Malaysia         | Sultan Ismail Petra Airport         | KBR    | Peru                    | Chachapoyas Airport                | CHH    |  19998.13
```

**Kurie oro uostai yra arčiausiai vienas kito?**
```
SELECT
    a.country AS a_country,
    a.name AS a_name,
    a.iata AS a_iata,
    b.country AS b_country,
    b.name AS b_name,
    b.iata AS b_iata,
    to_char(st_distance (a.geom, b.geom, TRUE) / 1000, '99999.99') AS distance_km
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
    a_country     |                a_name                 | a_iata |    b_country     |                       b_name                        | b_iata | distance_km
------------------+---------------------------------------+--------+------------------+-----------------------------------------------------+--------+-------------
 Australia        | Shute Harbour Airport                 | JHQ    | Australia        | Whitsunday Island Airport                           | WSY    |      0.14
 Papua New Guinea | Nadunumu Airport                      | NDN    | Papua New Guinea | Kagi Airport                                        | KGW    |      1.83
 Papua New Guinea | Kagi Airport                          | KGW    | Papua New Guinea | Efogi Airport                                       | EFG    |      2.24
 Rwanda           | Gisenyi Airport                       | GYI    | Congo (Kinshasa) | Goma International Airport                          | GOM    |      2.38
 United Kingdom   | Westray Airport                       | WRY    | United Kingdom   | Papa Westray Airport                                | PPW    |      2.83
 Papua New Guinea | Nadunumu Airport                      | NDN    | Papua New Guinea | Efogi Airport                                       | EFG    |      2.92
 Papua New Guinea | Bodinumu Airport                      | BNM    | Papua New Guinea | Kagi Airport                                        | KGW    |      3.13
 Virgin Islands   | Charlotte Amalie Harbor Seaplane Base | SPB    | Virgin Islands   | Cyril E. King Airport                               | STT    |      3.46
 United States    | Brown Field Municipal Airport         | SDM    | Mexico           | General Abelardo L. Rodríguez International Airport | TIJ    |      3.59
 French Guiana    | Saint-Laurent-du-Maroni Airport       | LDX    | Suriname         | Albina Airport                                      | ABN    |      3.71
```

**Kokį atstumą skristume aplink žemę, jei iš Vilniaus skristume ta pačia platuma?**
**Kiek kartų reikia nuskristi United Economy klase aplink žemę Vilniaus
  platumoje, kad uždirbtume [nemokamus pusryčius][2]?**


[1]: https://en.wikipedia.org/wiki/International_Air_Transport_Association_code
[2]: https://www.united.com/ual/en/us/fly/mileageplus/premier/full-premier-benefits-chart.html
[3]: https://openflights.org/data.html
