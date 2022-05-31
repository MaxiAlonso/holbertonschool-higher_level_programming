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

    def to_json(self, attrs=None):
        if type(attrs) is list:
            dic = {}
            for at in attrs:
                for key, value in self.__dict__.items():
                    if key == at:
                        dic[key] = value
            return dic
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        self.__dict__.clear()
        self.__dict__.update(json)
