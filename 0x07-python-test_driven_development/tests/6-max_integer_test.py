#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unittests for the function def max_integer(list=[])
    """

    def test_intergers(self):
        """
        Testing signed and unsigned intergers
        """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4e100]), 4e100)
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([-31, 0, -3, -24]), 0)

    def test_floats(self):
        """
        Testing signed and unsigned floats
        """

        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)
        self.assertEqual(max_integer([0., 0.0]), 0.0)
        self.assertEqual(max_integer([-1.5, -2.5, -3.8, -4.0]), -1.5)

    def test_strings(self):
        """
        Testing strings
        """

        self.assertEqual(max_integer(["abc", "xyz"]), "xyz")
        self.assertEqual(max_integer(["a", "j", "h", "w"]), "w")
        self.assertEqual(max_integer(["a", "Z"]), "a")
        self.assertEqual(max_integer("12345678"), "8")
        self.assertEqual(max_integer("Cohort 17 from Holberton School"), "t")

    def test_none(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "Hello World", True])
        with self.assertRaises(TypeError):
            max_integer([False, None, -3.14])
        with self.assertRaises(TypeError):
            max_integer([[1, 2, 3], (5, 2)])
