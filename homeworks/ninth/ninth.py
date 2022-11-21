#!/usr/bin/env python
# coding: utf8

def BinarisKereses(lista):
    N = len(lista)
    counter = 0
    also, felso = 0, N - 1
    while also <= felso:
        counter += 1
        k = (felso+also) // 2
        if 70 < lista[k]:
            felso = k - 1
        elif 70 > lista[k]:
            also = k + 1
        else:
            kimenet = True, k
            break
    else:
        kimenet = False

    print(f"{counter} lépésben találta meg, {felso} a felső index, {also} az alsó indxe és {k} a k index.")


if __name__ == "__main__":
    lista = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    BinarisKereses(lista)