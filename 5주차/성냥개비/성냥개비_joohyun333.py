# https://www.acmicpc.net/problem/3687
import sys
input = sys.stdin.readline
arrs = [int(input()) for _ in range(int(input()))]

max_DP = [0] * 101
for i in range(2, 101):
    if i % 2 == 0:
        max_DP[i] = int((i // 2) * "1")
    elif i % 2 == 1:
        max_DP[i] = int("7" + "1" * str(max_DP[i - 3]).count("1"))

min_num = [0, 0, 1, 7, 4, 2, 0, 8, 10]
min_DP = min_num+[0]*92
min_DP[6] = 6
for i in range(9, 101):
    min_DP[i] = min_DP[i-2]*10 + min_num[2]
    for j in range(3, 8):
        min_DP[i] = min(min_DP[i], min_DP[i-j]*10 + min_num[j])
for i in arrs:
    print(min_DP[i], max_DP[i])