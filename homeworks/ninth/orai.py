#!/usr/bin/env python
# coding: utf8

def BuborekRendezes(lista):
    N = len(lista)
    for k in range(0, N):
        for i in range(1, N - k):
            if lista[i - 1] > lista[i]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
    print(lista)

if __name__ == "__main__":
    lista = [54, 76, 23, 45, 21, 5, 67, 22, 12, 64, 26, 59, 82, 99]
    BuborekRendezes(lista)

