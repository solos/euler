#!/usr/bin/python
#coding=utf-8

from math import sqrt

def smallest_factor(number):
    """return smallest factor of a number"""
    for i in xrange(2, int(sqrt(number))):
        if number % i == 0:
            return i
    return False

def prime_factors(number):
    """return prime factors of a number"""
    prime_factors = []
    while ( smallest_factor(number) ):
        smallest = smallest_factor(number)
        prime_factors.append(smallest)
        number /= smallest
    prime_factors.append(number)
    #return prime_factors
    return number

if __name__ == '__main__':
    print prime_factors(600851475143)
