#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    """

    :param string s: string of letters and characters
    :param int n: position of end of substring
    :return: occurances of letter 'a' in first n characters.
    """
    count = 0
    newstring = ""
    while len(newstring) < n:
        tempstring = newstring + s
        newstring = tempstring

    substring = newstring[0:n]
    for char in substring:
        if char == 'a':
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()