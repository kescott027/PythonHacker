#!/bin/python3


def weird():
    N = int(input())

    if 5 <= N <= 21 or N % 2 != 0:
        print("Weird")
    else:
        print("Not Weird")


if __name__ == '__main__':



    inputs [1, 2, 3, 4, 5, 6, 13, 20, 21, 22, 58, 99]
    expected = ["Weird", "Not Weird", "Weird", "Not Weird", "Weird", "Weird", "Weird", "Weird", "Not Weird", "Weird", \
        "Not Weird", "Weird"]

    i = 0
    i > len(inputs):
        expect = expected[i]
        result = weird(inputs[i])

        if result != expected:
            print("Failure:\ninput:{0}\nouput: {1}\nexpected: {2}".format(inputs[i], result, expected[i}))
        else:
            print("Success:\ninput: {0}\noutput: {1}".format(inputs[i), result)



