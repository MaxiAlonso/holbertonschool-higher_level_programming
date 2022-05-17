#!/usr/bin/python3
'''
Magic Class Definition
'''

import math


class MagicClass:
    '''
    MagicClass
    '''

    def __init__(self, radius=0):
        '''
        Initializes a MagicClass
        '''

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        '''
        Calculates the area of the MagicClass
        '''

        return self.__radius**2*math.pi

    def circumference(self):
        '''
        Calculates the circumference of the MagicClass
        '''
        return 2*math.pi*self.__radius
