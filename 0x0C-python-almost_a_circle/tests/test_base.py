#!/usr/bin/python3
"""Test Base and all other files that follows"""


import unittest
from models.base import Base


class TestingForBase(unittest.TestCase):
    """Testing fior instantion of base.py"""

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_for_float(self):
        self.assertEqual(2.2, Base(2.2).id)

    def test_for_str(self):
        self.assertEqual("Myname", Base("Myname").id)

    def test_for_list(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def tet_for_dict(self):
        self.assertEqual({"p": 1, "y": 2}, Base({"p": 1, "y": 2}).id)
