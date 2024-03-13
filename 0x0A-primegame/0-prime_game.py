#!/usr/bin/python3
"""
Prime numbers game module
"""


def is_prime(num):
    """ Checks if a number is a prime number """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def next_prime(start):
    """ Returns the next prime number from the current number """
    while True:
        if is_prime(start):
            return start
        start += 1


def optimal_winner(n):
    """
    Returns the winner based on the n
    """
    current = 2
    while n > 1:
        current = next_prime(current)
        if n % current == 0:
            return "Ben"
        n //= current
    return "Maria"


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = optimal_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
