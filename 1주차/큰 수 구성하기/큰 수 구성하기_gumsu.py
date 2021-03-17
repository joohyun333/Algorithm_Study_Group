n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
res = 0

def DFS(x):
    global res
    if x > n:
        return
    res = max(res, x)
    for i in arr:
        DFS(10*x+i)
DFS(0)
print(res)