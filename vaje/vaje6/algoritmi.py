import heapq

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

graf = {1:[(2, 1), (3, 3)], 2:[(3, 6), (4, 2), (5, 4)], 3:[(4, 1), (5, 3), (7, 6)], 4:[(6, 6), (7, 2)], 5:[(7, 2)], 6:[(3, 1), (8, 3)], 7:[(8, 1)], 8:[]}
print(DijkstraSeznam(graf, 1))