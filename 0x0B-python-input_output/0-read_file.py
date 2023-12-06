#!/usr/bin/python3
"""this function reads a text file"""
def read_file(filename=""):
    """reads the text file and prints it to the stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
