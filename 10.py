#!/usr/bin/python
#coding=utf-8

from math import sqrt

def is_prime(number):
    '''return whether a number is a prime number'''
    for i in xrange(2, int(sqrt(number))+1):
        if not number % i:
            return False
    return True

def primes_sum(max):
    """return the sum of all the primes below max"""
    primes_sum = 2
    for i in xrange(3, max, 2):
        primes_sum += (0, i)[is_prime(i)]
    return primes_sum

if __name__ == '__main__':
    print primes_sum(2000000)
