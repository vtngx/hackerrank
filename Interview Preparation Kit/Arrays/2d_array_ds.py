# Complete the hourglassSum function below.
def hourglassSum(arr):
    sumList = list()
    for i in range(4):
        for j in range(4):
            s = 0
            s += arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            s += arr[i + 1][j + 1]
            s += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            sumList.append(s)
    return max(sumList)


def main():
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print('Max hourglass sum in arr:', result)


main()
