import heapq
def Poisci(f_vrednosti, odprti):
    f = float('inf')
    v = 1
    for el in odprti:
        if f_vrednosti[el-1] < f:
            f = f_vrednosti[el-1]
            v = el
    return v

def Azvezda(graf, s, t, H_razdalje):
    n = len(graf)
    odprti = [s]
    zaprti = []
    razdaljeDo = [float('inf')] * n
    razdaljeDo[s-1] = 0
    prejsnji = [0] * n #iz kje smo prisli
    f_vrednosti = [float('inf')] * n
    f_vrednosti[s-1] = H_razdalje[s-1]
    while True:
        v = Poisci(f_vrednosti, odprti)
        if v == t:
            return razdaljeDo[v-1], razdaljeDo, f_vrednosti, prejsnji
        g = razdaljeDo[v-1]
        for (i, w) in graf[v]:
            if i in zaprti:
                continue
            if i not in odprti:
                odprti.append(i)
            if f_vrednosti[i-1] > g + w + H_razdalje[i-1]:
                razdaljeDo[i-1] = g + w
                f_vrednosti[i-1] = g + w + H_razdalje[i-1]
                prejsnji[i-1] = v
        odprti.remove(v)
        zaprti.append(v)

            
#preizkus na grafu iz videa https://www.youtube.com/watch?v=eSOJ3ARN5FM&t=504s
graf = {1:[(2, 5), (3, 5)], 2:[(1, 5), (3, 4), (4, 3)], 3:[(1, 5), (2, 4), (4, 7), (5, 7), (8, 8)]}
graf[4] = [(2, 3), (3, 7), (11, 16), (12, 13), (13, 14)]
graf[5] = [(3, 7), (6, 4), (8, 5)]
graf[6] = [(5, 4), (7, 9)]
graf[7] = [(6, 9), (14, 12)]
graf[8] = [(3, 8), (4, 11), (5, 5), (9, 3)]
graf[9] = [(8, 3), (10, 4)]
graf[10] = [(9, 4), (14, 3), (16, 8)]
graf[11] = [(4, 16), (12, 5), (14, 7), (15, 4)]
graf[12] = [(4, 13), (11, 5), (13, 9)]
graf[13] = [(4, 14), (12, 9), (15, 5)]
graf[14] = [(7, 12), (10, 3), (11, 7), (16, 7)]
graf[15] = [(11, 4), (13, 5)]
graf[16] = [(10, 8), (14, 7)]

H_vrednosti = [16, 17, 13, 16, 16, 20, 17, 11, 10, 8, 4, 7, 10, 7, 5, 0]


def izpisi(graf, s, t, H_vrednosti):
    dolzina, razdalje, odprti, predhodniki = Azvezda(graf, 1, 16, H_vrednosti)
    print("Dolzina: " + str(dolzina))
    print("Razdalje:")
    print(razdalje)
    print("F vrednosti:")
    print(odprti)
    pot = [t]
    print("Pot:")
    while t != s:
        t = predhodniki[t-1]
        pot.append(t)
    for i in range(len(pot) - 1, 0, -1):
        print(pot[i], end='->')
    print(pot[0])

izpisi(graf, 1, 16, H_vrednosti)