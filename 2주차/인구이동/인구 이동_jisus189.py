import sys

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(board):
    global n
    is_move = True
    answer = 0
    while is_move:
        # 이동이 없을 때까지 반복
        is_move = False
        visited = [[0] * n for _ in range(n)]
        all_unions =[]
        # 연결
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 1:
                    continue
                total,union = dfs(i,j,board,visited)
                if len(union)>1:
                    is_move = True
                    all_unions.append((total,union))

        #print(answer,board,all_unions)
        if is_move:
            for i in range(len(all_unions)):
                total = all_unions[i][0]
                union = all_unions[i][1]
                for x, y in union:
                    board[x][y] = int(total / len(union))
            answer += 1
        else:
            break

    return answer


def dfs(i, j, board, visited):
    global n, l, r
    stack = []
    union = []
    total = 0
    stack.append((i, j))

    while stack:
        x, y = stack.pop()

        if visited[x][y] == 0:

            visited[x][y]=1
            union.append((x, y))
            total += board[x][y]
        for d in direction:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < n and 0 <= ny < n:

                if (nx,ny) not in union:
                    k = abs(board[x][y] - board[nx][ny])
                    if l <=  k <= r:

                        stack.append((nx, ny))


    return total,union

if __name__ == "__main__":
    n, l, r = map(int, sys.stdin.readline().split())

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    print(solution(board))
