#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sor_dic = sorted(a_dictionary)
    for value in sor_dic:
        print(f"{value}: {a_dictionary[value]}")
