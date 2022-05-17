#!/usr/bin/python3
'''
Class Square that defines a square
'''


class Square:
    '''
    Square Class
    '''

    def __init__(self, size):
        '''
        Initializes a Square

        Size is private attribute because the size of a square is crucial
        for a square, many things depend of it (area computation, etc.) and
        keep it privately is one of the ways to have the control of size.
        '''

        self.__size = size
