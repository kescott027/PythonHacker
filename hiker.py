#!/bin/python3

import math
import os
import random
import re
import sys


class Walk(object):

    def __init__(self, n, s):
        self.steps = n - 1
        self.path = s
        self.cursor = 0
        self.elevation = 0
        self.valley_count = 0
        self.mountain_count = 0
        self.walking = True

    def begin(self):

        self.findterrain()
        return

    def report(self):

        if self.walking is False:
            return self.valley_count

        else:
            return None

    def step(self):

        terrain = self.path[self.cursor]

        if terrain == 'D':
            self.elevation -= 1

        elif terrain == 'U':
            self.elevation += 1

        else:
            pass

        if int(self.cursor) >= int(self.steps):
            self.walking = False
            return

        else:
            self.cursor += 1
            return

    def findterrain(self):

        while self.walking is True:
            self.step()

            if self.elevation < 0:
                self.walkvalley()

            elif self.elevation > 0:
                self.walkmountain()

        return

    def walkvalley(self):

        self.valley_count += 1

        while self.walking is True:
            self.step()

            if self.elevation >= 0:
                break
        return

    def walkmountain(self):

        self.mountain_count += 1

        while self.walking is True:
            self.step()

            if self.elevation <= 0:
                break
        return


# Complete the countingValleys function below.
def countingValleys(n, s):
    """
    n number of steps.
    s string describing path n characters describing path.
      path contains characters U and D for [Up] and [Down]
      respectively
      2<=n<=10**6
    """

    my_journey = Walk(n, s)
    my_journey.begin()

    return my_journey.report()


if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = "DDDUUUDDUUDDUUUDDUUUDDUDDDDDDDUUUUUU"
    # expected = 5

    s = "UDDDUDUU"
    expected = 1
    n = len(s) - 1

    result = countingValleys(n, s)

    if result == expected:
        print("Success")

    else:
        print("Failure")

    print("results: {0}\nexpected:{1}".format(result, expected))

    # fptr.write(str(result) + '\n')

    # fptr.close()


