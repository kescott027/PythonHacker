#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hgsums = []
    row = 0
    position = 0

    while row + 2 <= len(arr) - 1:
        column = 0
        while column + 2 <= len(arr[row]) - 1:
            top = arr[row][column] + arr[row][column + 1] + arr[row][column + 2]
            middle = arr[row + 1][column + 1]
            bottom = arr[row + 2][column] + arr[row + 2][column + 1] + arr[row + 2][column + 2]
            hgsums.append(top + middle + bottom)
            column += 1
            position += 1
        row += 1

    return max(hgsums)


if __name__ == '__main__':

    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]


   #  for _ in range(6):
   #     arr.append(list(map(int, input().rstrip().split())))

    expect = 19
    result = hourglassSum(arr)

    print("expect: {0}".format(expect))
    print("result: {0}".format(result))
