def DFS(x):
    visited[x] = True

    if not visited[matrix[x-1][1]]:
        DFS(matrix[x-1][1])

t = int(input())
for _ in range(t):
    n = int(input())
    permutation = list(map(int, input().split()))
    matrix = []
    visited = [False for _ in range(n+1)]
    cnt = 0

    for idx, value in enumerate(permutation):
        matrix.append([idx+1, value])
    
    for i in range(1, n+1):
        if not visited[i]:
            DFS(i)
            cnt += 1
    
    print(cnt)