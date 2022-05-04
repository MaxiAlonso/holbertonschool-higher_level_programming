#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) != 0:
        numerator = 0
        denominator = 0
        for pair in (my_list):
            numerator += pair[0] * pair[1]
            denominator += pair[1]
        return numerator / denominator
    return 0
