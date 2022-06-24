# Vaje 4
**Ime:** Tomaž Tratnik
**Datum:** 15.3.2022

Na vajah smo delali naloge iz podzaporedji na Tomotu.ž

# Najdaljše padajoče podzaporedje

## 1. podnaloga
**Navodilo:**
Sestavi rekurzivno funkcijo padajoce_podzaporedje_rekurzivno(zaporedje), ki za dano zaporedje vrne dolžino najdaljšega padajočega podzaporedja.

Kako lahko pospešimo delovanje funkcije?

**Rešitev:**
```
from functools import lru_cache
    
def padajoce_podzaporedje_rekurzivno(zaporedje):
    najdaljse = 0
    
    @lru_cache(maxsize=None)
    def rekurzija(ind, prejsnji):
        if ind >= len(zaporedje):
            return 0
        if zaporedje[ind] >= prejsnji:
            return rekurzija(ind + 1, prejsnji)
        else:
            return max(rekurzija(ind + 1, prejsnji), 1 + rekurzija(ind + 1, zaporedje[ind]))
    
    for i in range(len(zaporedje) - 1):
        dolzina = rekurzija(i + 1, zaporedje[i])
        najdaljse = max(najdaljse, dolzina + 1)
    
    return najdaljse
```

**Komentarji:**
Nalogo je bilo potrebno rešiti z rekurzijo. Ker rekurzija izračuna najdaljše podzaporedje samo za podzaporedja, ki se začnejo na elementu, za katerega jo naprej kličemo, je bilo treba z zanko klicati rekurzivno funkcijo za vsak element v zaporedju. Rekurzijo sem pospešil z memoizacijo.

## 2. podnaloga
**Navodilo:**
Sestavi funkcijo padajoce_podzaporedje_tabela(zaporedje), ki za dano zaporedje vrne dolžino najdaljšega padajočega podzaporedja. Funkcija naj ne bo rekurzivna, temveč naj si delne rešitve shranjuje v tabelo.

**Rešitev:**
```
def padajoce_podzaporedje_tabela(zaporedje):
    n = len(zaporedje)
    lis = [1]*n
    najdaljse = 0
 
    for i in range(1, n):
        for j in range(0, i):
            if zaporedje[i] < zaporedje[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                najdaljse = max(najdaljse, lis[i])
    return najdaljse
```

**Komentarji:**
Nalogo je bilo treba rešiti iterativno, s pomočjo tabele, ki na vsakem mestu hrani dolžino najdaljšega padajočega podzaporedja, ki se konča na tistem mestu v zaporedju. Na koncu je treba samo vrniti največji člen v tabeli.

## 3. podnaloga
**Navodilo:**
Sestavi funkcijo padajoce_podzaporedje(zaporedje), ki za dano zaporedje vrne najdaljše padajoče podzaporedje. Podzaporedje naj vrne kot seznam. Če je rešitev več, naj vrne tisto z najmanjšimi indeksi.

**Rešitev:**
```
def padajoce_podzaporedje(zaporedje):
    n = len(zaporedje)
    lis = [1]*n
    zaporedja = []
 
    for i in range(0, n):
        zap = [zaporedje[i]]
        for j in range(0, i):
            if zaporedje[i] < zaporedje[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                zap = zaporedja[j] + [zaporedje[i]]
        zaporedja.append(zap)
    
    najdaljse = []
    for el in zaporedja:
        if len(el) > len(najdaljse):
            najdaljse = el
    return najdaljse
```

**Komentarji:**
Nalogo sem rešil tako, da poleg tabele, ki hrani dolžino najdaljšega zaporedja na mestu v zaporedju, hrani še tabelo teh najdaljših podzaporedji. Na koncu je treba vrniti prvo izmed najdaljših.

## 4. podnaloga
**Navodilo:**
Sestavi funkcijo vsa_padajoca_podzaporedja(zaporedje), ki za dano zaporedje vrne vsa najdaljša padajoča podzaporedja. Vsako podzaporedje naj bo predstavljeno s terico (tuple), rešitev pa naj bo podana kot množica podzaporedij.

**Rešitev:**
```
def vsa_padajoca_podzaporedja(zaporedje):
    n = len(zaporedje)
    lis = [1]*n
    zaporedja = []
 
    for i in range(0, n):
        zap = (zaporedje[i],)
        for j in range(0, i):
            if zaporedje[i] < zaporedje[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                zap = zaporedja[j] + (zaporedje[i],)
            elif zaporedje[i] < zaporedje[j] and lis[i] == lis[j] + 1:
                zap = [zap, zaporedja[j] + (zaporedje[i],)]
        zaporedja.append(zap)
    
    najdaljse = []
    for el in zaporedja:
        if isinstance(el, tuple):
            if len(najdaljse) == 0:
                najdaljse = [el]
            else:
                if len(el) > len(najdaljse[0]):
                    najdaljse = [el]
                elif len(el) == len(najdaljse[0]):
                    najdaljse.append(el)
        else:
            for e in el:
                if len(najdaljse) == 0:
                    najdaljse = [e]
                else:
                    if len(e) > len(najdaljse[0]):
                        najdaljse = [e]
                    elif len(e) == len(najdaljse[0]):
                        najdaljse.append(e)
    return najdaljse
```

