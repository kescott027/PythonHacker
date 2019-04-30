#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # a is array, d is len(a), rotation
    l = len(a)
    # a2 = [l-1]
    a2 = [0] * l
    r = d % l
    p = 0
    print("l: {0}\nr: {1}\np: {2}".format(l, r, p))
    print("a: {0}\na2: {1}".format(a, a2))
    while p < l:
        if p - r < 0:
            a2[l + (p-r)] = a[p]
        else:
            a2[p-r] = a[p]
        p +=1

    return a2

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()

    # n = int(nd[0])

    # d = int(nd[1])

    # a = list(map(int, input().rstrip().split()))

    d = 4
    a = [1,2,3,4,5]
    result = rotLeft(a, d)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    print(result)