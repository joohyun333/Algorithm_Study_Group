# https://www.acmicpc.net/problem/2565
import sys

input = sys.stdin.readline
arr = []
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr = [j for i, j in sorted(arr, key=lambda a: a[0])]
asc = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            asc[i] = max(asc[i], asc[j] + 1)
print(N-max(asc))