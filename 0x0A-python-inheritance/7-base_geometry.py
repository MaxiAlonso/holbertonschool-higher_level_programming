#!/ume} must be greater than 0"f"{name} must be greater than 0"sr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
