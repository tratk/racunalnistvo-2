import time
import matplotlib.pyplot as plt
import random
import Levenshtein

def sestavi_nize():
    '''Generira testne nize'''
    nizi = []
    znaki = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPrRsStTuUvVzZ., !?'
    d = len(znaki)
    dolzine = [(10, 10), (15, 15), (20, 20), (25, 25), (30, 30), (35, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60)]
    for i in range(len(dolzine)):
        d_prvi = dolzine[i][0]
        d_drugi = dolzine[i][1]
        niz1 = ''
        niz2 = ''
        for j in range(d_prvi):
            niz1 += znaki[random.randint(0, d-1)]
        for j in range(d_prvi):
            niz2 += znaki[random.randint(0, d-1)]
        nizi.append((niz1, niz2, d_prvi, d_drugi))
    return nizi

def izmeri_cas(fun, a, b):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""
    t1 = time.time()
    for i in range(100):
        n = fun(a, b)
    t2 = time.time()
    return (t2 - t1)

def narisi_graf(fun):
    '''Narise graf izvajanje funkcije na n primerih.'''
    casi = []
    nizi = sestavi_nize()
    sez_n = []
    for el in nizi:
        casi.append(izmeri_cas(fun, el[0], el[1]))
        sez_n.append(el[2] * el[3])
    plt.plot(sez_n, casi, 'r')
    plt.plot(sez_n, casi, 'bx')
    plt.xlabel('produkt dolzin nizov')
    plt.ylabel('čas stotih ponovitev [s]')
    plt.show()

narisi_graf(Levenshtein.levenshtein_iter)
narisi_graf(Levenshtein.levenshtein_rek)