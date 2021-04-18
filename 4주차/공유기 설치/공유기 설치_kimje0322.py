import sys
input = sys.stdin.readline
def check(distance):
    cnt = 1
    ep = house[0]
    for i in range(1, N):
        if house[i] - ep >= distance:
            cnt += 1
            ep = house[i]
    return cnt

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()
lt, rt = 0, house[N-1]
ans = 0
while lt <= rt:
    mid = (lt+rt)//2
    if check(mid) >= C:
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(ans)

