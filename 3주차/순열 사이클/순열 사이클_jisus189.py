def dfs(num):
    while True:
        x=num
        visited[x] = True
        num = numbers[x]
        if visited[num]:
            break

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N
    result = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)