#!/bin/python3
from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if Counter(note) - Counter(magazine) == Counter():
        print('Yes')
    else:
        print('No')


def main():
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)

main()
