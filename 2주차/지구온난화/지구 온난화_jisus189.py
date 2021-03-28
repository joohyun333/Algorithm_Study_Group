import sys

direction= [(1,0),(-1,0),(0,1),(0,-1)]

def solution(r,c,board):
    global land, land_count
    temp = board[:]
    now_r, now_c = r,c

    land, temp = chk_land(land,temp)

    if land_count != len(land):

        now_r,now_c,temp=squeeze_map(land)

    for i in range(now_r):
        for j in range(now_c):
            print(temp[i][j],end="")
        print("\n")
    return

def chk_land(land,temp):
    global board,r,c
    temp_land = []
    save =[]
    for i, j in land:
        count = 0
        for d in direction:
            if 0<=i+d[0]<r and 0<=j+d[1]<c:
                if board[i+d[0]][j+d[1]]==".":
                    count+=1
            else:
                count+=1
        if count>=3:
            save.append((i,j))
        else:
            temp_land.append((i,j))
    for i,j in save:
        temp[i][j]="."
    land = temp_land[:]
    return land, temp

def squeeze_map(land):
    land_x = []
    land_y = []
    if len(land)==1:
        return land[0][0],land[0][1],land
    elif len(land)==0:
        return 1,1,'.'
    for i,j in land:
        land_x.append(i)
        land_y.append(j)
    land_x.sort()
    land_y.sort()

    temp_board=[['.'] * land_y[-1] for _ in range(land_x[-1])]

    for i,j in land:
        temp_board[i-land_x[0]][j-land_y[0]]="X"

    return land_x[-1],land_y[-1],temp_board

if __name__=="__main__":
    r,c = map(int,sys.stdin.readline().split())

    board = []
    land = []
    land_count =0
    for i in range(r):
        board.append(list(input()))

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'X':
                land.append((i, j))
                land_count+=1

    solution(r,c,board)

