first, second, third = input(), input(), input()

dp = [[[0]*(len(third)+1) for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        for k in range(1, len(third)+1):
            if first[i-1] == second[j-1] == third[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])