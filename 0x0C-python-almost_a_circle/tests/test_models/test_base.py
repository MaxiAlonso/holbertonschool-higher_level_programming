"""
Unittest for the Base class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_ids(self):
        """
        Test id
        """

        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(-3)
        self.assertEqual(b4.id, -3)
        b5 = Base()
        self.assertEqual(b5.id, 2)


    def test_json_string(self):
        """
        test to_json_string method
        """

        Base._Base__nb_objects = 0
        obj = Base(33)
        dic = obj.__dict__

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(dic), '{"id": 33}')

    def test_save_to_file(self):
        """
        test save_to_file method
        """
        Base._Base__nb_objects = 0
        obj = Base(33)

        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            read = f.read()
            new_list = Base.from_json_string(read)
            self.assertEqual(new_list, [])
