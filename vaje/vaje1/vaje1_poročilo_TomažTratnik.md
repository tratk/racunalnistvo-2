# Vaje 1

**Ime:** Tomaž Tratnik
**Datum:** 26.2.2022

# Delo na tabli
Na začetku smo se pogovarjali o časovni zahtevnosti metod na različnih podatkovnih strukturah, ki smo jih spoznali pri računalništvu 1 in povedali nekaj o različnih tipih in oznakah za časovne zahtevnosti.
Potem smo se skupaj lotili naloge žabice in jajca na Tomotu.

# Žabica

**Navodilo:**
Žabica se je izgubila v močvari in želi kar se da hitro odskakljati ven. Na srečo močvara vsebuje veliko muh, s katerimi si lahko povrne energijo, kajti utrujena žabica ne skoči daleč.

S funkcijo zabica(mocvara) želimo ugotoviti, kako hitro lahko žabica odskaklja iz močvare. Močvaro predstavimo s tabelo, kjer žabica prične na ničtem polju. Če je močvara dolžine k, je cilj žabice priskakljati vsaj na k-to polje ali dlje (torej prvo polje, ki ni več vsebovano v tabeli).

Energičnost žabice predstavimo z dolžino najdaljšega možnega skoka. Torej lahko žabica z količino energije e skoči naprej za katerokoli razdaljo med 1 in e, in če skoči naprej za k mest ima sedaj zgolj e - k energije. Na vsakem polju močvare prav tako označimo, koliko energije si žabica povrne, ko pristane na polju. Tako se včasih žabici splača skočiti manj daleč, da pristane na polju z več muhami. Predpostavimo, da ima vsako polje vrednost vsaj 1, da lahko žabica v vsakem primeru skoči naprej.

V primeru [2, 4, 1, 2, 1, 3, 1, 1, 5] lahko žabica odskaklja iz močvare v treh skokih, v močvari [4, 1, 8, 2, 11, 1, 1, 1, 1, 1] pa potrebuje zgolj dva.

**Rešitev:**
```
def memo(func):
    def ovojnica( k = 0, e = 0):
        if (k, e) in cache:
            return cache[(k, e)]
        else:
            cache[(k, e)] = func(k, e)
            return cache[(k, e)]


    cache = {}
    return ovojnica


def zabica(mocvara):
    @memo
    def z(e, k):
        if k >= len(mocvara):
            return 0
        e += mocvara[k]
        if e >= len(mocvara) - k:
            return 1
        najmanj = float('inf')
        for i in range(1, e + 1):
            najmanj = min(najmanj, z(k + i, e - i))
        return 1 + najmanj
    return z(0, 0)
```

**Časovna zahtevnost:**
Časovna zahtevnost je navzgor omejena z O(n^2), če je n dolžina tabele, ki predstavlja močvaro.


# Minsko polje

**Navodilo:**
Robotka moramo prepeljati čez minirano območje, ki je pravokotne oblike in je razdeljeno na n×m kvadratnih polj. Znano je, kje so mine. Na začetku je robotek parkiran v zgornjem levem polju s koordinatama (0,0). Spodnje desno polje ima koordinati (n−1,m−1). Robotek se lahko v vsakem koraku pomakne bodisi eno polje navzdol bodisi eno polje v desno. Na koliko načinov lahko pride iz začetnega na končno polje? Predpostavite lahko, da na začetnem in končnem polju ni min.

Napišite funkcijo stevilo_poti(n, m, mine), kjer sta n in m dimenziji polja, in mine seznam koordinat, na katerih so mine. Funkcija naj vrne število različnih poti med (0,0) in (n−1,m−1), ki se izognejo minam.

Namig: najprej zapišimo rekurzivno formulo za funkcijo, ki pove, koliko je poti. Naj bo S(i,j) število poti od polja (i,j) do polja (n−1,m−1). Tedaj velja:

S(i,j)=0 če je na polju (i,j) mina,
S(i,j)=S(i+1,j)+S(i,j+1), če na polju (i,j) ni mine in velja i<n−1, j<m−1,
S(n−1,m−1)=1,
S(n−1,j)=S(n−1,j+1), ker gremo lahko v spodnji vrstici samo desno,
S(i,m−1)=S(i+1,m−1), ker gremo lahko v desnem stolpcu samo navzdol.

**Rešitev:**
```
from functools import lru_cache

def stevilo_poti(n, m, mine):
    @lru_cache(maxsize=None)
    def pot(i, j):
        if (i, j) in mine:
            return 0
        if i == n - 1 and j == m - 1:
            return 1
        if i == n - 1:
            return pot(i, j + 1)
        if j == m - 1:
            return pot(i + 1, j)
        return pot(i + 1, j) + pot(i, j + 1)
    return pot(0 , 0)
```

# Vlečenje vrvi

**Navodilo:**
Udeleženci piknika bodo vlekli vrv. So različnih spolov, starosti in mas, zato sprva niso vedeli, kako bi se pravično razdelili v dve skupini. Sklenili so, da je najpravičnejša razdelitev takšna, da bosta imeli obe skupini enako skupno težo, na število članov skupin pa se sploh ne bodo ozirali. Včasih dveh skupin s popolnoma enakima masama ni mogoče sestaviti, zato iščejo takšno razdelitev, da bo razlika med masama skupin čim manjša. Vsak udeleženec nam je zaupal svojo maso v kilogramih in sicer jo je zaokrožil na najbližje celo število.

