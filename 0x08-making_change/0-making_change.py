#!/usr/bin/python3
"""
Task 0: Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values
    determine the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if coin > total:
            continue
        count = total // coin
        total -= count * coin
        coin_count += count
        if total == 0:
            break
    if total > 0:
        return -1
    return coin_count
