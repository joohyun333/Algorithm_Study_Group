# 메모리 초과
from itertools import permutations
import sys

def formatting(word):
  result = []
  for i in range(len(word)):
    result.append(word[i])
  return sorted(result)

def solution(words):
  words = list(map(formatting, words))
  answer = []
  for word in words:
    candidates = list(permutations(word, len(word)))
    for candidate in candidates:
      answer.append(''.join(candidate))

  for i in range(len(answer)-1):
    if i == i + 1:
      answer.remove(i)
    print(answer[i])

input = sys.stdin.readline
n = int(input())
words = [input() for _ in range(n)]
solution(words)
