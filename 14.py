#!/usr/bin/python
#coding=utf-8

def sequence(number):
    sequence = []
    count = 0
    while ( number != 1 ):
        #sequence.append(number)
        count += 1
        number = (3 * number + 1, number / 2)[ number % 2 == 0]
    #sequence.append(1)
    count += 1
    return count

if __name__ == '__main__':
    max_length = 0
    starting_number = 1
    number = 2
    while ( number < 1000000):
        seq = sequence(number)
        if seq > max_length:
            starting_number = number
            max_length = seq
        number += 1
    print starting_number
