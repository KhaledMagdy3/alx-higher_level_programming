#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_uniq = set()
    sum = 0
    for i in my_list:
        if i not in set_uniq:
            set_uniq.add(i)
            sum = sum + i

    return sum
