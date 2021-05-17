t = int(input())
for _ in range(t):
    n = int(input())
    stiker = []
    for _ in range(2):
        stiker.append((list(map(int, input().split()))))
    
    dp = [[0]*n for _ in range(2)]

    dp[0][0], dp[1][0] = stiker[0][0], stiker[1][0]

    if n >1 :
        dp[0][1] = dp[1][0] + stiker[0][1]
        dp[1][1] = dp[0][0] + stiker[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1] + stiker[0][i], dp[1][i-2] + stiker[0][i])
        dp[1][i] = max(dp[0][i-1] + stiker[1][i], dp[0][i-2] + stiker[1][i])
    
    print(max(dp[0][n-1], dp[1][n-1]))