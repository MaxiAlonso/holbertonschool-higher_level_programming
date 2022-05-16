#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for count in range(x):
        try:
            print(f"{my_list[count]}", end="")
        except IndexError:
            count -= 1
            break
    print()
    return count + 1
