N, K, B = map(int, input().split())
traffic_light = [True for i in range(N+1)]
for idx in range(B):
    traffic_light[int(input())] = False
cnt = [0]*(N-K+1)
tmp = 0
for i in range(1, K+1):
    if not traffic_light[i]:
        tmp += 1
cnt[0] = tmp

for j in range(2, N-K+2):
    if not traffic_light[j-1]:
        tmp -= 1
    if not traffic_light[j+K-1]:
        tmp += 1
    cnt[j-1] = tmp
print(min(cnt))

# 시간초과
# s, e = 0, K-1
# while e < N:
#     s += 1
#     e += 1
#     for i in range(s, e+1):
#         if not traffic_light[i]:
#             cnt[s-1] += 1

