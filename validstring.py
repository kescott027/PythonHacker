#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    """
    test if a string is valid, with the following definition:
       All characters of the string appear the same number of times.
       Also valid if you can remove just 1 character at 1 index in the string and the remaining
       characters will occur the sname number of times.

    :param s: a string where 1<= |s| <= 10 ** 5

    :return: Print "YES" if a string is valid, otherwise, print "NO".
    for local testing concerns, return "YES" or "NO" as appropriate.
    """
    counts = {}
    frequencies = {}
    normal = []
    abnormal = []

    if len(s) <= 3:
        print("YES")
        return "YES"

    for i in range(0, len(s)):
        counts.setdefault(s[i], 0)
        counts[s[i]] += 1
    print("counts: {0}".format(counts))

    for j in counts:
        frequencies.setdefault(counts[j], 0)
        frequencies[counts[j]] += 1
    print("frequencies: {0}".format(frequencies))

    for k in frequencies:
        if frequencies[k] == max(frequencies.values()):
            normal.append(frequencies)
        else:
            abnormal.append(frequencies)

    print("max freq/value: {0}".format(max(frequencies.values())))
    print("normal: {0}".format(normal))
    print("abnormal: {0}".format(abnormal))
    print("length normal: {0}".format(len(normal)))
    print("length abnormal: {0}".format(len(abnormal)))

    if len(abnormal) == 0:
        print("YES")
        return "YES"

    if len(normal) > 1 or len(abnormal) > 1:
        print("NO")
        return "NO"
    else:
        base = normal[0]
        unbase = 0

    for l in counts:
        if counts[l] != base:
            unbase +=1

    if unbase <= 1 or abs(base - unbase) == 1:
        print("YES")
        return "YES"

    bob = """
    if len(frequencies) == 1:
        print("YES")
        return "YES"
    elif len(frequencies) > 2 or max(frequencies.values()) == min(frequencies.values()):
        print("NO")
        return "NO"
    elif min(frequencies.values()) > 1:
        print("NO")
        return "NO"
    elif abs(max(frequencies) - min(frequencies)) != 1 and min(frequencies) * min(frequencies.values()) != 1:
        print("NO")
        return "NO"
    else:
        print("YES")
        return "YES"
                   """
    # print("max freq: {0}".format(max(frequencies)))
    # print("max freq val: {0}".format(max(frequencies.values())))
    # print("min freq: {0}".format(min(frequencies)))
    # print("min freq val: {0}".format(min(frequencies.values())))

    print("NO")
    return "NO"

if __name__ == '__main__':

    inputs = ["aabbcd", "aabbccddeefghi", "abcdefghhgfedecba", "aaaabbcc", "xxxaabbccrry", "aaaaabc",
              "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"]
    expected = ["NO", "NO", "YES", "NO", "NO", "NO", "YES"]

    case = range(0, len(inputs))

    failures = 0

    i = 0
    while i < len(inputs):

        print("Test Case {0} ({1})".format(case[i], i))
        expect = expected[i]
        result = isValid(inputs[i])

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