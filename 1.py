#!/usr/bin/python
#coding=utf-8

def answer(start, end, *multiples):
    '''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    '''
    #multiples里的数字互质
    sum = 0
    for i in xrange(start, end):
        for multiple in multiples:
            if i % multiple == 0:
                sum += i
                break
    return sum

if __name__ == '__main__':
    print answer(1, 1000, 3, 5)
