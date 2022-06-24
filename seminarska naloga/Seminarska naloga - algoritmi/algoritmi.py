def naiven_alg(besedilo, vzorec, izboljsaj):
    st_primerjav = 0
    n = len(besedilo)
    m = len(vzorec)
    ujemanja = []
    for i in range(n-m + 1): #premika podniz cez besedilo
        ujema = True
        for j in range(m): #gre cez podniz/vzorec
            st_primerjav += 1
            if vzorec[j] != besedilo[i+j]: #primerja znaka na istem mestu
                ujema = False
                if izboljsaj:
                    break #ne ujema, prekine
        if ujema: #doda v tabelo, če ujema
            ujemanja.append(i)
    return ujemanja, st_primerjav

besedilo = '''In computer science, the Rabin–Karp algorithm or Karp–Rabin algorithm is a string-searching
algorithm created by Richard M. Karp and Michael O. Rabin (1987) that uses hashing to find an exact match
of a pattern string in a text. It uses a rolling hash to quickly filter out positions of the text that cannot
match the pattern, and then checks for a match at the remaining positions. Generalizations of the same idea
can be used to find more than one match of a single pattern, or to find matches for more than one pattern.'''
vzorec = 'algorithm'



def hash(besedilo, i, m, B):
    '''Polinomska hash funkcija'''
    h = 0
    for j in range(m):
        h = h + ord(besedilo[i + j]) * B**(m-1-j) # %Q
    return h # %Q

def rolling_hash(besedilo, i, m, B, prejsnji_hash, M):
    '''Polinomska rolling hash funkcija'''
    return (prejsnji_hash - ord(besedilo[i-1]) * M) * B + ord(besedilo[i + m - 1])

def RabinKarp(besedilo, vzorec, B):
    n = len(besedilo)
    m = len(vzorec)
    ujemanja = []
    
    hash_vzorec = hash(vzorec, 0, m, B) #hash vzorca
    M = B**(m-1)
    
    hash_podniz = None
    st_primerjav = 0
    for i in range(n-m + 1): #premika podniz cez besedilo
        if hash_podniz is None: #zacetna hash vrednost
            hash_podniz = hash(besedilo, i, m, B)
        else: #nova hash vrednost
            hash_podniz = rolling_hash(besedilo, i, m, B, hash_podniz, M)
            
        if hash_podniz == hash_vzorec: #enaki hash vrednosti, preverja po crkah
            ujema = True
            for j in range(m):
                st_primerjav += 1
                if vzorec[j] != besedilo[i+j]:
                    ujema = False
                    break
            if ujema:
                ujemanja.append(i)
    
    return ujemanja, st_primerjav


def hash_modulo(besedilo, i, m, B, Q):
    '''polinomska hash funkcija z modulom'''
    h = 0
    for j in range(m):
        h = (h * B + ord(besedilo[i+j])) % Q
    return h

def rolling_hash_modulo(besedilo, i, m, B, prejsnji_hash, Q, M):
    '''polinomska rolling hash funkcija s polinomom'''
    return ((prejsnji_hash + Q - (M * ord(besedilo[i - 1]) % Q )) * B + ord(besedilo[i + m - 1])) % Q

def RabinKarp_modulo(besedilo, vzorec, B, Q):
    n = len(besedilo)
    m = len(vzorec)
    ujemanja = []
    
    M = 1
    for j in range(m-1): #izrauna B^(m-1)modQ
        M *= B
        M = M % Q
    
    hash_vzorec = hash_modulo(vzorec, 0, m, B, Q) #hash vzorca
    
    hash_podniz = None
    st_primerjav = 0
    for i in range(n-m + 1): #premika podniz cez besedilo
        if hash_podniz is None: #zacetni hash podniza
            hash_podniz = hash_modulo(besedilo, i, m, B, Q)
        else: #naslednji hash podniza
            hash_podniz = rolling_hash_modulo(besedilo, i, m, B, hash_podniz, Q, M)
        
        if hash_podniz == hash_vzorec: #vrednosti ujemata
            ujema = True
            for j in range(m): #preveri po crkah
                st_primerjav += 1
                if vzorec[j] != besedilo[i+j]:
                    ujema = False
                    break
            if ujema:
                ujemanja.append(i)
    
    return ujemanja, st_primerjav


def RabinKarp_nedeter(besedilo, vzorec, B1, Q1, B2, Q2):
    n = len(besedilo)
    m = len(vzorec)
    
    M1 = 1
    M2 = 1
    for j in range(m-1):
        M1 *= B1
        M1 = M1 % Q1
        M2 *= B2
        M2 = M2 % Q2
    
    ujemanja = []
    hash_vzorec1 = hash_modulo(vzorec, 0, m, B1, Q1)
    hash_vzorec2 = hash_modulo(vzorec, 0, m, B2, Q2)
    hash_podniz1 = None
    hash_podniz2 = None
    for i in range(n-m + 1):
        if hash_podniz1 is None:
            hash_podniz1 = hash_modulo(besedilo, i, m, B1, Q1)
            hash_podniz2 = hash_modulo(besedilo, i, m, B2, Q2)
        else:
            hash_podniz1 = rolling_hash_modulo(besedilo, i, m, B1, hash_podniz1, Q1, M1)
            hash_podniz2 = rolling_hash_modulo(besedilo, i, m, B2, hash_podniz2, Q2, M2)
            
        if hash_podniz1 == hash_vzorec1 and hash_podniz2 == hash_vzorec2:
            ujemanja.append(i)
    
    return ujemanja

if __name__ == '__main__':
    print(len(besedilo), len(vzorec))
    print("Naiven algoritem brez prekinjanja:")
    print(naiven_alg(besedilo, vzorec, False))
    print("Naiven algoritem s prekinjanjem:")
    print(naiven_alg(besedilo, vzorec, True))
    
    print('Rabin-Karp brez modula:')
    print(RabinKarp(besedilo, vzorec, 257)) #najvecja ASCII koda je 255, 257 je naslednje prastevilo
    
    print('Rabin-Karp z modulom:')
    print(RabinKarp_modulo(besedilo, vzorec, 257, 999999999989))
    
    print("Nedeterminističen Rabin-Karp:")
    print(RabinKarp_nedeter(besedilo, vzorec, 257, 999999999989, 263, 1000000007))
    
    print(RabinKarp_modulo("Kdor čaka, dočaka.", "čaka", 257, 999999999989))


