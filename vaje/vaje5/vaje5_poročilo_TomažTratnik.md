# Vaje 5

**Ime:** Tomaž Tratnik
**Datum:** 22.3.2022

# Uvod
Na vajah smo reševali naloge na tablo in odgovarjali na vprašanja zastavljena na spletni učilnici.

# Vprašanja
## Kaj računa in kako deluje Floyd Warshallov algoritem? Kakšna je časovna zahtevnost?
Floyd Warrshalov algoritem izračuna najkrajše poti med vsemi pari vozlišč v obteženem usmerjenem grafu. Če z Pij(k) označimo najkrajšo pot med vozliščem i in j v k-tem koraku algoritma lahko algoritem zapišemo z Bellmanovo enačbo:
Pij(k) = min(Pij(k-1), Pim(k-1) + Pmj(k-1)) po vseh vozliščih m ki niso i ali j
Pij(0) = Uij - utež na poti med i in j
Naredimo toliko korakov kot je vozlišč v grafu. Časovna zahtevnost algoritma je O(n^3).

## Za spodnji graf izračunaj vse najkrajše poti s pomočjo Floyd Warshalovega algoritma:
![FWpostoprk](FWpostopek.jpg)
Nato dodamo vozlišče 10 in povezavo (5 -> 10) z utežjo -1 in (10 -> 6) z utežjo 2. Kako uporabil prejšnje rezultate, da bi izračunal nove najkrajše poti?

V matriko dodamo novo vozlišče, torej dodaten stoplec in vrstico. Na vsakem koraku moramo spremenit samo zadnjo vrstico in stolpec nato pa opraviti še en korak za novo vozlišče.

## Na predavanjih ste poleg izračuna matrike D(n) izračunali tudi P(n). Kaj lahko iz njih razberemo? Kako dobimo najkrajšo pot med i in j?
Iz matrike P(n) lahko razberemo najkrajše poti med vozlišči. Najkrajše poti dobimo z algoritmem:
```
def min_pot(P, i, j):
    pot = [j]
    while i != j:
        j = P[i][j]
        pot = [j] + pot
    return pot
```
## Ali imamo v omrežju lahko več najkrajših poti med dvema vozliščema? Kaj FW naredi v tem primeru? Konstruiraj graf, ki ima ogromno najkrajših poti. Bi lahko preštel vse take poti?
V omrežju lahko imamo več najkrajših poti, na primer, če gre iz vozlišča 1 v 2 pot s ceno 2 in iz vozlišča 1 v 3 in iz 3 v 2 poti s ceno 1. V takem primeru F-W izbere eno od teh, odvisno od implementacije.
Primer grafa z eksponentnim številom poti bi bil grafkjer se ponavlja vzorec, v katerem se iz enega vozlišča razdeli pot v dve vozlišči in nato spet združi v eno vozlišče. V takem grafu bi bilo število najkajših poti O(2^n), kjer je n število vzorcev.

## Kako bi s FW algoritmom odkrili, če v grafu obstajajo negativni cikli? Kaj vrne FW, če graf vsebuje negativen cikel?
Z F-W algoritmom bi odkrili negativen cikel tako, da bi preverjali, ali se kaki elementi v diagonali spremenijo iz ničle, saj bi v takem primeru našli negativno pot iz vozlišča v samega vase.

Če imamo negativen cikel v grafu, lahko dobimo v algoritmu eksponentno velika negativna števila.

## Uteži sedaj dodamo še na vozlišča. Kako bi sedaj poiskal vse najkrajše poti?
V tem primeru lahko spremenimo graf, na katerem izvajamo algoritem.Vsaki povezavi, ki kaže v neko vozlišče, prištejemo težo tistega vozlišča. Sedaj lahko poženemo F-W algoritem na takem grafu brez uteži v vozliščih.