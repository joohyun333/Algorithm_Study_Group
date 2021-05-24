# https://www.acmicpc.net/problem/9465
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    arr = []
    n = int(input())
    for i in range(2):
        arr.append(list(map(int, input().split())))
    DP = [[0] * (n + 1) for _ in range(2)]
    DP[0][1] = arr[0][0]
    DP[1][1] = arr[1][0]
    for i in range(2, n+1):
        DP[0][i] = arr[0][i-1] + max(DP[0][i-2], DP[1][i-2], DP[1][i-1])
        DP[1][i] = arr[1][i-1] + max(DP[1][i-2], DP[0][i-2], DP[0][i-1])
    print(max(DP[0][n], DP[1][n]))
