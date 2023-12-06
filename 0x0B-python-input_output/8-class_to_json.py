#!/usr/bin/python3
"""Defines a Python JSON function"""

def class_to_json(obj):
    """Return the dictionary representation"""
    return obj.__dict__
