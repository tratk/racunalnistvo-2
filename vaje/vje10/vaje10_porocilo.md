# Vaje 10

**Ime:** Tomaž Tratnik
**Datum:** 21.4.2022

# Uvod
Pri vajah smo pri tabli odgovarjali na vprašanja na spletni učilnici.

# Vprašanja

**V zgoščevalno tabelo velikosti 11 (n = 11) vstavimo ključe iz seznama [23, 1, 13, 11, 24, 33, 18, 42, 31] z zgoščevalno funkcijo h(x) = x mod n. Kakšna izgleda tabela glede na različne pristope reševanja trkov. Uporabi veriženje ter linearno in kvadratično iskanje(probing). Do kakšnih problemov lahko pridemo pri teh pristopih? Kaj bi bilo, če bi uporabili kakšno drugo zgoščevalno funkcijo oblike h(x) = ax mod n za nek a različen od 0 in manjši od n? Bi lahko za poljuben a našel zaporedje ključev, ki bi ustvaril veliko trkov? Naštej še kakšne standardne zgoščevalne funkcije.**

Veriženje:	        Linearno iskanje:       Kvadratično iskanje:
0   |11, 33         0   |11                 0   |11
1   |23, 1          1   |23                 1   |23
2   |13, 24         2   |1                  2   |1
3   |               3   |13                 3   |12
4   |               4   |24                 4   |24
5   |               5   |33                 5   |33
6   |               6   |                   6   |
7   |18             7   |18                 7   |18
8   |               8   |                   8   |
9   |               9   |                   9   |
10  |42, 31 	    10  |42                 10  |42
11  |               11  |31                 11  |31

Pri teh pristopih lahko spravimo veliko ključev v isti hash. Če bi uporabili funkcijo oblike h(x) = ax mod n se ne bi nič posebej spremenilo. Zaporedje ključev, ki so večkratniki števila n, bi za poljuben a ustvarilo veliko trkov. Primer kakih drugih funkcij bi bile kriptografske funkcije, dvojno hashiranje.

**Univerzalno zgoščevanje. U (univerzalna)  in V naj bosta množici, kjer je velikost U ogromno večja kot velikost V. Družini preslikav H iz U v V rečemo univerzalna, če za vsak x != y iz U velja Pr[h(x) = h(y)] <= 1/n, kjer preslikavo h vzamemo naključno iz družine H ter n = IVI.**

**Pokaži, da je H = {ax mod n : a iz Z_n} univerzalna družina.**
a*x = a*y + k*n
a*(x-y) = k*n ( = 0 mod n)
a*(x-y) je enakomerno porazdeljen od 0 do (n-1), verjetnost, da je enaka 0 je 1/n.

**Naj bo h zgoščevalna funkcija iz univerzalne družine (izbrana naključno). Recimo, da želimo v tabelo shranit m ključev. Definiramo "load factor" alpha = m/n. Koliko je povprečno število trkov? Kaj lahko poveš o dolžini najdaljše verige? Namig: Indikatorji, linearnost pričakovane vrednosti.**

|V| = m, |S| = n
h ∈ H univerzalna
L(x) = {y ∈ S|h(x) = h(y)}

Iy = 1 za h(x) = h(y), = 0 sicer
P(Iy = 1) = P(h(x) = h(y)) <= 1/m
E(L(x)) = 1 + vsota(E(Iy)) za y∈S <= 1 + (n-1)/m <= 1 + alpha <= 2 -> povprečno število trkov