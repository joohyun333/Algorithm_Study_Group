import sys

def DFS(now, times):
    
    global N, arr, answer
    
    if now > N:
        
        return

    answer = max(answer, now)
    
    for i in range(len(arr)):
        
        DFS(now+times * arr[i],times*10)






if __name__=="__main__":
    
    N, K = map(int,sys.stdin.readline().split())
    
    arr=list(map(int, sys.stdin.readline().split()))
    
    arr.sort()
    
    answer = 0
    
    DFS(0,1)

    print(answer)
    
