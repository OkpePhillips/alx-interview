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


def isWinner(x, nums):
    """
    Functio to return the winner in the game depending on
    who won the most round
    """
    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        # Find the first prime number in the list
        for num in nums:
            if is_prime(num):
                nums = [n for n in nums if n % num != 0]
                break

        # Check if either player can make a move
        if not any(is_prime(num) for num in nums):
            # Ben wins if Maria cannot make a move
            ben_wins += 1
        else:
            # Maria wins if Ben cannot make a move
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
