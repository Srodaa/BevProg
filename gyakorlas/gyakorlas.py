import datetime


def Beolvas():

    lista = []
    lista1 = []
    with open("playlist.csv", "r") as f:
        sor = f.readline()

        while sor:
            lista.append(sor.rstrip().split(";"))
            sor = f.readline()

        for i in lista:
            mydict = {}
            mydict["eloado"] = i[0]
            mydict["cim"] = i[1]
            mydict["mufaj"] = i[2]
            mydict["hossz"] = int(i[3])
            lista1.append(mydict)

        return lista1


def teljes_hossz(beolvas):
    dicti = dict()
    teljes = 0
    for i in beolvas:
        hossz = i['hossz']
        teljes += hossz
    teljesPerc = teljes // 60
    teljesMp = teljes % 60
    tenylegesHossz = f"{teljesPerc}:{teljesMp}"

    with open("02_hossz.txt", "w", encoding="utf-8") as f:
        f.write(tenylegesHossz)

def leghosszabb_rockzene(beolvas):
    lista = []
    leghosszabb = ""
    for i in beolvas:
        if i['mufaj'] == 'rock':
            rockzene = i['cim']
            lista.append(rockzene)
    max_len = len(max(lista))
    for i in range(len(lista)):
        if max_len == len(lista[i]):
            leghosszabb = lista[i]

    with open("03_leghosszabb_rock.txt", "w", encoding="utf-8") as f:
        f.write(leghosszabb)


def leggyakoribb_mufaj(beolvas):
    dicti = {}
    for i in beolvas:
        val = i.get('mufaj')
        if val in dicti:
            dicti[val] += 1
        else:
            dicti[val] = 1
    maxdb = -1
    mufaj = ""
    for i, j in dicti.items():
        if j > maxdb:
            maxdb = j
            mufaj = i

    with open("04_kedvenc_mufaj.txt", "w", encoding="utf-8") as f:
        f.write(mufaj.upper())


def zeneket_csoportosit(beolvas):
    dicti = {}
    for i in beolvas:
        val = i.get('eloado')
        if val in dicti:
            hos = i.get('hossz')
            dicti[val] += hos
        else:
            hos = i.get('hossz')
            dicti[val] = hos
    print(dicti)

    dicti = dict(sorted(dicti.items()))

    with open("05_osszegzes.txt", "w", encoding="utf-8") as f:
        for i, j in dicti.items():
            f.write(f"{i} - összesen {j} másodpercnyi zene\n")

def zeneket_listaz(beolvas, eloado):
    cim = ""
    with open(f"06_{eloado.lower().replace(' ', '_')}", "w", encoding="utf-8") as f:
        valtozo = True
        for i in beolvas:
            if i["eloado"].lower() == eloado.lower():
                f.write(f"{i['cim']};{i['mufaj']};{i['hossz']}\n")
                valtozo = False

        if valtozo:
            f.write("Nincs ilyen eloado a lejatszasi listaban!")


def zeneket_torol(beolvas, lista):
    with open("07_torolt.txt", "w", encoding="utf-8") as f:
        for i in beolvas:
            if i['eloado'] not in lista:
                f.write(f"{i['eloado']};{i['cim']};{i['mufaj']};{i['hossz']}\n")


if __name__ == "__main__":
    Beolvas()
    teljes_hossz(Beolvas())
    leghosszabb_rockzene(Beolvas())
    leggyakoribb_mufaj(Beolvas())
    zeneket_csoportosit(Beolvas())
    zeneket_listaz(Beolvas(), "Imagine Dragons")
    lista = ["Rick Astley", "Imagine Dragons"]
    zeneket_torol(Beolvas(), lista)