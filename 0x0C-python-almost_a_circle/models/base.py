#!/usr/bin/python3
"""
Bass class
"""


import json


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instanitation
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            string = "[]"
        else:
            string = json.dumps(list_dictionaries)

        return string
