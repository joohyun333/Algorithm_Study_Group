# https://www.acmicpc.net/problem/2470
import sys, bisect, heapq

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr = [-1000000001] + arr + [1000000001]
result = sys.maxsize
queue = []
for i in range(1, N+1):
    a = bisect.bisect_left(arr, -arr[i])
    b = [j for j in [a - 1, a, a + 1] if 1 <= j <= N and arr[i] != arr[j]]
    for j in b:
        c = abs(arr[j] + arr[i])
        if result >= c:
            result = c
            heapq.heappush(queue, (c, arr[i], arr[j]))
answer = heapq.heappop(queue)[1:]
answer = sorted(answer)
print(answer[0], answer[1])

