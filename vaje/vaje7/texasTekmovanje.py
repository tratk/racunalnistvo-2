import heapq
from itertools import permutations
import os

pot = os.path.dirname(os.path.realpath(__file__))
os.chdir(pot)

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

#print(poisci(graf, 0, 10000, [1000, 3000, 5000, 8000, 9000]))
print(dijkstra(graf, 100, 100000))