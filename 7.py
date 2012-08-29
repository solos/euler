#!/usr/bin/python
#coding=utf-8

from math import sqrt

def is_prime(number):
    '''return whether a number is a prime number'''
    for i in xrange(2, int(sqrt(number))+1):
        if not number % i:
            return False
    return True

def prime_number(n):
    '''return the nth prime number'''
    count = 1
    number = 2
    while (count < n):
        number += 1
        if  is_prime(number):
            count += 1
    return number

if __name__ == '__main__':
    print prime_number(10001)
