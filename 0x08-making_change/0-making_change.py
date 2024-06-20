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
    if total < 0:
        return 0
    if total == 0:
        return 0      
    # Initialize an array to store the minimum coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make amount 0
    # Fill dp array
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    # If dp[total] is still float('inf'), it means it's not possible
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
