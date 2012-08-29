#!/usr/bin/python
#coding=utf-8

from math import sqrt

def smallest_factor(number):
    """return smallest factor of a number"""
    for i in xrange(2, int(sqrt(number)+1)):
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
    return prime_factors

def least_common_multiple(*numbers):
    '''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
       What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
    least_common_multiple = 1
    factors = {}
    for number in numbers:
        factors.setdefault(number, 0)
        tmp = {}
        for factor in prime_factors(number):
            tmp.setdefault(factor, 0)
            tmp[factor] += 1

        for factor,times in tmp.iteritems():
            if factors[factor] < tmp[factor]:
                factors[factor] = tmp[factor]
    for number, times in factors.iteritems():
        least_common_multiple = least_common_multiple * pow(number, times)
    return least_common_multiple

if __name__ == '__main__':
    print least_common_multiple(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
