#!/usr/bin/python3
'''
Class Square that defines a square
'''


class Square:
    '''
    Square Class
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initializes a Square

        Size and position are private attributes
        because things depend of them and
        keep them privately is one of the ways to have the control of them.
        '''

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''
        To get the position
        '''

        return self.__position

    @position.setter
    def position(self, value):
        '''
        To set the position
        '''

        if ((type(value) is not tuple) or (len(value) != 2) or
                (type(value[0]) is not int) or
                (type(value[1]) is not int) or
                (value[0] < 0) or
                (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''
        Calculates and return the area of the square
        '''

        return self.__size**2

    def my_print(self):
        '''
        Prints in stdout the square with the character #
        '''

        if self.__size == 0:
            print()
        else:
            for row_spaces in range(self.__position[1]):
                print()
            for width in range(self.__size):
                for col_spaces in range(self.__position[0]):
                    print(" ", end="")
                for heigth in range(self.__size):
                    print("#", end="")
                print()
