#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    c = 0
    newstring = s
    i = 0
    while i+1 < len(newstring):
        print("pass {0} string: {1} deletions: {2}".format(i, newstring, c))
        tempstring = ''
        if newstring[i] == newstring[i + 1]:
            tempstring = newstring[0:i] + newstring[i+1:]
            newstring = tempstring
            print("modified: {0}".format(newstring))
            c += 1
        else:
            i += 1
    return c

if __name__ == '__main__':

    inputs = ["AAAA", "BBBBB", "ABABABAB", "BABABA", "AAABBB", "AAABBBAABB", "AABBAABB", "ABABABAA", "ABBABBAA"]
    expected = [3, 4, 0, 0, 4, 6, 4, 1, 3]

    case = range(0, 9)

    failures = 0

    i = 0
    while i < len(inputs):

        print("Test Case {0} ({1})".format(case[i], i))
        expect = expected[i]
        result = alternatingCharacters(inputs[i])

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


