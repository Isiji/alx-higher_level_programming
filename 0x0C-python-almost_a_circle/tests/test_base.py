#!/usr/bin/python3
"""Defines unittests for base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantiation(unittest.TestCase):
    """tests the base"""
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(13, Base(13).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(13)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(13)
        b.id = 18
        self.assertEqual(18, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(13).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hey", Base("hey").id)

    def test_float_id(self):
        self.assertEqual(8.25, Base(8.25).id)

    def test_complex_id(self):
        self.assertEqual(complex(6), Base(complex(6)).id)

    def test_dict_id(self):
        self.assertEqual({"first": 1, "second": 2}, Base({"first": 1, "second": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_range_id(self):
        self.assertEqual(range(6), Base(range(6)).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

