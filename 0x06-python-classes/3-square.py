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

        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''
        Calculates and return the area of the square
        '''
        return self.__size**2
