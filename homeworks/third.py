#!/usr/bin/env python
# coding: utf8

def editability(a, b, c):

    if (a + b) >= c and (a + c) >= b and (b + c) >= a:
        print(f"Az {a}, {b} és {c} oldalú háromszög szerkezthető.")
    else:
        print(f"Az {a}, {b} és {c} oldalú háromszög NEM szerkezthető.")


if __name__ == "__main__":
    print("Adja meg a háromszög három oldalát cm-ben: ")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))
    editability(a, b, c)