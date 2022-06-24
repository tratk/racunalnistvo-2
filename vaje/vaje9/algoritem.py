import math
import matplotlib.pyplot as plt

def razdalja(t1, t2):
    return math.sqrt((t1[0] - t2[0])**2 + (t1[1] - t2[1])** 2)

def poisciMVD(datoteka):
    tocke = []
    with open(datoteka, 'r', encoding='utf-8') as f:
        vr = f.readline()
        while vr != '':
            vr = vr.split(';')
            tocke.append((float(vr[0]), float(vr[1])))
            vr = f.readline()
    n = len(tocke)
    tocke1 = tocke.copy()
    drevo = [tocke[0]]
    povezave = dict()
    del tocke[0]
    cena = 0
    for i in range(n-1):
        min_pov = float('inf')
        min_zacetna = None
        min_koncna = None
        for tocka1 in drevo:
            for tocka2 in tocke:
                d = razdalja(tocka1, tocka2)
                if d < min_pov:
                    min_pov = d
                    min_zacetna = tocka1
                    min_koncna = tocka2
        tocke.remove(min_koncna)
        drevo.append(min_koncna)
        cena += d
        if min_zacetna not in povezave:
            povezave[min_zacetna] = [min_koncna]
        else:
            povezave[min_zacetna].append(min_koncna)
    return cena, povezave, tocke1

d1, pov1, tocke1 = poisciMVD('primer1.txt')
d2, pov2, tocke2 = poisciMVD('primer2.txt')
print(d1, d2)

def narisi(tocke, povezave):
    t_x = []
    t_y = []
    for t in tocke:
        print(t)
        t_x.append(t[0])
        t_y.append(t[1])
    plt.plot(t_x, t_y, 'o', color='black')
    for t, t1 in povezave.items():
        for el in t1:
            plt.plot([t[0], el[0]], [t[1], el[1]])
    plt.show()

narisi(tocke1, pov1)
narisi(tocke2, pov2)