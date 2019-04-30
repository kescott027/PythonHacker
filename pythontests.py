#!/bin/python3


def weird(N):

    if 5 <= N <= 21 or N % 2 != 0:
        return "Weird"
    else:
        return "Not Weird"


if __name__ == '__main__':



    inputs = [1, 2, 3, 4, 5, 6, 13, 20, 21, 22, 58, 99]
    expected = ["Weird", "Not Weird", "Weird", "Not Weird", "Weird", "Weird", "Weird", "Weird", "Weird", "Not Weird", \
        "Not Weird", "Weird"]

    failures = 0
    i = 0
    while i < len(inputs):
        expect = expected[i]
        result = weird(inputs[i])

        if result != expect:
            print("Failure:\ninput:{0}\nouput: {1}\nexpected: {2}".format(inputs[i], result, expect))
            failures += 1
        else:
            # print("Success:\ninput: {0}\noutput: {1}".format(inputs[i], result))
            pass
        i += 1

    if failures > 0:
        print("Test cases failed.")
    else:
        print("All cases Pass successfully")

