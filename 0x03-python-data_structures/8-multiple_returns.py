#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x == 0:
        y = None
    else:
        y = sentence[0]
    return x, y
