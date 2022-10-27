#!/usr/bin/env python
# coding: utf8

def Szorzotabla():
    elrendezes = "{0:>2}{1:>0}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}{13:>4}"
    for i in range(1, 2):
        print(
            elrendezes.format(" ", " ", i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10, i * 11,
                              i * 12))
        print(elrendezes.format("", ":", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----",
                                "----", "----"))
    for i in range(1, 13):
        print(elrendezes.format(i, ":", i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10, i * 11,
                                i * 12))


if __name__ == "__main__":
    Szorzotabla()
