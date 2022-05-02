#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        maxnum = None
    else:
        maxnum = my_list[0]
        for num in my_list:
            if num > maxnum:
                maxnum = num
    return(maxnum)
