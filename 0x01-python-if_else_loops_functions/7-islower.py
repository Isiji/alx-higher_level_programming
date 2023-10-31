#!/usr/bin/python3

def islower(c):

    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False

input_char = 'b'
result = islower(input_char)
print(result)

