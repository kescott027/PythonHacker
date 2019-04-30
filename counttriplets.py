#!/bin/python3

import math
import os
import random
import re
import sys


def countTripletsStripped(arr, r):
    c = 0
    d1 = {}
    d2 = {}
    d3 = {}

    for i in arr:
        d3.setdefault(i, 0)
        d3[i] = arr.count(i)
    d2 = d3
    for j in arr:
        k = j*r
        l = j*r*r
        if k in d2.keys() and l in d3.keys():
            t = arr.count(j) * d2[k] * d3[l]
            d1[j] = t
            c = sum(d1.values())

    return c

# Complete the countTriplets function below.
def countTriplets(arr, r):
    c = 0
    d1 = {}
    d2 = {}
    d3 = {}
    print("array: {0}".format(arr))
    print("ratio: {0}".format(r))
    for i in arr:
        d3.setdefault(i, 0)
        d3[i] += 1
        d2.setdefault(i, 0)
        d2[i] += 1

    if r == 1:
        c = 0
        for m in d3:
            if d3[m] >= 3:
                # c += math.floor(d3[m] * 2)
                c = (1 + (d3[m] - 4)) ** 2 + 1
                # d3[m] * (anagrams[m] - 1) / 2
                # n * (n-2) = x
                # 5 * 3 = 18
                # 3 * 1 = 3

        return c

    for j in arr:
        print("j: {0}\tc: {1}".format(j, c))
        k = j*r
        l = j*r*r
        if k in d2.keys() and l in d3.keys():
            t = arr.count(j) * d2[k] * d3[l]
            print("found valid for j = {0}:".format(j))
            print("\t({0}, {1}, {2})".format(j, j*r, j*r*r))
            print("counts:\n\t {0}:{1} {2}:{3} {4}:{5} = + {6}".format(j, arr.count(j), k, d2[k], l, d2[l], t))
            print("t: {0} c previous: {1} total: {2}".format(t, c, t+c))
            d1[j] = t
            c = sum(d1.values())

    if r == 1:
        c = 0
        for m in d3:
            if d3[m] >= 3:
                c += math.floor(d3[m]/3)
    print("c final: {0}".format(c))
    return c


if __name__ == '__main__':
    input_list = [[1, 2, 1, 2, 4], [1, 2, 2, 4], [1, 3, 9, 9, 27, 81], [1, 5, 5, 25, 125], [1, 3, 9, 9, 9, 81],
                  [8, 8, 8, 8,8]]
    input_ratio = [2, 2, 3, 5, 1, 1]
    expect_list = [3, 2, 6, 4, 1, 10]

    bob = """8[0], 8[1], 8[2]

    8[0], 8[1], 8[2]
    8[0], 8[1], 8[3]
    8[0], 8[1], 8[4]
    
    8[0], 8[2], 8[3]
    8[0], 8[2], 8[4]
    8[0], 8[3], 8[4]

    8[1], 8[2], 8[3]
    8[1], 8[2], 8[4]
    8[1], 8[3], 8[4]

    8[2], 8[3], 8[4] """

    success = 0
    fail = 0
    i = 0

    while i < len(input_list):
        arr = input_list[i]
        r = input_ratio[i]
        expect = expect_list[i]
        # result = sherlockAndAnagrams(s)
        # result = noshit(s)
        print("\nTest Case: {0} ".format(i))
        result = countTripletsStripped(arr, r)
        result = countTriplets(arr, r)
        if result == expect:
            print("\nTest case {0} results - Success:\n\texpect: {1}\n".format(i, expect))
            print("\tresults: {0}".format(result))
            success += 1
        else:
            print("Test case {0} - Failure:\n\texpect: {1}".format(i, expect))
            print("\tresults: {0}".format(result))
            fail += 1
        i += 1
    print("Total Passing: {0}".format(success))
    print("Total Failures: {0}\n".format(fail))

    scratch = """
    1, 2, 1, 2, 4
    1[0], 2[1], 4[4] 
    1[0], 2[3], 4[4]
    1[2], 2[1], 4[4]
    1[2], 2[3], 4[4]    
    
    """