## Prva podnaloga
Sestavite funkcijo razdeli(mase), ki dobi seznam mas udeležencev in vrne skupno maso manjše od skupin pri najbolj pravični delitvi. Ta funkcija naj deluje s sestopanjem, torej pregleda vse možnosti. (Katere so vse možnosti in koliko jih je?) Zgled, v katerem je optimalna razdelitev dosežena, ko damo udeleženca z masama 102 in 95 skupaj eno skupino, vse ostale pa v drugo:
```
>>> razdeli([95, 82, 87, 102, 75])
197
```
Navodilo: naj bo skupaj skupna masa vseh udeležencev, torej vsota števil v seznamu mase. Definirajmo pomožno funkcijo deli(levi, i), ki sprejme maso levi udeležencev, ki so bili do sedaj razporejeni v levo skupino, ter indeks i naslednjega udeleženca, ki ga moramo še razporediti. Funkcija razdeli potem enostavno pokliče deli(0,0).

Funkcija deli je rekurzivna in pregleduje vse možnosti. Pri tem pazi, da masa levi ne preseže skupaj//2, da se izogne dvakratnemu pregledovanju simetričnih kombinacij. Funkcija vrne maso lažje od obeh skupin:

-če je i == len(mase), smo obravnavli vse, in vrnemo levi
-če bi dali i-tega na levo in bi s tem leva skupina presegla skupaj//2, potem ga damo na desno
-sicer rekurzivno preizkusimo obe možnosti (i-tega damo na levo ali na desno) ter se odločimo za boljšo od obeh možnosti.

**Rešitev:**
```
def razdeli(mase):
    skupaj = sum(mase) / 2
    def deli(levi, i):
        if i == len(mase):
            return levi
        if levi + mase[i] > skupaj:
            return deli(levi, i + 1)
        m1 = deli(levi, i + 1)
        m2 = deli(levi + mase[i], i + 1)
        if skupaj - m1 > skupaj - m2:
            return m2
        else:
            return m1
    return deli(0, 0)
```
**Časovna zahtevnost:**
Ta verzija ima časovno zahtevnost O(2^n)

## Druga podnaloga:
Če zgornjo rešitev preizkusite na seznamih dolžine 25 ali več, boste ugotovili, da deluje izjemno počasi. Kakšna je njena časovna zahtevnost?

Nalogo bomo rešili še z dinamičnim programiranjem. Gre za tako imenovani problem 0-1 nahrbtnika. Izkoristili bomo dejstvo, da mase ljudi ne morejo biti poljubno velike (največja dokumentirana masa človeka je 635 kg) in da so celoštevilske. Pri sestavljanju skupin lahko dosežemo enako maso na različne načine.

Sestavite funkcijo razdeli_dinamicno(mase), ki naredi isto kot prejšnja funkcija, le da se reševanja tokrat lotite z dinamičnim programiranjem. Zgled:
```
>>> razdeli_dinamicno([95, 82, 87, 102, 75])
197
```
Funkcijo preizkusite na seznamu dolžine 50 in na seznamu dolžine 100.

Navodilo: Naj bo skupaj skupna masa vseh udeležencev. Tokrat bomo izračunali množico mozna tako da bo veljalo i ∈ mozna natanko tedaj, ko je možno razdeliti udeležence tako, da ima ena od obeh skupin maso i. To lahko naredimo s preprosto zanko, upoštevajoč:

0 ∈ mozna, če damo vse udeležence v eno skupino
če imamo udeleženca z maso k, ki ga še nismo obravnavali, in je i ∈ mozna, potem velja tudi (i+k) ∈ mozna.
Ko enkrat imamo tabelo mozna, poisčemo največji indeks i, ki je manjši ali enak skupaj//2 in je mozna[i] == True.

**Rešitev:**
```
def razdeli_dinamicno(mase):
    mozna = []
    mozna.append(0)
    for k in mase:
        for i in mozna.copy():
            if i + k not in mozna:
                mozna.append(i + k)
    i = sum(mase) // 2
    while i not in mozna:
        i -= 1
    return i
```

**Časovna zahtevnost:**
Časonva zahtevnost je O(n^2).

## Tretja podnaloga
Prejšnja funkcija nam izračuna maso manjše skupine, nič pa ne izvemo o tem, kdo so udeleženci, ki tvorijo to skupino. Sestavite še funkcijo razdeli_udelezence(mase), ki vrne seznam mas udeležencev, ki bodo manjšo od obeh skupin. Če je rešitev več, lahko funkcija vrne katerekoli rešitev. Zgled:
```
>>> razdeli_udelezence([95, 82, 87, 102, 75])
[102, 95]
```
Namig: Spremenite prejšnjo rešitev tako, da bo namesto množice možnih mas skupin mozna izračunala slovar skupine. Ključi v slovarju so možne mase (torej elementi množice mozna), vrednosti pa množice, ki sestavljajo pripadajočo skupino.

**Rešitev:**
```
def razdeli_udelezence(mase):
    mozna = dict()
    mozna[0] = []
    for k in mase:
        for i in mozna.copy().keys():
            if i + k not in mozna.keys():
                mozna[i + k] = mozna[i] + [k]
    i = sum(mase) // 2
    while i not in mozna.keys():
        i -= 1
    return mozna[i]
```

**Časovna zahtevnost:**
Časonva zahtevnost je O(n^2).