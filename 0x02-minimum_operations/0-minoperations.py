#!/usr/bin/python3
"""
Task 0: Minimum Operations
""" 


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    """
    n_ops = 0
    number = n
    i = 2
    while i <= number:
        while number % i == 0:
            number = number / 2
            n_ops = n_ops + i
        i += 1
    return n_ops
