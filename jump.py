#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    jumps = 0
    position = 0
    last_cloud = len(c) - 1

    while position != last_cloud:
        if position + 2 <= last_cloud and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        jumps += 1
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
