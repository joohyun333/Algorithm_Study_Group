# https://www.acmicpc.net/problem/6443
import collections, sys, heapq, copy

input = sys.stdin.readline
for i in range(int(input())):
    a = input().strip("\n")
    alphas = collections.Counter(a)
    queue = []
    def backtracking(alpha, co):
        if len(alpha) == len(a):
            heapq.heappush(queue, alpha)
            return

        for z in co:
            if co[z] > 0:
                co_al = copy.deepcopy(co)
                co_al[z] -= 1
                backtracking(alpha + z, co_al)


    for j in alphas:
        copy_alphas = copy.deepcopy(alphas)
        copy_alphas[j] -= 1
        backtracking(j, copy_alphas)

    while queue:
        print(heapq.heappop(queue))
