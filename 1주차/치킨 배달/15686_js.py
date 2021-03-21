from itertools import combinations
 
def solution():
    global chicken, house, answer
    for ch in combinations(chicken, M):
        now_sum = 0
        for home in house:
            now_sum += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
            if answer <= now_sum: break
        if now_sum < answer: answer = now_sum



if __name__=="__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    house = []
    chicken = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1: house.append((i, j))
            elif board[i][j] == 2: chicken.append((i, j))
                
    answer = float('inf')
    solution()
    print(answer)
