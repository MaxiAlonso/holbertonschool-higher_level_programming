#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    Class Student that defines a Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)
