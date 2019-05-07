#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    origin = sorted(arr)
    output = []

    for i in range(len(origin) -1 ):
        output.append(abs(origin[i] - origin[i+1]))

    # print(output)
    return min(output)

if __name__ == '__main__':

    inputs = [[3, -7, 0], [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75], [1, -3, 71, 68, 17]]
    expected = [3, 1, 3]

    case = range(0, len(inputs))

    failures = 0

    i = 0
    while i < len(inputs):

        print("Test Case {0} ({1})".format(case[i], i))
        expect = expected[i]

        result = minimumAbsoluteDifference(inputs[i])

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