#!/bin/python3
import math

# Complete the repeatedString function below.
def repeatedString(s, n):
    numStrDuplicates = math.floor(n / len(s))
    strResidual = s[0 : (n - (numStrDuplicates * len(s)))]
    totalNumOfA = (s.count('a') * numStrDuplicates) + strResidual.count('a')
    return totalNumOfA


def main():
    # kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm
    s = input('Enter string: ')
    # 736778906400
    n = int(input('Enter number of chars: '))
    # 51574523448
    result = repeatedString(s, n)
    print('Number of a:', result)

main()
