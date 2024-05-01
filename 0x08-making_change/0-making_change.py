#!/usr/bin/python3
""" Make change Module
"""


def sum_iterator(coin_value, total, iter_value=None):
    """ Sums up possibilities
    Return:
        - sum of possibles coins
    """
    if coin_value < total:
        new_sum = coin_value + iter_value
        if new_sum > total:
            new_sum = new_sum - iter_value

    return new_sum


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

    sum_to_meet = sorted_coins.pop(0)
    least_coins_num = 1
    meet_sum = sum_to_meet

    while meet_sum < total:
        meet_sum = meet_sum + sum_to_meet
        if meet_sum > total:
            meet_sum = meet_sum - sum_to_meet
            try:
                sum_to_meet = sorted_coins.pop(0)
            except IndexError:
                return -1
            meet_sum = sum_iterator(meet_sum, total, sum_to_meet)

        least_coins_num += 1
    if not meet_sum == total:
        return -1

    return least_coins_num
