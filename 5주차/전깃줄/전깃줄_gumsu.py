n = int(input())
wire = []
for _ in range(n):
    a, b = map(int, input().split())
    wire.append((a, b))

wire.sort(key= lambda x: x[1])
max_length = [1]*n

for i in range(1, n):
    for j in range(i):
        if wire[i] > wire[j]:
            max_length[i] = max(max_length[i], max_length[j] + 1)

print(n-max(max_length))