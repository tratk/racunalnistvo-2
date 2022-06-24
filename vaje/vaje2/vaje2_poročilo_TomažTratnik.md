# Vaje 2

**Ime:** Tomaž Tratnik
**Datum:** 1.3.2022

## Vprašanja
**Kako dobiti število vseh optimalnih produktov?**
Število optimalnih produktov dobimo z Bellmanovo enačbo:
O(i,j) - št. optimalnih produktov za zmnožitev matrik Ai do Aj
O(i,i) = 1
O(i,j) = vsota po k(O(i,k)*O(k+1,j)), k v N(i,j), kjer smo dosegli minimum. (N(i,j) - optimalno št operacij za izracun produkta med Ai do Aj)

**Kako dobiti vse optimalne produkte?**
Iz matrike, kjer smo si shranili tiste k-je, kjer smo v algoritmu za izračun optimalnega števila operacij dobili minimum. k nam pove, na katerem mestu moramo postaviti oklepaje, nato pa enako naredimo za oba podizraza, na katera nam je začetni izraz razdelila postavitev oklepajev.

**Kaj lahko poveš v primeru, ko so vse matrike kvadratne?**
Če so vse matrike kvadratne, ni važno, v kakšnem vrstnem redu množimo.

**Kako bi algoritem poganjali na več računalnikih?**
Narišeš drevo množenj, razdeliš na podprobleme, kjer mnoćžiš samo dve matriki in razdeliš te naloge med računalnika. Nato posodobiš drevo in ponoviš.

**Problem "rezanja" palice.**
Pri tem problemu režemo palico na določenih mestih, cena reza je enaka dolžini palice.
Problem lahko zapišemo z Bellmanovo enačbo:
C(i, i) = 0
C(i, j) = L + min(C(i, k) + C(k, j)), kjer k teče od i do j
C(i, j) označuje najmanjšo ceno razreza palice z mesti reza i do j, L pa dolžino take palice.

# Postavljanje oklepajev
## Prva podnaloga
**Navodilo:**
Sestavi rekurzivno funkcijo oklepaji(izraz), ki sprejme niz izraz, v katerem nastopajo cela števila in računske operacije seštevanje, odštevanje, množenje in deljenje(števila in operatorji so ločeni s presledkom) ter vrne par '(najvecja, najmanjsa)', kjer 'najvecja' predstavlja največjo vrednost, ki jo lahko dobimo, če v izrazu dodamo oklepaje, 'najmanjsa' pa najmanjšo vrednost, ki jo lahko dobimo, če v izrazu dodamo oklepaje. Primer:
```
>>> oklepaji('1 + 5 * 6 - 3')
(33, 16)
```
Največjo vrednost dosežemo z izrazom ((1 + 5) * 6) - 3, najmanjšo pa z '1 + (5 * (6 - 3))'.

Spodaj je že napisan del kode. Ustrezno ga dopolni. Mesta, kjer je potrebno kaj dopisati so označena z ###.

**Rešitev:**
```
def oklepaji(izraz):
    ''' rekurzivno poišče največjo in najmanjšo vrednost, ki ju lahko dosežemo
    z dodajanjem oklepajev izrazu izraz '''
    if not izraz:  # izraz je prazen niz
        return 0, 0
    izraz = izraz.split()  # sestavimo seznam števil in operatorjev
    if len(izraz) == 1:  # izraz vsebuje le eno število
        return (int(izraz[0]), int(izraz[0]))
    n = len(izraz) // 2  # število operatorjev, ki nastopa v izrazu
    najvecja = -float('inf')
    najmanjsa = float('inf')
    for i in range(n):
        op = izraz[2*i+1]
        levo_max, levo_min = oklepaji(' '.join(izraz[:2*i+1]))
        desno_max, desno_min = oklepaji(' '.join(izraz[2*i+2:]))

        v1 = eval(str(levo_max) + op + str(desno_max))
        v2 = eval(str(levo_max) + op + str(desno_min))
        v3 = eval(str(levo_min) + op + str(desno_max))
        v4 = eval(str(levo_min) + op + str(desno_min))

        max_vrednost = max(v1, v2, v3, v4)
        min_vrednost = min(v1, v2, v3, v4)
        if max_vrednost > najvecja:
            najvecja = max_vrednost
        if min_vrednost < najmanjsa:
            najmanjsa = min_vrednost
    return najvecja, najmanjsa
```

**Časovna zahtevnost:**
Algoritem ima časovno zahtevnost O(n^2).

## Druga podnaloga
Sestavi funkcijo oklepaji_dinamicno(izraz), ki sprejme niz izraz, v katerem nastopajo cela števila in računske operacije seštevanje, odštevanje, množenje in deljenje(števila in operatorji so ločeni s presledkom) ter vrne par '(najvecja, najmanjsa)', kjer 'najvecja' predstavlja največjo vrednost, ki jo lahko dobimo, če v izrazu dodamo oklepaje, 'najmanjsa' pa najmanjšo vrednost, ki jo lahko dobimo, če v izrazu dodamo oklepaje. Nalogo reši z dinamičnim programiranjem. Primer:
```
>>> oklepaji_dinamicno('1 + 5 * 6 - 3')
(33, 16)
```
Največjo vrednost dosežemo z izrazom ((1 + 5) * 6) - 3, najmanjšo pa z '1 + (5 * (6 - 3))'.

Spodaj je že napisan del kode. Ustrezno ga dopolni. Mesta, kjer je potrebno kaj dopisati so označena z ###.

**Rešitev:**
```
def oklepaji_dinamicno(izraz):
    ''' poišče največjo in najmanjšo vrednost, ki ju lahko dosežemo
    z dodajanjem oklepajev izrazu izraz '''
    if not izraz:
        return 0, 0
    izraz = izraz.split()
    n = len(izraz) // 2 + 1
    vrednosti = [[(0, 0) for _ in range(n)] for _ in range(n)]

    # napolnimo glavno diagonalo
    for i in range(n): 
        vrednosti[i][i] = (int(izraz[2*i]), int(izraz[2*i]))
    
    # polnimo po naddiagonalah
    for i in range(1, n):  # katera naddiagonala
        for k in range(n-i):  # kateri zaporedni elt v naddiagonali
            najvecja = -float('inf')
            najmanjsa = float('inf')
            for j in range(i):
                levo_max, levo_min = vrednosti[k][k + j]
                desno_max, desno_min = vrednosti[k + j + 1][i + k]
                op = izraz[2*(j + k) + 1]
                
                v1 = eval(str(levo_max) + op + str(desno_max))
                v2 = eval(str(levo_max) + op + str(desno_min))
                v3 = eval(str(levo_min) + op + str(desno_max))
                v4 = eval(str(levo_min) + op + str(desno_min))

                max_vrednost = max(v1, v2, v3, v4)
                min_vrednost = min(v1, v2, v3, v4)
                if max_vrednost > najvecja:
                    najvecja = max_vrednost
                if min_vrednost < najmanjsa:
                    najmanjsa = min_vrednost
            vrednosti[k][i + k] = (najvecja, najmanjsa)  ### dopolni z ustreznimi indeksi
    
    return vrednosti[0][-1]
```

**Časovna zahtevnost:**
Algoritem ima časovno zahtevnost O(n^2).