#!/bin/python3

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    path = list()
    i = 0
    while True:
        if i == len(c) - 1:
            return len(path)

        if i + 2 <= len(c) - 1:
            if c[i + 2] == 0:
                path.append(c[i + 2])
                i += 2
            else:
                path.append(c[i + 1])
                i += 1
        else:
            path.append(c[i + 1])
            i += 1

def main():
    n = int(input('Enter number of clouds: '))
    c = list(map(int, input('Enter path: ').rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)

main()
