#!/bin/python3

import math
import os
import random
import re
import sys

def checkMagazine(magazine, note):
    d = {}
    result = 'Yes'
    for word in magazine:
        d.setdefault(word, 0)
        d[word] +=1

    for word in note:
        if word in d and d[word] -1 >= 0:
            d[word] -=1
        else:
            result = 'No'

    print(result)

stillnotefficient = """
def checkMagazine(magazine, note):

    d = {}
    result = 'Yes'
    for word in magazine:
        d.setdefault(word, 0)
        d[word] +=1

    for word in note:
        if word in d and d[word] -1 >= 0:
            note[word] -=1
        else:
            result = 'No'

def checkMagazine(magazine, note):
    result = 'Yes'
    for i in range(len(note)):
        try:
            magazine.pop(magazine.index(i))
        except ValueError:
            result = 'No'

    print(result)
"""

# Valid but too expensive at higher
# list counts
# def checkMagazine(magazine, note):
#
#
#    result = 'Yes'
#    for word in note:
#        if word not in magazine:
#            result = 'No'
#        else:
#            magazine.pop(magazine.index(word))
#    print(result)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
