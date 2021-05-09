# https://www.acmicpc.net/problem/9252
import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()


def LCS(a, b, c):
    DP = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for z in range(1, len(c) + 1):
                if a[i - 1] == b[j - 1] == c[z - 1]:
                    DP[i][j][z] = DP[i - 1][j - 1][z - 1] + 1
                else:
                    DP[i][j][z] = max(DP[i - 1][j][z], DP[i][j - 1][z], DP[i][j][z - 1])
    return DP[len(a)][len(b)][len(c)]


print(LCS(a, b, c))
