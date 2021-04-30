import sys
input = sys.stdin.readline
# 최대 부분 증가수열

# 맨 처음 시도했던 풀이
# 각 위치에서 교차하는 전깃줄 위치 저장
# 가장 많은 전깃줄과 교차하는 위치 삭제하면서 체크
# 오류: 가장 많은 전깃줄의 개수가 2개 이상일때
# a,b,c중에 a,b를 삭제하면 c가 자동으로 삭제돼서 2개만 삭제하면 되는데
# c를 먼저 삭제하면 a,b,c 3개를 삭제해야함

N = int(input())
ab_line = []
for _ in range(N):
    a, b = map(int, input().split())
    ab_line.append((a, b))
ab_line.sort(key=lambda x:x[1])
max_length = [1]*(N+1)
for i in range(1, N):
    for j in range(i):
        if ab_line[i][0] > ab_line[j][0]:
            max_length[i] = max(max_length[i], max_length[j]+1)

print(N - max(max_length))
    # tmp = max(a,b)
    # if maxV < tmp:
    #     maxV = tmp
# cross = [[] for _ in range(maxV+1)]
# cnt_cross = []
# for i in range(N):
#     a, b = power_pole[i]
#     cnt = 0
#     for j in range(N):
#         x, y = power_pole[j]
#         if (a > x and b < y) or (a < x and b > y):
#             cross[a].append((x,y))
#
# del_cnt = 0
# for c in range(len(cross)):
#     if cross[c]:
#         cnt_cross.append((len(cross[c]), c))
# # cnt_cross.sort()
#
# while cnt_cross:
#
#     for i in range(len(cross)):
#         if not cross:
#             break
#         j = 0
#         while j < len(cross[i]):
#             if cross[i][j][0] == x:
#                 del cross[i][j]
#                 break
#             j += 1
#     cnt_cross = []
#     if cross:
#         for c in range(len(cross)):
#             if cross[c]:
#                 cnt_cross.append((len(cross[c]), c))
#         # cnt_cross.sort()
#
# print(del_cnt)
# 가장 많이 겹치는 것이 여러 개일 경우 뭘 먼저 지우느냐에 따라 답이 달라질 수 있습니다.