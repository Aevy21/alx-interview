#!/usr/bin/python3

"""
func to calc the fewest number of operations needed to result in \
        n  chars  in a file using copy all and paste.
"""


def minOperations(n):
    """
    Calculate the min number of copy and paste operations required to generate
    exactly n 'h' characters using the fewest operations.

    Parameters:
    n (int): The target number of 'h' characters.

    Returns:
    int: The minimum number of operations required.
    """
    if n == 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
