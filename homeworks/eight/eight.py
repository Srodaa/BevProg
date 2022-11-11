#!/usr/bin/env python
# coding: utf8

import string


def hazi():
    lista = ""
    irasjelNelkuli = ""
    with open("hazi.txt", "r", encoding="utf-8") as f:
        sor = f.readline()
        while sor:
            if sor != "\n":
                lista += sor
            sor = f.readline()

        for i in lista:
            if i not in string.punctuation and i != " ":
                irasjelNelkuli += i

        mgh = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
        mghNelkuli = ""
        for i in irasjelNelkuli:
            if i not in mgh:
                mghNelkuli += i
                
    lines = list(mghNelkuli.split("\n"))
    with open("kimenet.txt", "w", encoding="utf-8") as file:
        for number, line in enumerate(lines):
            if (number + 1) % 3 == 0:
                file.write(line + "\n")
                # 2, 5, 8, 11, 14, 17


if __name__ == "__main__":
    hazi()
