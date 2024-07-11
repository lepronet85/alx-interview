#!/usr/bin/python3
"""
Function to calculate the minimum number of operations required
to reduce a number to 1.
"""


def minOperations(n):
    """
    :param n:
    :return:
    """
    if n <= 1:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op
