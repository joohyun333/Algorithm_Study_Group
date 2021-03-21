import sys


direction = [(-1, 0), (1, 0), (0, -1), (0, 1),(0,0)]

def chk_visit(i, j, visited):
    for idx in range(5):
        ni = i + direction[idx][0]
        nj = j + direction[idx][1]
        if (ni, nj)  in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    
    if total >= answer:return
    
    if len(visited) == 15:
        
        answer = min(answer, total)
        
    else:
        for i in range(1, N-1):
            
            for j in range(1, N-1):
                
                if chk_visit(i, j, visited):
                    temp=[]
                    temp_cost=0
                    for idx in range(5):
                        
                        ni = i + direction[idx][0]
                        nj = j + direction[idx][1]
                        temp.append((ni, nj))
                        temp_cost += fields[ni][nj]
                    dfs(visited + temp, total + temp_cost)




if __name__=="__main__":
    
    N = int(input())
    
    answer =  float('inf')
    
    fields = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dfs([], 0)

    print(answer)
