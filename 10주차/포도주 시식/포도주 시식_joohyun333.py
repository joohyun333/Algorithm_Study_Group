arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
print(arr)
DP = [0]*(n+1)
DP[1] = arr[0]
for i in range(2, n+1):
    DP[i] = max(arr[i-1] + max(arr[i-2]+DP[i-3], DP[i-2]), DP[i-1]) #3
print(DP)
