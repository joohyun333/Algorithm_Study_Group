import itertools, sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
n = len(str(N))
while K > 0:
    result = []
    for i in itertools.product(arr, repeat=n):
        a = int(''.join(map(str, i)))
        if a <= N:
            result.append(a)
    if result:
        print(max(result))
        break
    else:
        n -= 1
