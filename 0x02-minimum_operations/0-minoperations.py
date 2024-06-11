#!/usr/bin/python3

"""
function to calculate the fewest number of operations needed to result in exact characters in a file using copy all and paste only
"""


def minOperations(n):
    """
    Calculate the minimum number of copy and paste operations required to generate
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
