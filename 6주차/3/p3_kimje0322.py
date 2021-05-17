# from itertools import combinations
# 슬라이딩 윈도우
from collections import deque

def solution(prices,d,k):
    prices.sort()
    answer = 0
    # 조건1
    if prices[-1] - prices[0] <= d:
        answer = sum(prices) // len(prices)
    # 조건2
    else:
        if prices[-2] - prices[1] <= d:
            prices = deque(prices)
            prices.pop()
            prices.popleft()
            answer = sum(prices) // len(prices)
        # 조건3
        else:
            queue = deque()
            idx, tmp = 0, 0
            flag = False
            while idx < len(prices):
                if len(queue) < k:
                    queue.append(prices[idx])
                    tmp += prices[idx]
                if len(queue) == k:
                    min_num = queue[0]
                    max_num = queue[-1]
                    if max_num - min_num <= d:
                        answer = tmp // len(queue)
                        flag = True
                        break
                    queue.popleft()
                    tmp -= min_num
                idx += 1
            if not flag:
                n = len(prices)
                if n % 2:
                    answer = prices[n//2]
                else:
                    answer = prices[n//2-1]
    return answer


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
# 9

# print(solution([4, 5, 6, 7, 8],4,3))
# print(solution([4, 5, 6, 7, 8],2,1))
# print(solution([4, 5, 6, 7, 8],1,2))
# print(solution([8, 4, 5, 7, 6],1,3))
# print(solution([1, 8, 1, 8, 1, 8],6,4))
# print(solution([1, 22,32,44,22228],10,2))


# lst = list(combinations(prices,k))
# tmp = 999999
# for data in lst:
#     if abs(data[-1]-data[0]) <= d:
#         flag = True
#         tmp = min((data[-1]+data[0])//2, tmp)