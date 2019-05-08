#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    """
    given a list of integers arr, and a single integer k, create an array of length k from elements arr such
    as its unfairness is minimized.  Call that array subarr.  unfairness of an array is calculated as:
      max(subarr) - min(subarr)
    :param k: an integer - the number of elements in the array to create
    :param arr: a list of integers
    :return:
    """
    debug = False
    newarr = []
    c = {}

    arr = sorted(arr)
    if debug:
        print("array size: {0}".format(k))
        print("starting array {0}".format(arr))

    i=0
    while i + k <= len(arr):
        c[arr[i+(k - 1)] - arr[i]] = i
        i+=1
    print("ranges: {0}".format(c))
    start_index = c[min(c.keys())]

    if debug:
        print("min key: {0}".format(min(c.keys())))
        print("starting index: {0}".format(start_index))

    newarr = arr[start_index:start_index+k]
    final = max(newarr) - min(newarr)

    if debug:
        print("sorted array {0}".format(arr))
        print("final array {0}".format(newarr))
        print("min {0}".format(min(newarr)))
        print("max {0}".format(max(newarr)))
        print("result = {0} ".format(final))

    return final


if __name__ == '__main__':
    k = [3, 4, 2, 5, 3]
    inputs = [[10, 100, 300, 200, 1000, 20, 30], [1, 2, 3, 4, 10, 20, 30, 40, 100, 200], [1, 2, 1, 2, 1],
              [4504, 1520, 5857, 4094, 4157, 3902, 822, 6643, 2422, 7288, 8245, 9948, 2822, 1784, 7802, 3142, 9739,
              5629, 5413, 7232], [100, 200, 300, 350, 400, 401, 402]]

    expected = [20, 3, 0, 1335, 2]

    case = range(0, len(inputs))

    failures = 0

    i = 0
    while i < len(inputs):

        print("Test Case {0} ({1})".format(case[i], i))
        expect = expected[i]
        print("inputs: {0}\nk: {1}".format(inputs[i], k[i]))
        result = maxMin(k[i], inputs[i])

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