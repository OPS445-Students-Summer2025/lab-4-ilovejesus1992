#!/usr/bin/env python3
# Author ID: 166335232

def is_digits(sobj):
    # place code here - loop through each character in sobj 
    length = len(sobj)
    offset = 0
    checknum = False
    for isnum_ in sobj:
        if isnum_ not in '0123456789':
            checknum = False
            break
        checknum = True
    return checknum

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')