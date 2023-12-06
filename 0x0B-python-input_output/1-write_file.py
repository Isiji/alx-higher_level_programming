#!/usr/bin/python3
"""this function writes a string to a text file"""
def write_file(filename="", text=""):
    """and returns the number of characters"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
