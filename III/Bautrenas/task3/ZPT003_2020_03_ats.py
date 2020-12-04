#!/usr/bin/python3

Lp=271 # mm
Hp=582 # mm

Lt=round(Lp*2./3., 1) # mm
Ht=round(Hp*2./3., 1) # mm

Pvid=round(4/10*(Lp-Lt), 1)
Pisr=round(6/10*(Lp-Lt), 1)

Pv=round(5/10*(Hp-Ht),1)
Pa=round(7/10*(Hp-Ht),1)

tpl="""Uzduoties Nr. 
ZPT003_2020_03
Skaiciavo(Pavarde Vardas):
Motiejus_Jakstys
Puslapio plotis Lp(mm) (duotas) 
{Lp}
Puslapio aukstis Hp(mm) (duotas) 
{Hp}
Vieta iliustracijai ILGIS(mm) (duotas) 
55
Vieta iliustracijai AUKSTIS(mm) (duotas) 
151
Iliustracijos tipas (duotas) 
Uzdara iki krasto
Teksto bloko variantas (duotas. pvz.[1.2])
OPTIMALUS
Teksto bloko plotis Lt (0.1 mm tikslumu)
{Lt}
Vidine paraste Pvid (0.1 mm tikslumu)
{Pvid}
Isorine paraste Pisr (0.1 mm tikslumu)
{Pisr}
Virsutine paraste Pv (0.1 mm tikslumu)
{Pv}
Apatine paraste Pa (0.1 mm tikslumu)
{Pa}
Teksto bloko aukstis Ht (0.1 mm tikslumu)
{Ht}
=== KAINU SKAICIAVIMAS ===
Spaudos lapo (SL) pavadinimas (duotas 02 uzd.) pvz. ULTRA62
*******
Spaudos lapo (SL) plotis Wsl (mm)(duotas 02 uzd.) 
*******
Spaudos lapo (SL) ilgis Lsl (mm)(duotas 02 uzd.) 
*******
Kiek (is viso) pagaminta popieriaus spaudos lapu (apskaiciuota 02 uzd.) 
*******
Vieno popieriaus lapo savikaina 0.00 eu (apskaiciuota 02 uzd.) 
*******
Kiek puslapiu (duoto formato) galima ispjauti is vieno SL (max. kiekis vnt.)
*******
Vieno ispjauto puslapio savikaina (0.0000 Eu tikslumu)
*******
Kiek puslapiu (is viso) galima ispjauti is visu pasigamintu SL
*******
Visas spausdinamu simboliu kiekis (vnt. paskaiciuota 01 uzd.)
*******
VISAS simboliu kiekis DOC faile (atmetus vieta iliustracijai) 
*******
VIDUTINIS simboliu kiekis puslapyje 
*******
Puslapiu kiekis visu simboliu atspausdinimui 
*******
Visu puslapiu popieriaus kaina (0.00 Eu) 
*******
Koks galimas atspausdinimo tirazas (vnt.)
*******"""

print(tpl.format(**(dict(locals()))))
