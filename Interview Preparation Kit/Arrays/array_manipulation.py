# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)

    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        arr[a] += k
        arr[b] -= k

    max = 0
    sum = 0
    for num in arr:
        sum += num
        if sum > max:
            max = sum

    return max


def main():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    print(result)


main()
