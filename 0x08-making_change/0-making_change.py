#!/usr/bin/python3
"""
Making change challenge module
"""


def makeChange(coins, total):
    """
    Making change function to determine the fewest number of coins
    needed to make a total
    """
    if total <= 0:
        return 0

    fewest_coins = [float('inf')] * (total + 1)
    fewest_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            fewest_coins[i] = min(fewest_coins[i], fewest_coins[i - coin] + 1)
    return fewest_coins[total] if fewest_coins[total] != float('inf') else -1
