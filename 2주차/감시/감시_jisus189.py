
import sys

sys.setrecursionlimit(10**6)

direction= [(1,0),(-1,0),(0,1),(0,-1)]

cctv_pos = [[[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]],
[[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

def solution(x,y,temp,n_pos):

    for i in n_pos:
        nx, ny = x,y
        while True:
            nx += direction[i][0]
            ny += direction[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny]==6:
                    break
                elif temp[nx][ny]==0:
                    temp[nx][ny]="#"
            else:
                break

def dfs(board,count):
    global answer, cctv_count,n,m, cctv
    temp = board[:]

    if count == cctv_count:
        answer=min(answer,board.count(0))
        return
    x,y,num = cctv[count]
    for n_pos in cctv_pos[num]:
        solution(x,y,temp,n_pos)
        dfs(temp,count)
        temp=board[:]



if __name__=="__main__":
    n,m =map(int,sys.stdin.readline().split())

    board = [[0]*m for _ in range(n)]
    # 0~4 cctv num -1
    cctv = []
    cctv_count=0
    answer=n*m
    for i in range(n):
        temp=list(map(int,sys.stdin.readline().split()))
        for j in range(m):
            board[i][j]=temp[j]
            if 0<board[i][j]<6:
                cctv.append((i,j,board[i][j]))
                cctv_count +=1

    print(dfs(board,0))