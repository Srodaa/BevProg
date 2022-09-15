#!/usr/bin/env python
# coding: utf8

# 1.

print("Adjon meg egy mondatot: ")
txt = input()

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


########################################
# 2.

print("Kérek egy számot és egy mértékegységet (cm/inch): ")
number = int(input())
unit = input()
while unit != "inch" or unit != "cm":
    if unit == "inch":
        print(number * 2.54, "cm")
        break
    elif unit == "cm":
        print(number / 2.54, "inch")
        break
    else:
        print("Not correct unit!")
        break
