#!/usr/bin/python3
"""
Module for prime game
"""


def isWinner(x, nums):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def playRound(n):
        primes = [i for i in range(2, n + 1) if isPrime(i)]
        if len(primes) % 2 == 0:
            return 'Ben'
        else:
            return 'Maria'

    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = playRound(n)
        wins[winner] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None
