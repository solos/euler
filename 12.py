#!/usr/bin/python
#coding=utf-8
from math import sqrt

def triangle(n):
    triangle = n * (n + 1) / 2
    return triangle

def factors(number):
    count = 0
    if number == 1:
        return 1
    factors = set()
    for i in xrange(1, int(sqrt(number))+1):
        if number % i == 0:
            count += 1
            factors.add(i)
    count *= 2
    return count

if __name__ == '__main__':
    number = 1
    while ( factors(triangle(number)) <= 500 ):
        number += 1
    print triangle(number)
