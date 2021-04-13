n = int(input())
solution = list(map(int, input().split()))
solution.sort()
# print(solution)

lt, rt = 0, n-1
mix = 1000000000*2
res = []

while lt < rt:
    temp = solution[lt] + solution[rt]

    if abs(temp) <= abs(mix):
        res = [lt, rt]
        mix = temp

        if mix < 0:
            lt += 1
        else:
            rt -= 1
        continue
    if temp < 0:
        lt += 1
        continue
    else:
        rt -= 1
        continue
    
# print(mix)
print(solution[res[0]], solution[res[1]])