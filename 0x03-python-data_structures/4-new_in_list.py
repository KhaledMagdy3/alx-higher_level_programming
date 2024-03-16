#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    coppied_list = my_list.copy()
    if (idx < 0):
        return coppied_list
    elif (idx > (len(my_list) - 1)):
        return coppied_list
    else:
        coppied_list[idx] = element
        return coppied_list
