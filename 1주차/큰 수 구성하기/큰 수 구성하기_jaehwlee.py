from itertools import product
import sys

input = sys.stdin.readline

def solution(n, k, r):
  while r > 0:
    available = list(product(k, repeat=r))
    for value in available:
      now = int(''.join(value))
      if now <= n:
        return now
    r -= 1
  return

n, num_k = map(int, input().split())
k = list(map(str, sorted(list(map(int, input().split())), reverse=True)))
r = len(str(n))

print(solution(n, k, r))
