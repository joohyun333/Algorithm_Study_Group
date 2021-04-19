# https://www.acmicpc.net/problem/14465
import itertools, sys

input = sys.stdin.readline
N, K, B = map(int, input().split())
board = [True] * (N + 1)
for i in range(B):
    n = int(input())
    board[n] = False
DP = [0] * (N+1)
count = 0
for i in range(1, K+1):
    if not board[i]:
        count += 1
DP[K] = count
result = count
for i in range(K+1, N+1):
    before = DP[i - 1] # 망가진 신호등 수
    if not board[i - K]:
        before -= 1
    if not board[i]:
        before += 1
    DP[i] = before
    result = min(result, before)
print(result)
