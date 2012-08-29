#!/usr/bin/python
#coding=utf-8

def sum_of_squares(number_list):
    '''return sum of number's square'''
    sum_of_squares = 0
    for number in number_list:
        sum_of_squares += pow(number, 2)
    return sum_of_squares

def squares_of_sum(number_list):
    '''return squares of sum of numbers'''
    sum_of_numbers = sum(number_list)
    result = pow(sum_of_numbers, 2)
    return result

if __name__ == '__main__':
    number_list = [i for i in xrange(1, 101)]
    print squares_of_sum(number_list) - sum_of_squares(number_list)
