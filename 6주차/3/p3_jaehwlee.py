# prices = [4, 5, 6, 7, 8]
# d =	4	
# k = 3	

# prices = [4, 5, 6, 7, 8]	
# d = 2	
# k = 1	

# prices = [4, 5, 6, 7, 8]
# d=1
# k=2	

# prices = [8, 4, 5, 7, 6]	
# d=1	
# k=3	

# prices = [1, 8, 1, 8, 1, 8]	
# d=6	
# k=4	

#result = 4
prices = [1, 5, 9, 10, 2, 3]
d = 8
k = 1

from itertools import combinations


def solution(prices, d, k):
  flag = False
  prices.sort()
  
  if prices[-1] - prices[0] <= d:
    return sum(prices) // len(prices)
  
  else:
    if prices[-2] - prices[1] <= d:
      return sum(prices[1:-1]) // (len(prices)-2)

    else:
      c_list = combinations(prices, k)

      for c in c_list:
        if max(c) - min(c) <= d:
          flag = True
          return sum(c) // len(c)

      if not flag:
        if len(prices) % 2 == 0:
          return prices[len(prices)//2-1]
        else:
          return prices[len(prices)//2]
        
print(solution(prices, d, k))
