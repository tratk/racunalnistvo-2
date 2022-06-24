# Vaje 1

**Ime:** Tomaž Tratnik
**Datum:** 26.2.2022

# Uvod
Na vajah smo reševali naloge na tablo in odgovarjali na vprašanja zastavljena na spletni učilnici.

# Vprašanja

**Simuliraj Dijkstrov algoritem na spodnjem grafu.**
Bom dodal kar sliko, kar smo reševali na tablo.
![Delo na tabli](dijkstra.jpg)

**Napiši algoritem (v čim bolj python sintaksi) s katerim si rešil zgornji problem. Probaj napisat še algoritem z uporabo prioritetne vrste. Primerjaj časovne zahtevnosti teh dveh algoritmov in komentiraj v katerih primerih bi uporabil kateri algoritem. Primerjaj še z FW algoritmom iz prejšnjih vaj.**
Oba algoritma sem implementiral za graf, ki je predstavljen s slovarjem {št_vozlišča:[(št_vozlišča, cena_povezave), ...], ...}.
Osnovni algoritem:
```
def dobiMin(razd, obisk):
    r = float('inf')
    v = 0
    for i in range(len(razd)):
        if not obisk[i] and razd[i] < r:
            v = i + 1
            r = razd[i]
    return v

def DijkstraSeznam(graf, s):
    n = len(graf)
    razd = [float('inf')] * n
    obisk = [False] * n
    razd[s-1] = 0
    Q = set()
    for el in graf.keys():
        Q.add(el)
    while len(Q) != 0:
        v = dobiMin(razd, obisk)
        if obisk[v-1]:
            continue
        doMin = razd[v-1]
        for (i, w) in graf[v]:
            if doMin + w < razd[i-1]:
                razd[i-1] = doMin + w
        obisk[v-1] = True
        Q.remove(v)
    return razd
```
Ta algoritem ima časovno zahtevnost O(|V|^2).

Algoritem s prioritetno vrsto:
```
def DijkstraQ(graf, s):
    n = max(graf)
    razd = [float('inf')] * n
    obisk = [False] * n
    razd[s-1] = 0
    PQ = []
    heapq.heappush(PQ, (0, s))
    while len(PQ) != 0:
        doMin, minVoz = heapq.heappop(PQ)
        if obisk[minVoz-1]:
            continue
        obisk[minVoz-1] = True
        razd[minVoz-1] = doMin
        for (i, w) in graf[minVoz]:
            if not obisk[i-1]:
                heapq.heappush(PQ, (doMin + w, i))
    return razd
```
Ta algoritem ima časovno zahtevnost O(|E| + |V|*log|E|).

**Kako bi modificiral Dijkstrov algoritem, da bi poleg najcenejše vrnil še najkrajšo pot (ali kakšno drugo "sestavljeno" metriko")?**
Za najkrajšo pot bi se pretvarjali, da imajo vse povezave v grafu ceno 1 (v for zanki bi namesto z w preverjali in prištevali 1). V tem primeru bi bila najcenejša pot tudi najkrajša.

**Poizkusi opustiti predpostavko o nenegativnih utežeh, tako da vsem povezavam prišteješ tako število, da postanejo nenegativne. Kje je glavni problem tega pristopa?**
Težava je, da kaznujemo poti, ki so daljše, ker vsaki povezavi prištejemo enako konstanto, zato algoritem ne vrača več pravih najkrajših poti.

**Probaj modificirat Dijkstro, da poišče najdaljšo pot. Kje je problem? Pokaži, da je problem najdaljše poti v grafu "zelo težak" (Namig: Hamiltonova pot). Za kakšne grafe bi lahko poiskali najdaljšo pot/poti? Kakšen algoritem bi tam uporabili?**
