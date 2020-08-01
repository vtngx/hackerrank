# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arr = [i - 1 for i in arr]
    swaps = 0
    i = 0
    while True:
        v = arr[i]
        if v != i:
            arr[i], arr[v] = arr[v], arr[i]
            swaps += 1
        else:
            i += 1
        if i == len(arr) - 1:
            break
    return swaps


def main():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print(res)


main()
