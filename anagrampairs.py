#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def noshit(s):
    from collections import Counter
    count = 0
    for i in range(1, len(s) + 1):
        a = ["".join(sorted(s[j:j + i])) for j in range(len(s) - i + 1)]
        b = Counter(a)
        for j in b:
            count += b[j] * (b[j] - 1) / 2
    return int(count)


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    anagrams = {}

    # create all possible substrings
    for i in range(1, len(s) + 1):
        substrings = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        anagrams = Counter(substrings)
        print("substrings:\n {0}".format(substrings))
        print("anagrams: \n{0}".format(anagrams))
        # check each substring for anagrams
        for j in anagrams:
            new_anagrams = anagrams[j] * (anagrams[j] - 1) / 2
            print("j = {0} x {1}".format(j, anagrams[j]))
            print("anagrams found: {0}".format(new_anagrams))
            count += int(new_anagrams)

    print(anagrams)
    return math.floor(count)


if __name__ == '__main__':

    input_list = ['abba', 'abcd', 'ifailuhkqq', 'kkkk', 'cdcd']
    expect_list = [4, 0, 3, 10, 5]

    success = 0
    fail = 0
    i = 0

    while i < len(input_list):
        s = input_list[i]
        expect = expect_list[i]
        # result = sherlockAndAnagrams(s)
        # result = noshit(s)
        print("Test Case: {0} ".format(i))
        result = kylesAnagrams(s)
        if result == expect:
            print("\nTest case {0} results - Success:\n\texpect: {1}\n".format(i, expect))
            print("\tresults: {0}".format(result))
            success +=1
        else:
            print("Test case {0} - Failure:\n\texpect: {1}".format(i, expect))
            print("\tresults: {0}\n".format(result))
            fail += 1
        i += 1
    print("\n Total Passing: {0}".format(success))
    print("\n Total Failures: {0}".format(fail))
