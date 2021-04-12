from collections import deque
# 제자리 + 8방향
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

miro = [list(input()) for _ in range(8)]

def chess_bfs(x, y, height):
    q = deque()
    q.append((x, y, height))
    
    while q:
        a, b, now_height = q.popleft()
        for i in range(9):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < now_height and 0 <= ny < 8 and miro[nx][ny] == '.':
                if nx == 0 :
                    print(1)
                    return
                nx -= 1     # 미로 대신 사람을 올림
                if miro[nx][ny] == '.':
                    if nx == 0 :
                        print(1)
                        return
                    q.append((nx, ny, now_height-1))
    print(0)
    return
        
chess_bfs(7, 0, 8)
# print('-------------')
# for z in miro:
#     print(z)
# print('-------------')