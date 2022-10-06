#!/usr/bin/env python
# coding: utf8

class Team:
    def __init__(self, nev, projekt, szerepkor):
        self.nev = nev
        self.projekt = projekt
        self.szerepkor = szerepkor

    def __str__(self):
        print("-- Developer létrehozva --")
        return self.nev + " a " + str(self.projekt) + "-en dolgozik " + str(self.szerepkor) + " szerepkörben."

    def __eq__(self, other):
        if self.projekt == other.projekt:
            return self.nev + " és " + other.nev + " dolgoznak egy projekten."
        else:
            return ""


if __name__ == "__main__":
    ricsi = Team("Ricsi", "SolArch", "Frontend")
    angela = Team("Angéla", "ZerTeng", "Tesztelő")
    peti = Team("Peti", "KefERP", "Backend")
    eva = Team("Éva", "KefERP", "Frontend")

    print(ricsi)
    print(angela)
    print(peti)
    print(eva)

    print(ricsi == angela)  # Teszt hamisra
    print(eva == peti)  # Teszt igazra
