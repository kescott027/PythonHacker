#!/bin/python3

import math
import os
import random
import re
import sys


def luckBalance(k, contests):
    """
    return an integer that represents the maximum luck balance achievable.
    :param k: the number of important contests that can be lost
    :param contests: a 2D array of integers where each contest[i] contains two integers that represent the luck balance
            and importance of the ith contest
    :return: int that represents the maximum luck balance achievable.
    """
    lost = 0
    luck = 0

    prioritized = sorted(contests, key=lambda x: (x[1], x[0]), reverse=True)

    while len(prioritized) >= 1:
        c = prioritized.pop(0)
        if lost < k or c[1] == 0:
            luck += c[0]
            lost += c[1]
        else:
            luck -= c[0]

    return luck


# Complete the luckBalance function below.
def luckBalance2(k, contests):
    """
    return an integer that represents the maximum luck balance achievable.
    :param k: the number of important contests that can be lost
    :param contests: a 2D array of integers where each contest[i] contains two integers that represent the luck balance
            and importance of the ith contest
    :return: int that represents the maximum luck balance achievable.
    """
    # length = k[0]
    loss_limit = k
    lost = 0
    # important = []
    luck = 0
    print("loss limit: {0}".format(loss_limit))
    print(sorted(contests, key=lambda x: (x[1], x[0]), reverse=True))

    prioritized = sorted(contests, key=lambda x: (x[1], x[0]), reverse=True)

    while len(prioritized) >= 1:
        c = prioritized.pop(0)
        print(c)
        if lost < loss_limit or c[1] == 0:
            luck += c[0]
            lost += c[1]
            print("luck + {0} = {1}".format(c[0], luck))
            print("lost + {0} = {1}".format(c[1], lost))
        else:
            luck -= c[0]
            print("luck - {0} = {1}".format(c[0], luck))
        print("luck: {0}".format(luck))

    return luck


if __name__ == '__main__':
    k = [3, 5, 2]
    inputs = [[[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]],
              [[13, 1], [10, 1], [9, 1], [8, 1], [13, 1], [12, 1], [18, 1], [13, 1]],
              [[5,1], [4, 0], [6, 1], [2, 1], [8,0]]]
    expected = [29, 42, 21]

    case = range(0, len(inputs))

    failures = 0

    i = 0
    while i < len(inputs):

        print("Test Case {0} ({1})".format(case[i], i))
        expect = expected[i]

        result = luckBalance(k[i], inputs[i])

        if result != expect:
            print("Test Case {0}: FAIL\n\tinput:{1}\n\touput: {2}\n\texpected: {3}".format(case[i], inputs[i], result,
                                                                                           expect))
            failures += 1
        else:
            print("Test Case {0}: PASS\n\tinput: {1}\n\toutput: {2}".format(i, inputs[i], result))
            # pass
        print(" ")
        i += 1

    if failures > 0:
        print("Test cases failed.")
    else:
        print("All cases Pass successfully")