#!/usr/bin/python3
def uppercase(str):
    
    for j in str:
        if ord("a") <= ord(j) <= ord("z"):
            j = chr(ord(j) - 32)
        print("{:s}".format(j), end="")
    print()
