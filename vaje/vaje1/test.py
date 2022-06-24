from tkinter import N


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

print(zabica([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]))

def razdeli(mase):
    skupaj = sum(mase) / 2
    

    def deli(levi, i):
        global st
        st += 1
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
    return deli(0, 0), st

def razdeli_dinamicno(mase):
    n = 0
    mozna = []
    mozna.append(0)
    for k in mase:
        for i in mozna.copy():
            if i + k not in mozna:
                mozna.append(i + k)
                n += 1
    i = sum(mase) // 2
    print(mozna)
    while i not in mozna:
        i -= 1
    return i, n

print(razdeli_dinamicno([98, 99, 103, 72, 117, 88, 93, 70, 78, 90, 104, 96, 101, 79, 119, 105, 107, 109, 71, 93]))