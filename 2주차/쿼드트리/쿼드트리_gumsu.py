def cut(x, y, num):
    check = int(arr[x][y])

    for i in range(x, x+num):
        for j in range(y, y+num):
            if check != int(arr[i][j]):
                print('(', end='')
                cut(x, y, num//2)
                cut(x, y+num//2, num//2)
                cut(x+num//2, y, num//2)
                cut(x+num//2, y+num//2, num//2)
                print(')', end='')
                return
    if check == 1:
        print(1, end='')
        return
    else:
        print(0, end='')
        return

n = int(input())
arr = [list(input()) for _ in range(n)]

cut(0, 0, n)

# for z in arr:
#     print(z)