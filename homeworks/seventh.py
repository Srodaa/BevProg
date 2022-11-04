#!/usr/bin/env python
# coding: utf8
import string


def Palindrom(mondat):
    msgh = {"a": "á", "e": "é", "i": "í", "o": "óöő", "u": "úüű"}
    duplaMsgh = ["dz", "gy", "ny", "sz", "ty", "zs", "cs", "ly"]
    triplaMsgh = ["dzs", "ggy", "nny", "ssz", "tty", "css"]
    sz = ""
    sz2 = ""
    sz3 = ""
    counter = 0

    for i in mondat:  # Kiszedi a speciális karaktereket és a szóközt, majd átadja kisebetűsen a sz-nek.
        if i not in string.punctuation and i != " ":
            sz += i.lower()

    for i in sz:  # Ha nincs benne ékezet továbbadja a szoveg2nek, ha van benne akkor pedig kicseréli.
        if i not in "áéíóöőúüű":
            sz2 += i
        else:
            for x, y in msgh.items():
                if i in y:
                    sz2 += x
                    break

    while counter < len(sz2):
        ketto = ""
        harom = ""
        if counter != len(sz2) - 1:
            ketto = sz2[counter] + sz2[counter + 1]
        if counter < len(sz2) - 2:
            harom = sz2[counter] + sz2[counter + 1] + sz2[counter + 2]
        if harom in triplaMsgh:
            sz3 += harom[::-1]
            counter += 2
        elif ketto in duplaMsgh:
            sz3 += ketto[::-1]
            counter += 1
        else:
            sz3 += sz2[counter]
        counter += 1
    print(sz2)
    print(sz3[::-1])
    if sz2 == sz3[::-1]:
        print("Ez a mondat egy palindróm!")
    else:
        print("Ez a mondat nem egy palindróm!")


if __name__ == "__main__":
    mondat = input("Kérek egy mondatot:")
    Palindrom(mondat)
