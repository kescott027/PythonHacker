#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.


def isBalanced(s):
    def _check(c0, c1):
        b = {"{": "}", "[": "]", "(": ")"}

        if c0 not in b.keys():
            return False
        if b[c0] == c1:
            return True
        else:
            return False

    q = []
    if (len(s) % 2) != 0:
        return "NO"
    else:
        for i in range(len(s)):
            q.append(s[i])

    while len(q) > 0:
        length = len(q)
        #check first
        if _check(q[0], q[1]):
            q = q[2::]
        #check last
        elif _check(q[-2], q[-1]):
            q = q[0:-2]
        #check inner
        elif _check(q[int(len(q)/2)-1], q[int(len(q)/2)]):
            q = q[0:int(len(q)/2)-1] + q[int(len(q)/2)+1::]
        #check outer
        elif _check(q[0], q[-1]):
            q = q[1:-1]
        else:
            if length <= len(q):
                return 'NO'

    return 'YES'



if __name__ == '__main__':

    inputs = ['{[()]}', '{[(])}', '{{[[(())]]}}', '{{([])}}', '{{)[](}}', '{(([])[])[]}', '{(([])[])[]]}',
              '{(([])[])[]}[]', '}][}}(}][))]', '[](){()}', '()', '({}([][]))[]()', '{)[](}]}]}))}(())(',
              '([[)']
    expected = ['YES', 'NO', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'NO', 'NO']

    case = range(0, len(inputs))

    failures = 0

    i = 0
    while i < len(inputs):

        print("Test Case {0} ({1})".format(case[i], i))
        expect = expected[i]

        result = isBalanced(inputs[i])

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
        print("{0} test case(s) failed.".format(failures))
    else:
        print("All cases Pass successfully")