import time
import algoritmi
import os
pot = os.path.dirname(os.path.realpath(__file__))
os.chdir(pot)

with open("besedilo.txt", 'r', encoding='utf-8') as f:
    text = f.read()

vzorec = "lie"


t = time.time()
print('Naiven:')
print(algoritmi.naiven_alg(text, vzorec, True))
print(time.time() - t)

t = time.time()
print('\nRabin-Karp:')
print(algoritmi.RabinKarp(text, vzorec, 257))
print(time.time() - t)

t = time.time()
print('\nRabin-Karp modulo:')
print(algoritmi.RabinKarp_modulo(text, vzorec, 257, 999999999989))
print(time.time() - t)

t = time.time()
print('\nRabin-Karp nedeterministicen:')
print(algoritmi.RabinKarp_nedeter(text, vzorec, 257, 999999999989, 263, 1000000007))
print(time.time() - t)
