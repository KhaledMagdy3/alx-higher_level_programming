#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None

    roman_dic = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
    result = 0
    prv_value = 0

    for i in roman_string[::-1]:
        value = roman_dic[i]
        if value < prv_value:
            result -= value
        else:
            result += value
        prv_value = value

    return result
