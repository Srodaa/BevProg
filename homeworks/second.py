#!/usr/bin/env python
# coding: utf8

def unit_converter(number, unit):
    unit = unit.lower()

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


if __name__ == "__main__":
    print("Kérek egy számot és egy mértékegységet (cm/inch): ")
    number = int(input())
    unit = input()
    unit_converter(number, unit)
