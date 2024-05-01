#!/usr/bin/python3
""" Make change Module
"""


def makeChange(coins, total):
    """ Make change function
    Return:
        - Num of possible coins that can be summed up to meet
        'total'
    """
    if total <= 0:
        return 0
    if not coins:
        return -1
    sorted_coins = sorted(coins, reverse=True)

    coin_value = sorted_coins.pop(0)
    least_coins_num = 0
    meet_sum = 0
    control_count = 0

    while True:
        if coin_value > total:
            coin_value = sorted_coins.pop(0)
        if coin_value < total:
            if meet_sum < total:
                meet_sum += coin_value
            if meet_sum > total:
                meet_sum -= coin_value
                try:
                    coin_value = sorted_coins.pop(0)
                except IndexError:
                    return -1
                meet_sum += coin_value
                control_count += 1
            least_coins_num += 1
        if control_count >= 2:
            least_coins_num -= 1
        if meet_sum == total:
            break
        if coin_value == total:
            least_coins_num += 1
            return least_coins_num

    if not meet_sum == total:
        return -1

    return least_coins_num
