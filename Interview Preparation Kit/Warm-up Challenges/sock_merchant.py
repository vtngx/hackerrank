#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colorsCount = dict()
    pairs = 0
    for color in ar:
        colorsCount[color] = colorsCount.get(color, 0) + 1
    for (color, count) in colorsCount.items():
        pairs += int(math.floor(count / 2))
    return pairs


def main():
    n = int(input('Number of socks? '))
    ar = list(map(int, input('Colors of socks? ').rstrip().split()))
    result = sockMerchant(n, ar)
    print('Number of pairs of socks:', result)

main()