**Komentarji:**
Nalogo sem rešil tako, da v primeru, ko imamo več enako dolgih podzaporedji, shranim oboje v tabelo. Čeprav mi je Tomo sprejel rešitev, pa moja rešitev v splošnem ne bi delovala.

# Največja vsota podzaporedja
**Navodilo:**
Sestavi funkcijo max_podzaporedje_lihi(zaporedje), ki za dano zaporedje vrne najdaljše naraščajoče podzaporedje, sestavljeno iz samih lihih števil.

Funkcije ne piši iz nule, ampak si pomagaj z rešitvami prejšnjih podnalog.

**Rešitev:**
```
def max_podzaporedje_vsota(zaporedje):
    n = len(zaporedje)
    if n == 0:
        return 0
    lis = [1] * n
    vsote = [0] * n
    vsote[0] = zaporedje[0]
 
    for i in range(1, n):
        for j in range(0, i):
            if zaporedje[i] > zaporedje[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                vsote[i] = vsote[j] + zaporedje[i]
    return max(vsote)
```

**Komentarji:**
Pri tej nalogi sem v tabelo vsote na vsakem mestu hranil vsoto najdaljšega naraščujočega podzaporedja, ki se konča na tistem mestu. Na koncu sem samo vrnil največjo vsoto.

# Najdaljše naraščujoče podzaporedje lihih členov
**Navodilo:**
Sestavi funkcijo max_podzaporedje_lihi(zaporedje), ki za dano zaporedje vrne najdaljše naraščajoče podzaporedje, sestavljeno iz samih lihih števil.

Funkcije ne piši iz nule, ampak si pomagaj z rešitvami prejšnjih podnalog.

**Rešitev:**
```
def max_podzaporedje_lihi(zaporedje):
    n = len(zaporedje)
    lis = [1]*n
    zaporedja = []
    najdaljse = []
 
    for i in range(0, n):
        if zaporedje[i] % 2 != 0:
            zap = [zaporedje[i]]
            for j in range(0, i):
                if zaporedje[i] > zaporedje[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                    zap = zaporedja[j] + [zaporedje[i]]
            zaporedja.append(zap)
        else:
            zaporedja.append([])
            lis[i] = 0
        
    for el in zaporedja:
        if len(el) > len(najdaljse):
            najdaljse = el
    
    return najdaljse
```

**Komentarji:**
Pri tej nalogi sem uporabil rešitev iz tretje podnaloge iz nalogenajdaljše padajoče podzaporedje, le da sem upošteval samo lihe člene. Za sode člene pa sem v tabelo zaporedja dodal prazne tabele, da ni prišlo do težav z indeksi.

# Sod - lih

## 1. podnaloga
**Navodilo:**
Sestavi funkcijo 'sod_lih(zaporedje)', ki vrne dolžino najdaljšega naraščajočega podzaporedja zaporedja 'zaporedje', sestavljenega iz izmenično lihih in sodih členov (prvi člen je lahko tako lih kot sod).

**Rešitev:**
```
def sod_lih(zaporedje):
    n = len(zaporedje)
    lis = [1]*n
    najdaljse = 0
    for i in range(1, n):
        sodo = zaporedje[i] % 2 == 0
        for j in range(i):
            sodoj = zaporedje[j] % 2 == 0
            if zaporedje[i] > zaporedje[j] and lis[i] < lis[j] + 1 and sodo != sodoj:
                lis[i] = lis[j] + 1
                najdaljse = max(najdaljse, lis[i])
    return najdaljse 
```

**Komentarji:**
Tu je rešitev podobna kot v prvi podnalogi iz naloge najdaljše padajoče podzaporedje, le da sem dodal pogoj, ki preveri, da so v zaporedju izmenično soda in liha števila.

## 2. podnaloga
**Navodilo:**
Sestavi funkcijo 'sod_lih_podzap(zaporedje)', ki vrne najdaljše naraščajoče podzaporedje zaporedja 'zaporedje', sestavljenega iz izmenično lihih in sodih členov (prvi člen je lahko tako lih kot sod).

**Rešitev:**
```
def sod_lih_podzap(zaporedje):
    n = len(zaporedje)
    lis = [1]*n
    zaporedja = []
    for i in range(0, n):
        sodo = zaporedje[i] % 2 == 0
        zap = [zaporedje[i]]
        for j in range(i):
            sodoj = zaporedje[j] % 2 == 0
            if zaporedje[i] > zaporedje[j] and lis[i] < lis[j] + 1 and sodo != sodoj:
                lis[i] = lis[j] + 1
                zap = zaporedja[j] + [zaporedje[i]]
        zaporedja.append(zap)
    
    najdaljse = []
    for el in zaporedja:
        if len(el) > len(najdaljse):
            najdaljse = el
    return najdaljse
```

**Komentarji:**
Spet enaka rešitev kot v tretji podnalogi naloge najdaljše padajoče podzaporedje, kateri sem spet dodal pogoj, ki preveri, da so v podzaporedju izmenično soda in liha števila.