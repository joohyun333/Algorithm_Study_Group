import sys
input = sys.stdin.readline

N = int(input())
ab_line = []
for _ in range(N):
    a, b = map(int, input().split())
    ab_line.append((a, b))
ab_line.sort(key=lambda x:x[1])
max_length = [1]*(N+1)
for i in range(1, N):
    for j in range(i):
        if ab_line[i][0] > ab_line[j][0]:
            max_length[i] = max(max_length[i], max_length[j]+1)

print(N - max(max_length))