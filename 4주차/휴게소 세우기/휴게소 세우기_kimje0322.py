from copy import deepcopy
import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
data = [0] + sorted(list(map(int, input().rstrip().split())))+[L]

lt = 0
rt = L

while lt <= rt:
    mid = lt + (rt - lt) // 2
    i = 0
    cnt = M
    tmp = deepcopy(data)
    possible = False

    while True:
        if cnt > 0:
            if tmp[i] + mid < tmp[i+1]:
                tmp.insert(i+1, tmp[i]+mid)
                cnt -= 1

        else:
            if tmp[i] + mid < tmp[i+1]:
                possible = True
                break

        i += 1
        if tmp[i] == L:
            break

    if possible:
        lt = mid + 1
    else:
        rt = mid - 1
print(lt)


