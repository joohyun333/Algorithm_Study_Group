min_dp = [0]*101

min_dp[2] = 1
min_dp[3] = 7
min_dp[4] = 4
min_dp[5] = 2
min_dp[6] = 6
min_dp[7] = 8
min_dp[8] = 10
min_dp[9] = 18
min_dp[10] = 22
min_dp[11] = 20
min_dp[12] = 28
min_dp[13] = 68
min_dp[14] = 88
min_dp[15] = 108
min_dp[16] = 188
min_dp[17] = 200

for i in range(18, 101):
    min_dp[i] = int(str(min_dp[i-7]) + str(8))


t = int(input())
for _ in range(t):
    n = int(input())

    print(min_dp[n], end=' ')

    if n % 2 == 0:
        print('1'*(n//2))
    else:
        print('7'+'1'*(n//2-1))