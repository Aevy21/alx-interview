#!/usr/bin/python3
"""
Dynamic Programming Solution to Make Change with the Fewest Coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to make a given total .

    Args:
    - coins (list of int): The values of the coins available.
    - total (int): The total amount to make with the coins.

    Returns:
    - int: The fewest number of coins needed to meet the total.
      Returns 0 if the total is 0 or less.
      Returns -1 if the total cannot be met with the given coins.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    return count if total == 0 else -1
