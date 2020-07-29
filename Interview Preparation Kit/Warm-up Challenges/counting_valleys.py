#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sealevel = 0
    isValley = False
    count = 0

    for c in s:
        if c == 'U':    sealevel += 1
        elif c == 'D':  sealevel -= 1

        if sealevel == -1 and c == 'D':
            isValley = True

        if sealevel == 0 and isValley:
            count += 1
            isValley = False

    return count

def main():
    n = int(input('Enter steps: '))
    s = input('Enter path: ')
    result = countingValleys(n, s)
    print('Number of valleys:',result)

main()
