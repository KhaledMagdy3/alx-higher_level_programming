#!/usr/bin/python3
def weight_average(my_list=[]):
    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total score += score * weight
        total weight += weight

    return total_score / total_weight
