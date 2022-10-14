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
        if self.nev == other.nev:
            return ""
        return self.projekt == other.projekt


def sameproject(team):
    parok = []
    for i in team:
        for j in team:
            if i.projekt == j.projekt and i.nev != j.nev:
                if (i.nev, j.nev) not in parok and (j.nev, i.nev) not in parok:
                    parok.append((i.nev, j.nev))
    for i in parok:
        print("\n" + i[0] + " és " + i[1] + " egy projekten dolgoznak.")


if __name__ == "__main__":
    ricsi = Team("Ricsi", "SolArch", "Frontend")
    print(ricsi)
    angela = Team("Angéla", "ZerTeng", "Tesztelő")
    print(angela)
    peti = Team("Peti", "KefERP", "Backend")
    print(peti)
    eva = Team("Éva", "KefERP", "Frontend")
    print(eva)
    
    csipetcsapat = (ricsi, angela, peti, eva)
    sameproject(csipetcsapat)
