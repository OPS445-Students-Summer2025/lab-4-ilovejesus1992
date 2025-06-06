#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(str_: str):
    # Place code here - refer to function specifics in section below
    first_5 = str_[0:5]
    return first_5

def last_seven(str_: str):
    # Place code here - refer to function specifics in section below
    last_7 = str_[-7:]
    return last_7

def middle_number(num):
    # Place code here - refer to function specifics in section below
    mid_num = str(num)
    mid_num = mid_num[1:3]
    return mid_num

def first_three_last_three(text1: str, text2: str):
    # Place code here - refer to function specifics in section below
    first_last_three = text1[:3] + text2[-3:]
    return first_last_three


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))