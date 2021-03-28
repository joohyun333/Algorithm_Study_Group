# https://www.acmicpc.net/problem/14391
import itertools, sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [input() for _ in range(N)]

result = 0

for m in itertools.product(itertools.product([0, 1], repeat=M), repeat=N):
    total = []
    for a in range(N):
        s = ""
        for b in range(M):
            if m[a][b] == 1:
                s += str(arr[a][b])
            elif m[a][b] == 0:
                s += " "
        total.append(sum(list(map(int, s.split()))))
    row = sum(total)

    total = []
    for a in range(M):
        s = ""
        for b in range(N):
            if m[b][a] == 0:
                s += str(arr[b][a])
            elif m[b][a] == 1:
                s += " "
        total.append(sum(list(map(int, s.split()))))
    col = sum(total)

    result = max(result, row + col)
print(result)
