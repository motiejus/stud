Pasaulio oro uostų įdomybės
===========================

Kai mokėmės duomenų bazių, paprastai pavyzdiniai duomenų bazių modeliai būdavo
gana panašūs vienas į kitą ir nuobodūs: sumodeliuoti biblioteką, sumodeliuoti
"draugų" duomenų bazę, ar gyvūnų klasifikaciją.

Šis įrašas parodys, kaip prie nuobodžių SQL tipų greitai galima pridėti
erdvinius, ir iš karto kokius įdomius klausimus galime uždavinėti. Apie oro
uostus. :)

Duomenų bazės sukūrimas
-----------------------

Susikurkime PostgreSQL lentelę su viso pasaulio oro uostais (bent tais, kurie
turi [IATA kodą][1]). Oro uostų informaciją gausime iš [openflights.org][3].

```
$ ./managedb init
```

Visi skriptai ir `airports.dat` (oro uostų informacija) yra [šioje
repositorijoje][2]; skriptai nedideli. Kad suprastumėte toliau esančias SQL
užklausas, rekomenduoju perskaityti `init.sql`.

Kai duombazė sukurta ir duomenys importuoti, patikrinkime, kas viduje:

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

Matome Vilniaus, Rygos ir Talino oro uostų informaciją: IATA kodą, pavadinimą,
ilgumą, platumą, aukštį virš jūros lygio metrais.

Dabar, kai informacija ranka pasiekiama, užduokime kelis įdomesnius klausimus,
ir juos atsakykime.

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

Turint galvoje, kad pusė atstumo aplink žemę ties ekvatoriais yra 20037.50 km
(ties poliais - 20004 km!), atstumas tarp tolimiausių oro uostų yra gana arti
teorinio maksimumo: trūksta tik 35km iki teorinio maksimumo ties ekvatoriumi,
ir tik 2km iki teorinio maksimumo ties poliais.

**Kurie oro uostai yra arčiausiai vienas kito?**
```
SELECT
    a.country AS a_country,
    a.iata AS a_iata,
    b.country AS b_country,
    b.iata AS b_iata,
    to_char(st_y (a.geom), 'FMSG999.0000') || ',' || to_char(st_x (a.geom), 'FMSG999.0000') AS a_latlng,
    to_char(st_y (b.geom), 'FMSG999.0000') || ',' || to_char(st_x (b.geom), 'FMSG999.0000') AS b_latlng,
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

    a_country     | a_iata |    b_country     | b_iata |      a_latlng      |      b_latlng      | distance_km
------------------+--------+------------------+--------+--------------------+--------------------+-------------
 Australia        | JHQ    | Australia        | WSY    | -20.2772,+148.7556 | -20.2761,+148.7550 |      0.14
 Papua New Guinea | NDN    | Papua New Guinea | KGW    | -9.1436,+147.6842  | -9.1359,+147.6694  |      1.83
 Papua New Guinea | KGW    | Papua New Guinea | EFG    | -9.1359,+147.6694  | -9.1538,+147.6598  |      2.24
 Rwanda           | GYI    | Congo (Kinshasa) | GOM    | -1.6772,+29.2589   | -1.6708,+29.2385   |      2.38
 Papua New Guinea | NDN    | Papua New Guinea | EFG    | -9.1436,+147.6842  | -9.1538,+147.6598  |      2.92
 Papua New Guinea | BNM    | Papua New Guinea | KGW    | -9.1078,+147.6667  | -9.1359,+147.6694  |      3.13
 Virgin Islands   | SPB    | Virgin Islands   | STT    | +18.3386,-64.9407  | +18.3373,-64.9734  |      3.46
 United States    | SDM    | Mexico           | TIJ    | +32.5723,-116.9800 | +32.5411,-116.9700 |      3.59
 French Guiana    | LDX    | Suriname         | ABN    | +5.4831,-54.0344   | +5.5127,-54.0501   |      3.71
 Papua New Guinea | BNM    | Papua New Guinea | NDN    | -9.1078,+147.6667  | -9.1436,+147.6842  |      4.40
```

