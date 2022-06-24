# Vaje 7

**Ime:** Tomaž Tratnik
**Datum:** 31.3.2022

# Uvod
Na vajah smo reševali naloge na tablo in odgovarjali na vprašanja zastavljena na spletni učilnici. Nato smo tekmovali v iskanju najkrajših poti. Na spletni strani https://snap.stanford.edu/data/roadNet-TX.html smo dobili datoteko z križišči in povezavami med njimi. Iz datoteke sem nato sestavil graf, ki sem ga predstavil s slovarjem, kjer so ključi križišča, vrednosti pa tabele križišč, s katerimi je to križišče povezano.

# Vprašanja

**Ponovitev Bellman Fordovega algoritma. Kaj sprejme kot vhod, kaj izračuna, predpostavke, ideja algoritma.**
Algoritem izračuna najkrajše poti od izbranega vozlišča s do vseh ostalih vozlišč v grafu. Kot vhod prejme obtežen graf G in začetno vozlišče s. Predpostvimo, da nima negativnih ciklov, dovolimo pa negativne uteži.
Ideja:
```
d = ['inf'] * n
d[s] = 0
for _ in range(n-1):
    for u, v, w in E(G):
        if d[u] + w < d[v]:
            d[v] = d[u] + w
return d
```
Kjer je n število vozlišč, w cena povezave med u in v. Časovna zahtevnost je O(|V|*|E|).

**Kaj je A*? Kako izgleda "tipična" implementacija?**
Algoritem, ki poišče njkrajšo pot v grfu med izbranim začetnim vozliščem s in končnim vozliščem t.
Implementacija je v datoteki Astar.py

**Recimo, da imamo graf v obliki mreže z ovirami. Navedi primer hevristike. Kje bi še lahko uporabili tako hevristiko?**
Če se po mreži lahko premikamo samo levo, desno, gor in dol, uporabimo Manhatansko hevristiko. Če lahko gremo tudi diagonalno, uporabimo Evklidsko.

**Recimo, da imamo graf, kjer so vozlišča mest (vasi, kraji, križišča..) in povezave ceste med njimi. Vsaka povezava e ima utež w(e), ki predstavlja razdaljo oz. pot potovanja po tej povezavi. Poleg tega ima vsaka povezava e še "ocenjen čas zastojev" w'(e, t), kjer t predstavlja trenutni čas. Ocenjen čas zastojev je tako odvisen od časa. Želimo čim hitreje dobiti odgovore na poizvedbe oblike: Kako najhitreje priti iz mesta A do mesta B. Ideja: S predprocesiranjem skonsktuirajte ustrezno hevristiko za A* algoritem.**
Uporabili bi Floyd-Warshalow algoritem f(u, v) = FW(u, w).

# Tekmovanje
## Prva naloga
Koliko vozlišč (križišč) je na najkrajši poti od vozlišča 100 do 100000?

**Rešitev:**
Za rešitev sem uporabil malce modificiran Dijkstrov algoritem, ki prejme graf, začetno vozlišče in končno vozlišče ter prešteje število križišč na najkrajši poti med njima.

```
graf = dict()
with open('roadNet-TX.txt', 'r') as f:
    for i in range(4):
        f.readline()
    vr = f.readline()
    while vr != '':
        e = int(vr.split('\t')[0])
        v = int(vr.split('\t')[1])
        if e not in graf:
            graf[e] = [v]
        else:
            graf[e].append(v)
        vr = f.readline()

def dijkstra(graf, s, t):
    n = max(graf) + 1
    razd = [float('inf')] * n
    obisk = [False] * n
    razd[s] = 0
    PQ = []
    heapq.heappush(PQ, (0, s))
    while len(PQ) != 0:
        doMin, minVoz = heapq.heappop(PQ)
        if minVoz == t:
            return doMin
        if obisk[minVoz]:
            continue
        obisk[minVoz] = True
        razd[minVoz] = doMin
        for i in graf[minVoz]:
            if not obisk[i]:
                heapq.heappush(PQ, (doMin + 1, i))
```

## Druga naloga

Recimo, da začnemo v vozlišču 0 in želimo končati v vozlišču 10000, vmes pa moramo obiskati vozlišča 1000, 3000, 5000, 8000 in 9000. Obiskujemo jih lahko v poljubnem vrstnem redu in obiščemo jih lahko tudi večkrat. Pomembno je le to, da začnemo v 0 in končamo v 10000. Poiščite čim krajšo pot, ki ustreza tem zahtevam.

**Rešitev:**
Lahko uporabimo rešitev iz prejšnje naloge. Z prejšnjo rešitev lahko recimo preštejemo število križišč na najkrajši poti med križiščem 0 in 1000. Če seštejemo število najkrajših poti med pari obvezno obiskanih križišč, dobimo najkrajšo pot med 0 in 10000. Če naredimo to za vse možne permutacije vmesnih križišč in vzamemo najmanjše število, smo dobili najmanjše število poti na poti. V praksi bi morali še preveriti, da nismo na kakšni najkrajši poti med dvema križiščema že obiskali kakega dugega, a je rekel asistent, da je v tem primeru rezultat enak.

```
def poisci(graf, s, t, vmes):
    permutacije = list(permutations(vmes))
    najmanj = float('inf')
    perm = []
    for el in permutacije:
        pot = dijkstra(graf, s, el[0]) + dijkstra(graf, el[-1], t)
        for i in range(1, len(el)):
            pot += dijkstra(graf, el[i - 1], el[i])
        if najmanj > pot:
            najmanj = pot
            perm = el
    return najmanj, perm
```