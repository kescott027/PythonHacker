#!/bin/python3

import math
import os
import random
import re
import sys


def minimumBribesK2(q):
    """
    This is the most efficient version which psses performance testing.
    :param q:
    :return:
    """
    c = 0

    q = [p - 1 for p in q]

    for i, p in enumerate(q):
        if p - i > 2:
            print('Too chaotic')
            return 'Too chaotic'

        for j in range(max(p-1, 0), i):
            if q[j] > p:
                c += 1

    print(c)
    return c


def minimumBribesK(q):
    c = 0
    start = sorted(q)

    for i in range(len(q)):
        change = 0
        position = i + 1
        change = q[i] - position
        print("i: {0} q[i]: {1} position: {2} change {3}".format(i, q[i], position, change))

        if change > 2:
            print('Too chaotic')
            return 'Too chaotic'
        if q[i] > position:
            c += change
        if change < -2:
            c += 1

    print(c)
    return c


# Complete the minimumBribes function below.
def minimumBribes(q):
    """
    This version of position change reporting works, but does not perform to 10 x 1,000,000 checks in under 10 seconds
    timeout value.  The time spent actually sorting slows down the algorithm to the point where the performance
    timeout is reached

    :param q: numeric list of length n > 5 < 10
    prints response to stdout
    :return: none
    """
    c = 0
    i = 0
    b = sorted(q)
    print("current line: {0}".format(q))
    for i in range(len(q)):
        change = 0
        position = i + 1
        print("i = {0}\t Position = {1}\t origin rank = {2}".format(i, position, q[i]))
        if position < q[i] + 1:
            change = q[i] - position
            b.insert(i, b.pop(i + change))
            print("\tchange = {0} - {1} = {2}".format(q[i], position, change))
        elif b[i] > q[i]:
            change = i - b.index(q[i])
            print("caught change at position {0} with value {1} vs {2}".format(i, b[i], q[i]))
            print("calculating change at: {0}".format(change))
            # print("\tno change at position {0}".format(position))

        if change > 2:
            print("Too chaotic")
            return 'Too chaotic'
        else:
            c += change

        i += 1

    print("result = {0}".format(int(c)))
    return int(c)


if __name__ == '__main__':

    inputs = [[2, 1, 5, 3, 4], [2, 5, 1, 3, 4], [5, 1, 2, 3, 7, 8, 6, 4], [1, 2, 5, 3, 7, 8, 6, 4],
              [1, 2, 5, 3, 4, 7, 8, 6]]
    expected = [3, 'Too chaotic', 'Too chaotic', 7, 4]

    case = [0, 0, 1, 1, 2]

    failures = 0

    i = 0
    while i < len(inputs):
        print("Test Case {0} ({1})".format(case[i], i))
        expect = expected[i]
        result = minimumBribesK2(inputs[i])

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