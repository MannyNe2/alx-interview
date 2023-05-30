#!/usr/bin/python3
"""The Prime Number Game"""


def isWinner(x, nums):
    """Module that calculates the prime game (Algorithm)"""
    if not nums or x < 1:
        return None
    num = max(nums)
    tcase = [True for _ in range(max(num + 1, 2))]
    for i in range(2, int(pow(num, 0.5)) + 1):
        if not tcase[i]:
            continue
        for j in range(i * i, num + 1, i):
            tcase[j] = False
    tcase[0] = tcase[1] = False
    c = 0
    for i in range(len(tcase)):
        if tcase[i]:
            c += 1
        tcase[i] = c
    player1 = 0
    for num in nums:
        player1 += tcase[num] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
