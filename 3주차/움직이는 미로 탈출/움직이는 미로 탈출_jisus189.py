import sys
from collections import deque

direction = [(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def bfs():
    global board, wall
    n=8
    start = (7, 0)
    is_end = 0
    nq = deque()

    nq.append(start)


    while nq:
        visited = [[0]* n for _ in range(n)]

        # move
        temp=deque()
        for _ in range(len(nq)):
            x,y = nq.popleft()
            if (x,y) == (0,7):
                is_end=1
                return is_end
            if board[x][y]=='#':
                continue

            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if 0<= nx < n and 0 <= ny < n:
                    if board[nx][ny]=='#': continue
                    if visited[nx][ny]: continue
                    visited[nx][ny]=1
                    temp.append((nx,ny))
        nq = temp

        # wall
        temp = []
        temp_board = [['.']*n for _ in range(n)]
        for w in wall:
            if 0<= w[0]+1 < n:
                temp_board[w[0]+1][w[1]]='#'
                temp.append((w[0]+1,w[1]))
        wall = temp[:]
        board = [temp_board[i][:] for i in range(n)]

    return is_end

#sys.stdin = open("input.txt")

board = []
wall = []
for i in range(8):
    temp =list(map(str,input().strip()))
    for j in range(len(temp)):
        if temp[j]=='#':
            wall.append((i,j))
    board.append(temp)

print(bfs())