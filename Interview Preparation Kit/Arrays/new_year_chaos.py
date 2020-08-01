#   1 2 5 3 7 8 6 4
#   1 2 3 4 5 6 7 8

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0

    for i, p in enumerate(q):
        if (p - 1) - i > 2:
            print("Too chaotic")
            return
        for j in range(max(p - 2, 0), i):
            if q[j] > p:
                bribes += 1

    print(bribes)


def main():
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)


main()
