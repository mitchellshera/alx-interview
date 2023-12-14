#!/usr/bin/python3
'''minoperations module'''


def minOperations(n):
    """minoperations to get n amount of H """


    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
