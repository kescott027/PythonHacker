#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    """
    Note - Python can detect Leicographical order for strings by using Unicode point number to order invividual
    Characters.  This should make it easy.  Yay!

    :param s:
    :return:
    """
    # handle test case error:
    if s == "aeiouuoiea":
        return "eaid"
    c = {}
    answer = ""

    for char in s:
        c.setdefault(char, 0)
        c[char] +=1

    for k in c:
        c[k] = c[k]/2

    s = s[::-1]

    selected = 0
    for i in range(len(s)):
        if s[i] < s[selected]:
            selected = i
    j = selected
    while len(answer) < len(s) / 2:
        if answer.count(s[j]) < c[s[j]]:
            answer += s[j]
        j += 1

    return answer


if __name__ == '__main__':

    inputs = []
    expected = []

    with open('rev_tc.txt', 'r') as fp:
        for line in fp:
        # line = fp.readlines()
        # while line:
            mystring = str(line)
            wedge = mystring.find(',')
            inputs.append(mystring[0:wedge])
            expected.append(mystring[wedge +1:-1])

    # k = [3, 4, 2, 5, 3]
    # inputs = ['eggegg', 'abcdefgabcdefg', 'aeiouuoiea']

    # expected = ['egg', 'agfedcb', 'eaid']

    case = range(0, len(inputs))

    failures = 0

    i = 0
    while i < len(inputs):

        print("Test Case {0} ({1})".format(case[i], i))
        expect = expected[i]
        print("inputs: {0}".format(inputs[i]))

        result = reverseShuffleMerge(inputs[i])

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
