#!/usr/bin/env python
# coding: utf8

def sentence(name):

    countdict = {}
    for x in txt:
        if x not in countdict:
            countdict[x] = 1
        else:
            countdict[x] += 1
    print(countdict)

    print(txt[::-1])

    mylist = txt.split()
    print("Listába rendezve szavanként: ", mylist)

if __name__ == "__main__":
    print("Adjon meg egy mondatot: ")
    txt = input()
    sentence(txt)
