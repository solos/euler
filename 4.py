#!/usr/bin/python
#coding=utf-8

def is_palindromic(number):
    """return whether a number is palindromic"""
    str_num = str(number)
    length = len(str_num)
    if length % 2 == 0:
        for i in xrange(0, length / 2 + 1):
            if str_num[i] != str_num[ length -1 - i ]:
                return False
        return True
    return False

def largest_pal(n):
    """return largest palindromic made from the product of two n-digest number"""
    max = pow(10, n) - 1
    largest_pal = 0
    for i in xrange(max, 1, -1):
        for j in xrange(max, 1, -1):
            result = i * j
            if is_palindromic( result ):
                largest_pal = ( result, largest_pal) [ largest_pal > result ]
    return largest_pal

if __name__ == '__main__':
    print largest_pal(3)
