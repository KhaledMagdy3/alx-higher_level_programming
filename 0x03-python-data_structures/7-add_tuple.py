#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = len(tuple_a)
    y = len(tuple_b)

    if x == 0:
        tuple_a = (0, 0)
    elif x < 2:
        tuple_a += (0, 0)

    if y == 0:
        tuple_b = (0, 0)
    elif y < 2:
        tuple_b += (0, 0)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
