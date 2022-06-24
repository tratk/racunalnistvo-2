# Vaje 9

**Ime:** Tomaž Tratnik
**Datum:** 14.4.2022

# Uvod
Na vajah smo reševali probleme v povezavi z minimalnimi vpetimi drevesi. Kot vhod smo dobili datoteko s točkami. Poiskati smo morali minimalno vpeto prevo, ki povezuje vse točke.

# Najti ceno minimalnega vpetega drevesa (drevo, ki povezuje vse točke)
Uporabil sem verzijo Primovega algoritma. Na začetku sem dodal prvo točko v drevo. Nato sem v vsakem koraku poiskal tisto točko, ki je najbližje kateri koli točki, ki je že v drevesu, in prištel to razdaljo k ceni. Hkrati sem dodajal povezave med točkami v slovar, da sem lahko na koncu drevo narisal. Implementacija je v datoteki algoritem.py.

# Dodajanje točk
Ker me ni bilo na teh vajah, sem mogoče narobe razumel, kako konstuiramo drevo. Ker so v datotekah samo točke, sem predpostavil, da lahko vsako točko povežemo s katero koli drugo. Predpostavil sem tudi, da je cena povezave kar Evklidska razdalja med točkama. V tem primeru se meni zdi, da cene že skonstruiranega drevesa z dodajanjem točk ne moremo znižati. Če dodamo točko na povezavo v drevesu, se cena drevesa ne spremeni. Takoj ko dodamo točko izven povezav, bi se pa cena drevesa povečala. V tem primeru lahko dodajamo neskončno točk, dolker jih dajamo na povezave v drevesu.