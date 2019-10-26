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
turi [IATA kodą][1]) ir pažaiskime su duomenimis. Toliau tekste -- atsakymas į keletą 
su kelionėmis ir oro uostais susijusių klausimų.

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
    a.iata AS a_iata,
    b.country AS b_country,
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

    a_country     | a_iata |        b_country        | b_iata | distance_km
------------------+--------+-------------------------+--------+-------------
 China            | ZQZ    | Argentina               | OES    |  20002.42
 Saudi Arabia     | KMX    | French Polynesia        | PUK    |  20000.78
 Indonesia        | TKG    | Colombia                | MQU    |  20000.53
 French Polynesia | NAU    | Ethiopia                | AXU    |  20000.47
 Nicaragua        | RNI    | Cocos (Keeling) Islands | CCK    |  20000.20
 China            | JGS    | Argentina               | TUC    |  19999.93
 Malaysia         | LGL    | Brazil                  | TFF    |  19998.43
 New Zealand      | HLZ    | Spain                   | ODB    |  19998.36
 Indonesia        | PLM    | Colombia                | NVA    |  19998.19
 Malaysia         | KBR    | Peru                    | CHH    |  19998.13
```

**Kurie oro uostai yra arčiausiai vienas kito?**
```
SELECT
    a.country AS a_country,
    a.iata AS a_iata,
    b.country AS b_country,
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
    a.geom <-> b.geom ASC
LIMIT 10;

    a_country     | a_iata |    b_country     | b_iata | distance_km
------------------+--------+------------------+--------+-------------
 Australia        | JHQ    | Australia        | WSY    |      0.14
 Papua New Guinea | NDN    | Papua New Guinea | KGW    |      1.83
 Papua New Guinea | KGW    | Papua New Guinea | EFG    |      2.24
 Rwanda           | GYI    | Congo (Kinshasa) | GOM    |      2.38
 United Kingdom   | WRY    | United Kingdom   | PPW    |      2.83
 Papua New Guinea | NDN    | Papua New Guinea | EFG    |      2.92
 Papua New Guinea | BNM    | Papua New Guinea | KGW    |      3.13
 Virgin Islands   | SPB    | Virgin Islands   | STT    |      3.46
 United States    | SDM    | Mexico           | TIJ    |      3.59
 French Guiana    | LDX    | Suriname         | ABN    |      3.71
```

Dėl pirmų 4 oro uostų įrodymų neradau, kad jie greta, bet WRY ir PPW
tikrai [netoli][4].

**Aukščiausiai virš jūros lygio esantys oro uostai?**

```
SELECT
    iata,
    name,
    country,
    to_char(st_z (geom), '9999') AS altitude_m
FROM
    airports
ORDER BY
    altitude_m DESC
LIMIT 10;

 iata |                  name                  | country | altitude_m
------+----------------------------------------+---------+------------
 DCY  | Daocheng Yading Airport                | China   |  4411
 BPX  | Qamdo Bangda Airport                   | China   |  4334
 KGT  | Kangding Airport                       | China   |  4280
 NGQ  | Ngari Gunsa Airport                    | China   |  4274
 LPB  | El Alto International Airport          | Bolivia |  4071
 POI  | Capitan Nicolas Rojas Airport          | Bolivia |  3936
 YUS  | Yushu Batang Airport                   | China   |  3906
 \N   | Copacabana Airport                     | Bolivia |  3838
 JUL  | Inca Manco Capac International Airport | Peru    |  3826
 GMQ  | Golog Maqin Airport                    | China   |  3787
```

**Žemiausiai po jūros lygiu esantys oro uostai?**

```
SELECT
    iata,
    name,
    country,
    to_char(st_z (geom), 'FMSG999.00') AS altitude_m
FROM
    airports
WHERE
    iata != '\N'
ORDER BY
    st_z (geom) ASC
LIMIT 10;

 iata |                 name                 |    country    | altitude_m
------+--------------------------------------+---------------+------------
 MTZ  | Bar Yehuda Airfield                  | Israel        | -385.88
 EIY  | Ein Yahav Airfield                   | Israel        | -49.99
 TRM  | Jacqueline Cochran Regional Airport  | United States | -35.05
 GUW  | Atyrau Airport                       | Kazakhstan    | -21.95
 RZR  | Ramsar Airport                       | Iran          | -21.34
 ASF  | Astrakhan Airport                    | Russia        | -19.81
 NSH  | Noshahr Airport                      | Iran          | -18.59
 IPL  | Imperial County Airport              | United States | -16.46
 NJK  | El Centro NAF Airport (Vraciu Field) | United States | -12.80
 RAS  | Sardar-e-Jangal Airport              | Iran          | -12.19
```

Pabaiga
-------

Kaip matėme šiame įraše, PostGis suteikia erdvines funkcijas, duomenų tipus ir
indeksus prie patogios ir pažįstamos PostgreSQL sąsajos.

Užduotys susidomėjusiam skaitytojui:
* Kodėl artimiausių oro uostų užklausoje naudojome [<->][5], o
  tolimiausių -- [st_distance][6]?
* Kokį atstumą skristume aplink žemę, jei iš Vilniaus skristume ta pačia platuma?
* Kiek kartų reikia nuskristi United Economy klase aplink žemę Vilniaus
  platumoje, kad uždirbtume [nemokamus pusryčius][2]?


[1]: https://en.wikipedia.org/wiki/International_Air_Transport_Association_code
[2]: https://www.united.com/ual/en/us/fly/mileageplus/premier/full-premier-benefits-chart.html
[3]: https://openflights.org/data.html
[4]: https://goo.gl/maps/CCkqFvhN9rWfrsxT6
[5]: https://postgis.net/docs/geometry_distance_knn.html
[6]: https://postgis.net/docs/ST_Distance.html
