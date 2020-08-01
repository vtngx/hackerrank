#!/bin/python3
import math


# Complete the rotLeft function below.
def rotLeft(a, d):
    resultArr = []
    # if number of rotations % length of array
    # then rotate back to default position
    if d % len(a) == 0:
        return a
    else:
        n = d - (math.floor(d / len(a)) * len(a))

        for i in range(n, len(a)):
            resultArr.append(a[i])

        for i in range(0, n):
            resultArr.append(a[i])

    return resultArr


def main():
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    print(result)


main()
