#!/usr/bin/python3
""" Make change Module
"""


def sum_iterator(coin_value, total, iter_value=None):
    """ Sums up possibilities
    Return:
        - sum of possibles coins
    """
    if coin_value < total:
        if iter_value:
            new_sum = coin_value + iter_value
        else:
            new_sum = coin_value + coin_value
        if new_sum > total:
            if iter_value:
                new_sum = new_sum - iter_value
            else:
                return new_sum - coin_value

    return new_sum


def makeChange(coins, total):
    """ Make change function
    Return:
        - Num of possible coins that can be summed up to meet
        'total'
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)

    sum_to_meet = sorted_coins.pop(0)
    least_coins_num = 1
    new_iter_value = None
    while sum_to_meet < total:
        iter_sum = sum_iterator(sum_to_meet, total, new_iter_value)
        if sum_to_meet == iter_sum:
            try:
                new_iter_value = sorted_coins.pop(0)
            except IndexError:
                return -1
            iter_sum = sum_iterator(sum_to_meet, total, new_iter_value)
            sum_to_meet = iter_sum
        else:
            iter_sum = sum_iterator(sum_to_meet, total, new_iter_value)
            sum_to_meet = iter_sum

        least_coins_num += 1
