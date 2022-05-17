#!/usr/bin/python3
'''
Class Square that defines a square
'''


class Square:
    '''
    Square Class
    '''

    def __init__(self, size=0):
        '''
        Initializes a Square

        Size is private attribute because the size of a square is crucial
        for a square, many things depend of it (area computation, etc.) and
        keep it privately is one of the ways to have the control of size.
        '''

        self.__size = size

    @property
    def size(self):
        '''
        To get the size
        '''

        return self.__size

    @size.setter
    def size(self, value):
        '''
        To set the size
        '''

        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''
        Calculates and return the area of the square
        '''

        return self.__size**2
