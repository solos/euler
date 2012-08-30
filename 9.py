#!/usr/bin/python
#coding=utf-8

def pythagorean_triplet(sum):
    '''Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.'''
    for c in xrange(1, sum):
        for b in xrange(1, c):
            a = sum - c - b
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                return a * b * c

if __name__ == '__main__':
    print pythagorean_triplet(1000)
