# https://www.acmicpc.net/problem/10451
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    arr = [0]+list(map(int, input().split()))
    discoverd = [True]+[False]*N
    result = 0
    def dfs(n):
        global result
        discoverd[n] = True
        Next = arr[n]
        if discoverd[Next]:
            result +=1
            return
        else:
            dfs(Next)

    for i in range(1, N+1):
        if not discoverd[i]:
            dfs(i)
    print(result)