#!/usr/bin/python3
"""
Dynamic Programming Solution to Make Change with the Fewest Coins
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to make a given total using dynamic programming.

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

    # Initialize dp array with a large number (representing infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  

    /* Build up the dp table */
    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
