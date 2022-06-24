from functools import lru_cache


@lru_cache(maxsize = None)
def levenshtein_rek(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    if a[0] == b[0]:
        return levenshtein_rek(a[1:], b[1:])
    else:
        return 1 + min(levenshtein_rek(a[1:], b[1:]), levenshtein_rek(a[1:], b), levenshtein_rek(a, b[1:]))


def levenshtein_iter(a, b):
    
    if len(a) == 0 and len(b) == 0:
        return 0
    elif len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    n = len(a) + 1
    m = len(b) + 1
    tab = [[0 for i in range(m)] for j in range(n)]
    for i in range(1, n):
        tab[i][0] = i
    for i in range(1, m):
        tab[0][i] = i    
    
    for i in range(1, m):
        for j in range(1, n):
            if a[j - 1] == b[i - 1]:
                cena = 0
            else:
                cena = 1
            tab[j][i] = min(tab[j - 1][i] + 1, tab[j][i - 1] + 1, tab[j - 1][i - 1] + cena)
    
    return tab[-1][-1]

