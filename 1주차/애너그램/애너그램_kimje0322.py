import sys
input = sys.stdin.readline

def perm(idx):
    global ans
    n = len(alp)
    if idx == n:
        answer.append(ans)
        return
    overlap = 'none'
    for i in range(n):
        if not selected[i] and overlap != alp[i]:
            selected[i] = 1
            ans += alp[i]
            overlap = alp[i]
            perm(idx+1)
            selected[i] = 0
            ans = ans[:len(ans)-1]
    return

N = int(input())
for _ in range(N):
    alp = sorted(input())
    selected = [0]*len(alp)
    ans = ''
    answer = []
    perm(0)
    for x in answer:
        print(x)
