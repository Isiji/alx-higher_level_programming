#!/usr/bin/python3
if __name__ == '__main__':

    import sys
    import math

    result = 0

    for i in sys.argv[1:]:
        try:
            result += int(i)
        except ValueError:
            print("invalid input, enter an integer")

    print("{}".format(result))


