#!/usr/bin/env python
# coding: utf8

def divide():

    a = int(input("Enter 'a' value: "))
    b = int(input("Enter 'b' value: "))
    c = a / b
    print(c)


def exceptions():
    while True:
        try:
            divide()
        except ZeroDivisionError:
            print("Division by zero not allowed")
        finally:
            print("Out of try except blocks")


if __name__ == "__main__":
    exceptions()
