#!/usr/bin/python3
"""
Prime game Module
"""


def sieve_of_eratosthenes(limit):
    """
    Function that uses the concept of sieve of
    Eratothenes to return prime numbers within a range
    """
    primes = []
    # initially set all numbers as prime
    is_prime = [True] * (limit + 1)

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            # Mark multiples of num as non-prime
            for multiple in range(num*num, limit+1, num):
                is_prime[multiple] = False

    # Add remaining primes to the list
    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes


def isWinner(x, nums):
    """
    Function to determine the winner of the game based on the number
    of prime numbers in the list of numbers.
    """
    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        if len(primes) % 2 == 0:
            winners["Ben"] += 1
        else:
            winners["Maria"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return None
