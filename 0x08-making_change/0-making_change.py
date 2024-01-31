#!/usr/bin/python3
"""
Module for making change with fewest number of coins
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin values.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
              If total is 0 or less, return 0.
              If total cannot be met by any number of coins, return -1.
    """
    if total < 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

# Example usage
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
