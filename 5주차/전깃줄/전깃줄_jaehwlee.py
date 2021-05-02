n = int(input())
e_lines = []

for _ in range(n):
    a, b = map(int, input().split())
    e_lines.append((a, b))


def solution(n):
  e_lines.sort(key=lambda x: x[1])
  max_len = [1] * n
  for i in range(1, n):
    for j in range(i):
        if e_lines[i] > e_lines[j]:
            max_len[i] = max(max_len[i], max_len[j] + 1)

  answer = n - max(max_len)
  return answer

solution(n)
