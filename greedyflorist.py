#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.


def getMinimumCost(k, c):
    """
    calculate the maximization of money that can be charged given a group of customers purchasing items where
    the price of each unit is multiplied by the number of that customer's previously purchased units plus one.
    i.e. purchase 1 = (0 + 1) x original price.
         purchase 2 = (1 + 1) x original price. etc.
    constraints:
        where n is the number of flowers purchased, k is the number of friends, and c is the array of original prices

        1<= n, k <= 100
        1 <= c[i] <= 10 ** 6
        answer < 2 ** 31
        0 <= i < n

    :param k: an integer equal to the number of friends
    :param c: an array of integers representing the original price per flower
    :return: an integer indicating the minimum cost to purchase all of the flowers
    """
    debug = False
    cost = 0
    c = sorted(c)
    # f = [0] * k

    if debug:
        print("c: {0}".format(c))
        print("friends: {0} flowers: {1}".format(k, len(c)))

    if debug:
        print("f: {0}".format(f))

    j = 0
    while len(c) > 0:
        for i in range(k):
            if len(c) > 0:
                h = c.pop()
                i_cost = (j + 1) * h
                cost += i_cost
                if debug:
                    print("friend: {0} purchase: {1} origin cost: {2} multiplier: {3}".format(i, j+1, h, j + 1))
                    print("current transaction: [{0}] total cost [{1}] ".format(i_cost, cost))
        j += 1

    return cost


if __name__ == '__main__':

    k = [3, 2, 3, 3]
    inputs = [[2, 5, 6], [2, 5, 6], [1, 3, 5, 7, 9],
              [390225,  426456, 688267, 800389, 990107, 439248,240638, 15991, 874479, 568754, 729927, 980985, 132244,
               488186, 5037, 721765, 251885, 28458, 23710, 281490, 30935, 897665, 768945, 337228, 533277, 959855,
               927447, 941485, 24242, 684459, 312855, 716170, 512600, 608266, 779912, 950103, 211756, 665028, 642996,
               262173, 789020, 932421, 390745, 433434, 350262, 463568, 668809, 305781, 815771, 550800]]

    expected = [13, 15, 29, 163578911]

    case = range(0, len(inputs))

    failures = 0

    i = 0
    while i < len(inputs):

        print("Test Case {0} ({1})".format(case[i], i))
        expect = expected[i]

        result = getMinimumCost(k[i], inputs[i])

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