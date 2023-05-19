#!/usr/bin/python3
"""Given a n x n 2D matrix, rotate it 90 degrees clockwise."""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0

    coin_used = 0
    current_total = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        n = (total-current_total)//coin
        coin_used += n
        current_total += n*coin
        if current_total == total:
            return coin_used
    return -1
