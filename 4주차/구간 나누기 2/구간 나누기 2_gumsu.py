n, m = map(int, input().split())
num_list = list(map(int ,input().split()))

def divide(count):
    cnt = 1
    min_num = max_num = num_list[0]

    for i in range(1, n):
        min_num = min(min_num, num_list[i])
        max_num = max(max_num, num_list[i])
        if max_num - min_num > count:
            cnt += 1
            min_num = max_num = num_list[i]
    return cnt

lt, rt = 0, max(num_list)

while lt <= rt:

    mid = (lt+rt) // 2

    if divide(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)