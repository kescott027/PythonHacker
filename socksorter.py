#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sorted = {}
    pairs = []
    for value in ar:
        if value in sorted:
            sorted[value] += 1
        else:
            sorted[value] = 1

    #pair
    for color in sorted:
        pairs.append(int(sorted[color]/2))

    #count pairs
    return sum(pairs)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    list1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    list2 = [10, 10, 30, 10, 50, 40, 30, 30, 20, 10, 20, 40]
    list3 = [10, 20, 30, 40, 50]
    list4 = [20, 30, 20, 30, 10, 40, 20, 30, 50]
    list5 = [10, 10, 10, 10, 10, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40, 50]
    list6 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    arlist = [list1, list2, list3, list4, list5, list6]
    answers = [3, 5, 0, 2, 6, 8]
    i = 0

    for value in arlist:
        ar = value
        n = len(value)
        expected = answers[i]
        result = sockMerchant(n, ar)
        print("result: {0}  expected: {1}".format(result, expected))
        i += 1

    # fptr.write(str(result) + '\n')

    # fptr.close()