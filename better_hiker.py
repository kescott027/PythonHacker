#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    """
    n number of steps.
    s string describing path n characters describing path.
      path contains characters U and D for [Up] and [Down]
      respectively
      2<=n<=10**6
    """

    elevation = 0
    valleys = 0

    for char in s:
        if char == 'U':
            elevation +=1
        elif char == 'D':
            if elevation == 0:
                valleys += 1
            elevation -= 1

    return valleys


if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = "DDDUUUDDUUDDUUUDDUUUDDUDDDDDDDUUUUUU"
    # expected = 5

    s = "UDDDUDUU"
    expected = 1
    n = len(s) - 1

    result = countingValleys(n, s)

    if result == expected:
        print("Success")

    else:
        print("Failure")

    print("results: {0}\nexpected:{1}".format(result, expected))

    # fptr.write(str(result) + '\n')

    # fptr.close()


