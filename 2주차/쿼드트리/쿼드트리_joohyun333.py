N = int(input())
data = []
for i in range(N):
    data.append(input())
result = ""
def DC(arr, n):
    global result
    if len(set(list(''.join(arr)))) == 1:
        result += ''.join(set(list(''.join(arr))))
        print(set(list(''.join(arr))) , result)
        return
    result+="("
    DC([i[:n // 2] for i in arr[:n // 2]], n // 2)
    DC([i[n // 2:] for i in arr[:n // 2]], n // 2)
    DC([i[:n // 2] for i in arr[n // 2:]], n // 2)
    DC([i[n // 2:] for i in arr[n // 2:]], n // 2)
    result+=")"
DC(data, N)
print(result)
