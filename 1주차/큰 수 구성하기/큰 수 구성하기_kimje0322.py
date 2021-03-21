def dfs(idx):
    global maxV, ans
    # 처음 idx > n이라고 작성했더니 문제 다시 읽고 안돼서 고침
    # 반례 여러가지 넣다가 깨달음
    if idx > N or (ans and N < int(ans)):
        return
    if ans and N >= int(ans):
        maxV = max(maxV, int(ans))

    for i in num:
        ans += i
        dfs(idx+1)
        ans = ans[:len(ans)-1]
    return maxV

N, n = map(int, input().split())
num = list(input().split())
ans = ''
maxV = 0
print(dfs(0))

