#!/usr/bin/python3
"""
returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return list()
    else:
        arr = [[1]]
        for i in range(1, n):
            subarr = []
            prev = len(arr[i - 1])
            curr = prev + 1
            for x in range(0, curr):
                if x == 0:
                    subarr.append(1)
                elif x == prev:
                    subarr.append(1)
                else:
                    subarr.append(arr[i - 1][x - 1] + arr[i - 1][x])
            arr.append(subarr)
        return arr
