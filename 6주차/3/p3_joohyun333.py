import bisect, sys


def sliding_window(lst, d, k):
    min_aver = sys.maxsize
    for i in range(len(lst)):
        arr = []
        end = lst[i] + d
        a = bisect.bisect_right(lst, end) - 1
        if 0 <= a < len(lst) and lst[a] == end:
            idx_num = k-2
            new_lst = lst[i+1:a-1]
            arr.append(lst[i])
            arr.append(end)
            while idx_num > 0 and new_lst:
                arr.append(new_lst.pop(0))
                idx_num -= 1
        if len(arr) == k:
            min_aver = min(min_aver, sum(arr) // k)

    return min_aver


def solution(prices, d, k):
    p = sorted(prices)
    result = sliding_window(p, d, k)
    if p[-1] - p[0] <= d:
        return sum(p) // len(p)
    elif p[-2] - p[1] <= d:
        return sum(p[1:-1]) // (len(p) - 2)
    elif k == 1:
        return p[0]
    elif result < sys.maxsize:
        return result
    else:
        return p[(len(p) - 1) // 2]


prices, d, k = [4, 5, 6, 7, 8], 4, 3
print(solution(prices, d, k))
# 6
prices, d, k = [4, 5, 6, 7, 8], 2, 1
print(solution(prices, d, k))
# # 6
prices, d, k = [4, 5, 5, 7, 8], 1, 2
print(solution(prices, d, k))
# # 4
prices, d, k = [8, 4, 5, 7, 6], 1, 3
print(solution(prices, d, k))
# # 6

prices, d, k = [1, 8, 1, 8, 8], 6, 4
print(solution(prices, d, k))
# 8

prices, d, k = [8, 8, 8, 8, 8, 8, 8], 0, 1
print(solution(prices, d, k))
# 8

prices, d, k = [1, 22, 32 ,44, 22228], 10, 2
print(solution(prices, d, k))
# 27

prices, d, k = [1, 8, 1, 8, 1, 10, 10], 6, 4
print(solution(prices, d, k))
# 8