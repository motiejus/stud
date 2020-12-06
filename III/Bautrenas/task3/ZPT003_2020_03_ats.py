#!/usr/bin/python3

from consts import wc

def _pusl_kiekis(sl_ilgis_mm, sl_plotis_mm, puslapio_ilgis_mm, puslapio_plotis_mm):
    nw1, nh1 = int(sl_ilgis_mm / puslapio_ilgis_mm), int(sl_plotis_mm / puslapio_plotis_mm)
    nw2, nh2 = int(sl_ilgis_mm / puslapio_plotis_mm), int(sl_plotis_mm / puslapio_ilgis_mm)
    return max(nw1*nh1, nw2*nh2)

Lp=271 # mm
Hp=582 # mm

sl_ilgis=.75 # m
sl_plotis=.9 # m
sl_ilgis_mm=sl_ilgis*1000 # mm
sl_plotis_mm=sl_plotis*1000 # mm

Lt=round(Lp*2./3., 1) # mm
Ht=round(Hp*2./3., 1) # mm
Pvid=round(4/10*(Lp-Lt), 1)
Pisr=round(6/10*(Lp-Lt), 1)
Pv=round(5/10*(Hp-Ht),1)
Pa=round(7/10*(Hp-Ht),1)
avg_wc = round(wc / 6)

viso_pagaminta_lapu=1212
popieriaus_lapo_savikaina=0.42

pusl_kiekis=_pusl_kiekis(sl_ilgis_mm, sl_plotis_mm, Lp, Hp)
pusl_savikaina=round(popieriaus_lapo_savikaina/pusl_kiekis,4)

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
Ultra3C
Spaudos lapo (SL) plotis Wsl (mm)(duotas 02 uzd.) 
{sl_ilgis_mm}
Spaudos lapo (SL) ilgis Lsl (mm)(duotas 02 uzd.) 
{sl_plotis_mm}
Kiek (is viso) pagaminta popieriaus spaudos lapu (apskaiciuota 02 uzd.) 
{viso_pagaminta_lapu}
Vieno popieriaus lapo savikaina 0.00 eu (apskaiciuota 02 uzd.) 
{popieriaus_lapo_savikaina}
Kiek puslapiu (duoto formato) galima ispjauti is vieno SL (max. kiekis vnt.)
{pusl_kiekis}
Vieno ispjauto puslapio savikaina (0.0000 Eu tikslumu)
{pusl_savikaina}
Kiek puslapiu (is viso) galima ispjauti is visu pasigamintu SL
*******
Visas spausdinamu simboliu kiekis (vnt. paskaiciuota 01 uzd.)
*******
VISAS simboliu kiekis DOC faile (atmetus vieta iliustracijai) 
{wc}
VIDUTINIS simboliu kiekis puslapyje 
{avg_wc}
Puslapiu kiekis visu simboliu atspausdinimui 
*******
Visu puslapiu popieriaus kaina (0.00 Eu) 
*******
Koks galimas atspausdinimo tirazas (vnt.)
*******"""

print(tpl.format(**(dict(locals()))))