140 metrų atstumu esantys JHQ ir WSY oro uostai Australijoje atrodo kaip [tas
pats objektas][10]. `NDN` ir `KGW` atrodo kaip du [nupjautos žolės
ruožai, skirti nusileisti lėktuvams][4], užskaitysime!  Ketvirtosios vietos
laimėtojus tarp Ruandos ir Kongo [skiria 2.38 km][8], ir tai jau tikri nemaži
oro uostai.

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

Aukštai ir žemai esantiems oro uostams turbūt komentarų daug nereikia. Tiesa,
abejose kategorijose turime aiškias šalis-lyderes.

**Arčiausiai ašigalių esantys oro uostai?**

Čia nusižengsime iki šiol buvusiai taisyklei filtruoti oro uostus tik su IATA kodais. Jūsų malonumui:
```
SELECT
    name,
    country,
    to_char(st_y (geom), 'FMSG999.0000') || ',' || to_char(st_x (geom), 'FMSG999.0000') AS a_latlng
FROM
    airports
WHERE
    gid != 13011
ORDER BY
    abs(st_y (geom)) DESC
LIMIT 15;

               name               |  country   |      a_latlng
----------------------------------+------------+--------------------
 South Pole Station Airport       | Antarctica | -90.0000,+.0000
 Alert Airport                    | Canada     | +82.5178,-62.2806
 Nagurskoye                       | Russia     | +80.8032,+47.6636
 Eureka Airport                   | Canada     | +79.9947,-85.8142
 Ny-Ålesund Airport (Hamnerabben) | Svalbard   | +78.9275,+11.8743
 Pyramiden Heliport               | Norway     | +78.6523,+16.3372
 Svalbard Airport, Longyear       | Norway     | +78.2461,+15.4656
 McMurdo Station Pegasus Field    | Antarctica | -77.9634,+166.5250
 Svea Airport                     | Svalbard   | +77.8969,+16.7250
 Williams Field                   | Antarctica | -77.8674,+167.0570
 McMurdo Station Ice Runway       | Antarctica | -77.8540,+166.4690
 Siorapaluk Heliport              | Greenland  | +77.7865,-70.6387
 Qaanaaq Airport                  | Greenland  | +77.4886,-69.3887
 Thule Air Base                   | Greenland  | +76.5312,-68.7032
 Grise Fiord Airport              | Canada     | +76.4261,-82.9092
```

Pabaigai
--------

PostGis prie pažįstamos ir galingos PostgreSQL sąsajos suteikia erdvines
[funkcijas, duomenų tipus ir indeksavimo galimybes][9]. Jau žinant PostgreSQL,
importuoti erdvinius duomenis ir pradėti juos analizuoti reikia tikrai ne daug.

Užduotys susidomėjusiam skaitytojui:

* Kodėl artimiausių oro uostų užklausoje naudojome [<->][5], o
  tolimiausių -- [`st_distance`][6]?
* Kokį atstumą skristume aplink žemę Vilniaus platuma?
* Kiek kartų reikia nuskristi United Economy klase aplink žemę Vilniaus
  platuma, kad uždirbtume [nemokamus pusryčius][7]?

[1]: https://en.wikipedia.org/wiki/International_Air_Transport_Association_code
[2]: https://github.com/motiejus/stud/tree/master/MTM/task4-straipsnis
[3]: https://openflights.org/data.html
[4]: https://goo.gl/maps/RD3d9fsH8NwzAnsYA
[5]: https://postgis.net/docs/geometry_distance_knn.html
[6]: https://postgis.net/docs/ST_Distance.html
[7]: https://www.united.com/ual/en/us/fly/mileageplus/premier/full-premier-benefits-chart.html
[8]: https://goo.gl/maps/3usBcUHDWnefVmab6
[9]: https://postgis.net/docs/reference.html
[10]: https://goo.gl/maps/T6WQhT2FDUdymnRB9
